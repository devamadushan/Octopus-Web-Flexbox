

##################################################################################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,DATE, ForeignKey,DateTime,Enum
from sqlalchemy.orm import relationship
from flask import Flask
from Cellules import Cellule
from Experiences import Experience
from datetime import datetime
from conn import Base, DB_URL
##################################################################################################################


class HistoriqueCellule(Base):
    __tablename__ = 'historique_cellule'

    id =  Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    # id_Experience = Column(Integer, nullable=False)
    # experience_nom =  Column(String(255))
    # experience_debut = Column(DATE)
    # experience_fin = Column(DATE)
    # experience_status = Column(String(255))

    cellule_id= Column(Integer, ForeignKey('cellules.id'))
    cellule_experience_id = Column(Integer, ForeignKey('experience.id'))
    status = Column(String(255), nullable=False)
    action = Column(String(255), nullable=False)
    

Base.metadata.create_all(DB_URL)