#adding new president information -> update presidents.py and schemas.py
#starting uvicorn: "uvicorn main:app --reload"
#restarting uvicorn - "ps aux | grep uvicorn" and "kill <bottom number>"


from fastapi import FastAPI
from routes.route import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(router)

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

