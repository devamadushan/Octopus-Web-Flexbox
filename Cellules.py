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



class Cellule(Base):
    __tablename__= 'cellules'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    ##experience = Column(String(50), ForeignKey('experience.nom')) 
    ##experience = Column(String, ForeignKey('experience.nom'))
    experience_id = Column(Integer, ForeignKey('experience.id')) 


Base.metadata.create_all(DB_URL)





def init_app(app):
    db.init_app(app)