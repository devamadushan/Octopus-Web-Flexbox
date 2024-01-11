'''
pip install Flask-SQLAlchemy

'''
##############################################################################################


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,DATE, ForeignKey
from flask import Flask
from sqlalchemy.orm import relationship
from conn import Base , DB_URL



##############################################################################################

db = SQLAlchemy()



class Cellule(Base):
    __tablename__= 'cellules'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    experience_id = Column(Integer, ForeignKey('experience.id'))

    #experience = relationship('Experience', back_populates='cellules')

    


Base.metadata.create_all(DB_URL)