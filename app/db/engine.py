from app.core.config import Settigs
from sqlalchemy import URL, create_engine


settings = Settigs()
url = URL.create(
    drivername='postgresql+psycopg2',
    username=settings.DB_USER,
    password=settings.DB_PASS,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME
)

engine = create_engine(url=url)