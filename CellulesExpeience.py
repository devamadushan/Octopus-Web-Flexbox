'''
pip install Flask-SQLAlchemy

'''
##############################################################################################


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,DATE, ForeignKey
from flask import Flask
from sqlalchemy.orm import relationship
from conn import Base , DB_URL
from Experiences import Experiences


##############################################################################################

db = SQLAlchemy()

class CelluleExperience(Base):
    __tablename__ = 'CelluleExperience'
    id = Column(Integer, primary_key=True)
    cellule_id = Column('cellule_id', Integer, ForeignKey('cellule.id'))
    experience_id = Column('experience_id', Integer, ForeignKey('experience.id'))
    ## relation Many to Many 
    cellules = relationship('Cellule', back_populates='experience')