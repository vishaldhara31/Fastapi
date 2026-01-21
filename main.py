from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating: Optional[int] = None

my_posts = [{"title" : "title of the first post", "content":"Content of the first post", "id": 1}  
            ,{"title": "Library", "content":"This library content all types of book", "id" : 2}]

@app.get("/") #decorator
async def root(): #this is just a simple function and async for long duration task
    return {"message": "My world of api"}


@app.get("/posts")
def get_posts():
    return{"data" : my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data" : post_dict} 

@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"Post_Details" : f"Your Post Details {id}"}
