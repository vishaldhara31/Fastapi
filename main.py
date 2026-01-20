from fastapi import FASTAPI

app = FASTAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/post') 
#here the @ is used as we initialise the decorator and we use different https method and in the write the different urls like here example /post
async def post(): #this is just a simple function
     return{"message" : "This is the request send to post"} #return a dictionary


#the below is the post method , and we can test this url from different software, i am using the postman
@app.post("/createpost")
def create_posts(payload: dict = Body(...)): #what this do is take the content from the body and convert that content into the dictionary and store in payload
    print(payload)
    return{"message": "This post created successfully"}
