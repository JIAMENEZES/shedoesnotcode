import jwt
import sqlalchemy as sa
from jwt import encode as jwt_encode
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from bson import ObjectId

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Connection here
# engine = sa.create_engine("postgres://postgres:postgres@localhost:5442/pdb")
# connection = engine.connect()

SECRET_KEY = "asldfjaoiw4tuasjlkau8tu4wojfau8ufalset78woejfo"
security = HTTPBearer()

@app.get("/")
def homepage():
    return {"message": "Welcome to the internet"}

@app.post("/login")
def login(user: User):
    pass