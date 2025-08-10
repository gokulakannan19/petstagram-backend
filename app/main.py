from fastapi import FastAPI
from .database import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Petstagram", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Welcome to Petstagram!"}
