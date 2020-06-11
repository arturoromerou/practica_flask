# con este archivo importamos todo del archivo .env para por ejemplo crear la conexion a la db
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)