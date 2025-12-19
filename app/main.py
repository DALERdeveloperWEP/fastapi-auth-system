from fastapi import FastAPI
from app.db import engine
from app.db import Base
from app.models import users, authtoken
from app.routers import users, auth 

app = FastAPI(title='Auth System Api')
app.include_router(users.router)
app.include_router(auth.router)




Base.metadata.create_all(engine)