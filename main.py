from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    email: str
    password: str


# Home
@app.get("/")
def home():
    return {"message": "iGOT Karmayogi backend is running successfully!"}


# Test
@app.get("/hello")
def hello():
    return {"message": "Karmayogi backend is running successfully!"}


# LOGIN API
@app.post("/login")
def login(data: LoginData):

    # Demo login
    if data.email == "admin@gmail.com" and data.password == "1234":
        return {
            "success": True,
            "message": "Login successful!",
            "email": data.email
        }

    return {
        "success": False,
        "message": "Incorrect email or password"
    }


# Serve frontend
app.mount("/", StaticFiles(directory=".", html=True), name="frontend")
