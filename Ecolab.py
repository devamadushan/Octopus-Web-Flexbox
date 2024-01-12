'''
pip install Flask-SQLAlchemy

'''
##############################################################################################


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from flask import Flask
from conn import Base, DB_URL



##############################################################################################

db = SQLAlchemy()

class Ecolab(Base):
    __tablename__ = 'ecolab'

    id = Column(Integer, primary_key=True)
    nom = Column(String(255),nullable=False)

    # Relation ONE TO MANY
    cellules = relationship('Cellule',backref='ecolab')
    
Base.metadata.create_all(DB_URL)