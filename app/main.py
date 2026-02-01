from fastapi import FastAPI, Response , status , HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres'
                                , password = 'god', cursor_factory= RealDictCursor)   
        cursor = conn.cursor()
        print("Database connection is successfull!") 
        break
    except Exception as e:
        print("Connecting to database failed")
        print("Error: ", e)
        time.sleep(2)


my_posts = [{"title" : "title of the first post", "content":"Content of the first post", "id": 1} 
             ,{"title": "Library", "content":"This library content all types of book", "id" : 2}]

@app.get("/") #decorator
async def root(): 
    return {"message": "My world of api"}


@app.get("/sqlalchemy")
def test_posts(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    print(posts)
    return{"data" : "successful"}

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
         return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i    
        
@app.get("/posts")
def get_posts(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return{"data" : posts}


@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post: schemas.PostCreate, db : Session = Depends(get_db)):
    new_posts = models.Post(**post.model_dump())
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return{"data" : new_posts} 

@app.get("/posts/{id}")
def get_post(id : int, db : Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException (status_code= status.HTTP_404_NOT_FOUND,detail = f"post with {id} was not found")
    return {"Post_Details" :  post}


@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id : int, db : Session = Depends(get_db)):
    deleted_post = db.query(models.Post).filter(models.Post.id==id)
    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"post with id: {id} does not exist")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} does not exist"
        )
    post_query.update(updated_post.model_dump() , synchronize_session=False)
    db.commit()

    return {"data": post_query.first()}
