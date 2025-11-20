from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AuthRequest(BaseModel):
    user: str
    password: str

@app.post("/login")
def login(data: AuthRequest):
    if data.user == "admin" and data.password == "123":
        return {"token": "fake-jwt-token"}
    return {"error": "invalid credentials"}
