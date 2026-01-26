from fastapi import FastAPI, Response , status , HTTPException
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
    return{"data" : my_posts}



#creating the post
#here we change the http response using status code
@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data" : post_dict} 
#this is a dictonary and it convertes to a json file later


# to run the server use fastapi dev main.py
# use uvicorn main:app

# @app.post("/createpost")
# def create_posts(payload: dict = Body(...)): #what this do is take the content from the body and convert that content into the dictionary and store in payload
#     print(payload)
#     return{"new_post": f"title : {payload['title']} content : {payload['content']}"}

# @app.post("/createpost")
# def create_post(new_post : Post): #here we are using our model to check properly if we get title and content from the user instead of collecting an whole bunch of non sense data
#     print(new_post)
#     print(new_post.title)
#     print(new_post.content)
#     print(new_post.published)
#     print(new_post.rating)
#     # print(new_post.dict())
#     print(new_post.model_dump()) # this is use in the latest pydantic model the above one is used become outdated
#     return{"data":"new_posts"}

#getting one individual post
@app.get("/posts/{id}") #here the {id} is the path parameter
def get_post(id : int):
    post = find_post(id)#the path function return the id in string so to work we should convert that parameter in int
    if not post:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail = f"post with{id}: was not found")
    return {"Post_Details" :  post}


@app.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"post with{id} does not exist")


    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# We return 204 No Content for DELETE requests
# to indicate successful deletion without sending any response data.


@app.put("/posts/{id}")
def get_post(id: int, post:Post):

    
    index = find_index_post(id)

    if index == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail= f"post with{id} does not exist")
    
    post_dict = post.model_dump() #here the data we get from the post which is written in the function and converted into regular python dictionary
    post_dict["id"] = id  #this line add the id in each post dictionary , this id does not send by the user it is copy from the path url 
    my_posts[index] = post_dict #this line replace the context in the particular index of my_post. It get replaced with the content of present in post_dict

    return{"data" : post_dict}

