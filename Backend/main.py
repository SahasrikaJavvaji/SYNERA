from fastapi import FastAPI
from models.user import User

app = FastAPI()

@app.get("/")
def home():
    return {"message": "SYNERA Backend is running"}