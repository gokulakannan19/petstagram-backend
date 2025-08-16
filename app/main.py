from fastapi import FastAPI
from .database import Base, engine
from .routers import users


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Petstagram", version="1.0.0")

app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Welcome to Petstagram!"}
