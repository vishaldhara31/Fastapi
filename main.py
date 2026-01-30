from fastapi import FastAPI, Response , status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

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
def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    return{"data" : posts}

#creating the post
#here we change the http response using status code
@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(""" INSERT INTO posts(title, content, published) VALUES (%s, %s, %s) RETURNING * """,
                   (post.title, post.content, post.published))
    new_posts = cursor.fetchone()
    conn.commit()
    return{"data" : new_posts} #this is a dictonary and it convertes to a json file later

# getting one individual post
@app.get("/posts/{id}") #here the {id} is the path parameter
def get_post(id : int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id),))
    post = cursor.fetchone()
    # post = find_post(id)#the path function return the id in string so to work we should convert that parameter in int
    if not post:
        raise HTTPException (status_code= status.HTTP_404_NOT_FOUND,detail = f"post with {id} was not found")
    return {"Post_Details" :  post}

#delete
@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"post with id: {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#update
@app.put("/posts/{id}")
def update_post(id: int, post:Post):
    cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, 
                   (post.title, post.content, post.published, str(id),))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail= f"post with {id} does not exist")
    return{"data" : updated_post}
