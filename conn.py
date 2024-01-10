from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus
from sqlalchemy.orm import sessionmaker

'''
-pip install sqlalchemy
 -pip install pymysql

'''

utilisateur = "Deva"
password = "sio"
base_de_donne = "octopus"
port = 3306
encoded_password = quote_plus(password)
DB_URL = create_engine(f'mysql+pymysql://{utilisateur}:{encoded_password}@localhost:{port}/{base_de_donne}')

Session = sessionmaker(bind=DB_URL)
session = Session()
Base = declarative_base()

