import os
from dotenv import load_dotenv

load_dotenv()

# setting for DB
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASS = os.environ.get("POSTGRES_PASSWORD")

# setting for test db
DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
