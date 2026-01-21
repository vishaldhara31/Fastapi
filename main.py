from fastapi import FASTAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FASTAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/post') 
#here the @ is used as we initialise the decorator and we use different https method and in the write the different urls like here example /post
async def post(): #this is just a simple function
     return{"message" : "This is the request send to post"} #return a dictionary


# #the below is the post method , and we can test this url from different software, i am using the postman
# @app.post("/createpost")
# def create_posts(payload: dict = Body(...)): #what this do is take the content from the body and convert that content into the dictionary and store in payload
#     print(payload)
#     return{"message": "This post created successfully"}


# the above is the same function which is commented but this is directly checking the schemas using the pydantic module and checking the data properly
@app.post("/createpost")
def create_posts(new_post:Post): #what this do is take the content from the body and convert that content into the dictionary and store in payload
    print(new_post)
    print(new_post.title)
    print(new_post.content)
    print(new_post.published)
    return{"data": "new_posts"}




