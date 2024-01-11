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


class Experience(Base):
    __tablename__ = 'experience'

    id = Column(Integer, primary_key=True)
    date_debut = Column(DATE, nullable=False)
    date_fin = Column(DATE)
    nom = Column(String(255), nullable=False)


    # Relation ONE TO MANY
    ##cellule = Column(String(50), ForeignKey('cellule.nom')) 
    ##cellules = relationship('cellule', backref='experience')
    cellules = relationship('Cellule', backref='experience') 
    cellule_id = 
    

Base.metadata.create_all(DB_URL)


