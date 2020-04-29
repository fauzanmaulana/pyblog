import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(""))

load_dotenv(os.path.join(BASEDIR, '.env'))

conn = os.getenv("CONNECT")
db = os.getenv("DATABASE")