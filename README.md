# FastAPI Learning Repository 🚀

This repository contains everything I am learning about **FastAPI**, including setup, core concepts, examples, and small experiments as I progress.

### 🎯 Goals of this repository
- Track my learning journey 📈  
- Build a strong backend foundation using FastAPI  
- Maintain consistency through regular commits  

---

## 🛠️ Step 1: Initialize a Virtual Environment

 - Open **Command Prompt** in your project directory and run:

   py -3 -m venv venv

This will create a virtual environment named venv.
 
 - Activate the virtual environment:

   venv\Scripts\activate.bat

After activation, you should see (venv) in your terminal.

## 📦 Step 2: Install FastAPI
Install FastAPI along with all optional dependencies (as used in the tutorial):

pip install fastapi[all]

This installs:
 - FastAPI core framework
 
 - Uvicorn ASGI server

 - Optional tools such as:

 - HTML templates

 - File uploads

 - WebSockets

 - Validation & utility packages

## 🚀 Step 3: Create a Basic FastAPI App
Next steps in this repository will include:

 - Creating a basic FastAPI application

 - Running the server using Uvicorn

 - Exploring

 - Routing

 - Request & response models

 - Dependencies

## 🔍 Step 4: Understanding Routing & HTTP Methods

Today I learned how FastAPI uses decorators to define API routes and handle different HTTP methods.

## Implemented:

- A basic GET route for the root endpoint (/)

- A GET route with a custom path (/post)

- A POST route (/createpost) to accept data from the request body

## Learned that:

- FastAPI converts Python dictionaries into JSON responses automatically

- Browsers can only send GET requests

- POST requests must be tested using Swagger UI or Postman

- Data sent in the request body is automatically parsed and stored as a Python dictionary

## 🧪 Step 5: Testing APIs

- Tested all endpoints using Swagger UI (/docs) or Postman (I am using Postman).

- Use the Postman:

- Send GET requests

- Send POST requests with JSON body

- Verify responses and status codes

## 🧠 Key Takeaways

- Decorators like @app.get() and @app.post() define routes and HTTP methods

- GET is used to retrieve data

- POST is used to send data to the server

- FastAPI automatically handles request validation and JSON serialization

## 📈 Progress Update

Continuing to build APIs step by step and improving understanding of backend fundamentals.
