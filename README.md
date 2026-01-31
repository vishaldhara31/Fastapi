# 🚀 FastAPI Learning Repository

This repository documents my step-by-step learning journey with **FastAPI**, focused on building a strong backend foundation using modern Python tools and best practices.

It includes hands-on experiments, clean code structure, database integration, and continuous progress tracking through regular commits.

---

## 🎯 Goals of This Repository

- Track my FastAPI learning journey 📈  
- Build a strong backend foundation  
- Learn industry-standard practices (ORM, dependency injection, APIs)  
- Maintain consistency through meaningful commits  
- Gradually evolve this into production-ready APIs  

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **FastAPI**
- **Uvicorn**
- **PostgreSQL**
- **SQLAlchemy (ORM)**
- **psycopg2**
- **Postman / Swagger UI**

---

## 📂 Project Structure

Fastapi/
│

├── app/

│ ├── init.py # Marks app as a Python package

│ ├── main.py # FastAPI app entry point

│ ├── database.py # Database connection & session management

│ ├── models.py # SQLAlchemy ORM models

├── venv/ # Virtual environment (not tracked)

├── .gitignore

├── README.md




## 🧪 Step 1: Virtual Environment Setup

- Create a virtual environment:

   py -3 -m venv venv

- Activate it:

   venv\Scripts\activate
 
You should see (venv) in the terminal after activation.

## 📦 Step 2: Install Dependencies

pip install fastapi sqlalchemy psycopg2-binary uvicorn

This installs:

- FastAPI framework

- SQLAlchemy ORM

- PostgreSQL adapter

- Uvicorn ASGI server

## 🚀 Step 3: Running the Application
- Start the development server:

- uvicorn app.main:app --reload
  Open in browser:

- Swagger UI: http://127.0.0.1:8000/docs

- ReDoc: http://127.0.0.1:8000/redoc

## 🔍 Step 4: Routing & HTTP Methods
- Learned how FastAPI uses decorators to define routes and HTTP methods.

- Implemented:
  GET / – Root endpoint

- GET /post – Fetch data

- POST /createpost – Send data via request body

## Key Learnings:
- FastAPI automatically converts Python dictionaries to JSON

- Browsers can only send GET requests

- POST requests are tested using Swagger UI or Postman

- Request body data is automatically validated and parsed

## 🗄️ Step 5: Database Integration (SQLAlchemy)
- Integrated PostgreSQL with FastAPI using SQLAlchemy ORM.

## Implemented:
- SQLAlchemy engine configuration

- SessionLocal for database sessions

- ORM models using declarative_base

- Automatic table creation with Base.metadata.create_all()

## Concepts Learned:
- Difference between raw SQL and ORM

- Role of engine, SessionLocal, and Base

- Benefits of ORM abstraction

## 🔁 Step 6: Dependency Injection
- Implemented FastAPI dependency injection for database session handling.

- Implemented:
  get_db() dependency using yield

- Automatic DB session open & close per request

- Benefits:
  Cleaner code

- Better resource management

- No database connection leaks

## 🧠 Key Takeaways So Far
- FastAPI is fast, clean, and developer-friendly

- Decorators define routes and HTTP methods

- Dependency injection simplifies resource management

- SQLAlchemy ORM improves maintainability

- Swagger UI makes API testing easy

## ✅ Features Implemented
- FastAPI project setup

- Virtual environment configuration

- API routing (GET, POST)

- Request body handling

- Swagger UI & API testing

- PostgreSQL integration

- SQLAlchemy ORM models

- Dependency injection for DB sessions

## 🛣️ Roadmap (Next Steps)
- Planned improvements and learning goals:

- Full CRUD operations

- Pydantic schemas

-  Response models

-  Exception handling

-  JWT authentication

-  Environment variables (.env)

-  Alembic migrations

-  Deployment (Render / Railway / Docker)

## 🧠 Learning Philosophy
- I believe in learning by:

- Writing code daily

- Debugging deeply instead of skipping errors

- Maintaining clean commits

- Building real-world backend logic step by step
