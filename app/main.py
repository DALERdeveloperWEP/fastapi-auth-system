from fastapi import FastAPI
from app.db import engine
from app.db import Base
from app.models import users, authtoken
# from app.models.users import users
# from app.models.authtoken import authtoken


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
app = FastAPI(title='Auth System Api')