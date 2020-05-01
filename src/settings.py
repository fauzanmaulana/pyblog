import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(""))

load_dotenv(os.path.join(BASEDIR, '.env'))

secret_keys = os.urandom(16)
conn = os.getenv("CONNECT")
db = os.getenv("DATABASE")