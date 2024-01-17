'''
Flask  SQLALchemy : pip install Flask-SQLAlchemy
SQLALchemy : pip install SQLAlchemy
'''

##################################################################################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,DATE, ForeignKey,DateTime,Enum
from Cellules import Cellule
from Experiences import Experience
from datetime import datetime
from conn import Base, DB_URL

##################################################################################################################


class HistoriqueCellule(Base):
    __tablename__ = 'historique_cellule'

    id =  Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    cellule_id= Column(Integer, ForeignKey('cellules.id'))
    cellule_experience_id = Column(Integer, ForeignKey('experience.id'))
    status = Column(String(255), nullable=False)
    action = Column(String(255), nullable=False)
    

Base.metadata.create_all(DB_URL)