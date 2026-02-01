from fastapi import FastAPI, Response , status , HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind = engine)

app = FastAPI()


class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    # rating: Optional[int] = None

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
#this is path operation or route 
#this decorator to make the normal function to connect with a fastapi like @ is just the start of any decorator , the app is the # fastapi instance and the .get is the http method and in the bracket there is path , the slash is the root path
@app.get("/") #decorator
async def root(): #this is just a simple function and async for long duration task
    return {"message": "My world of api"}


@app.get("/sqlalchemy")
def test_posts(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    #here the query method created a query and to run that query we need to run a method for example here is .all()
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


#getting all the post
@app.get("/posts")
def get_posts(db : Session = Depends(get_db)):
    posts = db.query(models.Post).all()

    # cursor.execute(""" SELECT * FROM posts """) using raw sql
    # posts = cursor.fetchall()

    return{"data" : posts}



#creating the post
#here we change the http response using status code
@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post: Post, db : Session = Depends(get_db)):
    # post_dict = post.model_dump()
    # post_dict['id'] = randrange(0,1000000)
    # my_posts.append(post_dict)


# RAW SQL CODE 
    # cursor.execute(""" INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    #                (post.title, post.content, post.published)) 
    # new_posts = cursor.fetchone()
    # conn.commit()
    # print(**post.model_dump())
    # new_posts = models.Post(title = post.title, content = post.content, published = post.published)
    # Instead of writing each model field manually, convert the data to a dictionary
    # and unpack it. This gives the same result and is cleaner and easier.

    new_posts = models.Post(**post.model_dump())
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return{"data" : new_posts} 


#getting one individual post
@app.get("/posts/{id}") #here the {id} is the path parameter
def get_post(id : int, db : Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id),))
    # post = cursor.fetchone()
    # post = find_post(id)#the path function return the id in string so to work we should convert that parameter in int

    post = db.query(models.Post).filter(models.Post.id==id).first()

    if not post:
        raise HTTPException (status_code= status.HTTP_404_NOT_FOUND,detail = f"post with {id} was not found")
    return {"Post_Details" :  post}


@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id : int, db : Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    # index = find_index_post(id)

    deleted_post = db.query(models.Post).filter(models.Post.id==id)

    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"post with id: {id} does not exist")
    

    deleted_post.delete(synchronize_session=False)
    db.commit()

    # my_posts.pop(deleted_post)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# We return 204 No Content for DELETE requests
# to indicate successful deletion without sending any response data.


# @app.put("/posts/{id}")
# def update_post(id: int, post:Post, db : Session = Depends(get_db)):
#     # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, 
#     #                (post.title, post.content, post.published, str(id),))
    
#     # updated_post = cursor.fetchone()

#     # conn.commit()

    
#     # index = find_index_post(id)


#     post_query = db.query(models.Post).filter(models.Post.id==id)
#     post = post_query.first()

#     if post == None:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
#                             detail= f"post with {id} does not exist")
    
#     post_query.update(post.model_dump(), synchronize_session= False)
#     db.commit()
#     # post_dict = post.model_dump() #here the data we get from the post which is written in the function and converted into regular python dictionary
#     # post_dict["id"] = id  #this line add the id in each post dictionary , this id does not send by the user it is copy from the path url 
#     # my_posts[index] = post_dict #this line replace the context in the particular index of my_post. It get replaced with the content of present in post_dict

#     return{"data" : post_query.first()}


@app.put("/posts/{id}")
def update_post(id: int, updated_post: Post, db: Session = Depends(get_db)):

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
