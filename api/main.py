from api_v1.endpoints import auth
from fastapi import FastAPI
from api_v1 import todos
from database import engine

app = FastAPI()

# Include API routes
app.include_router(todos.router, prefix="/todos", tags=["todos"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
