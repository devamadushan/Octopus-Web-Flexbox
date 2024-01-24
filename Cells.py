'''
Flask  SQLALchemy : pip install Flask-SQLAlchemy
SQLALchemy : pip install SQLAlchemy
'''
##############################################################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,ForeignKey
from flask import Flask
from Connexion import Base , DB_URL
from Experiment import Experiment
from EcolabWeb import EcolabWeb

##############################################################################################

db = SQLAlchemy()

class Cells(Base):
    __tablename__= 'cells'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable=False)
    Experiment_id = Column(Integer, ForeignKey('experiment.id'))
    ecolabWeb_id = Column(Integer,ForeignKey('ecolabWeb.id'))
    #Experiment = relationship('Experiment', back_populates='cellules')

    


Base.metadata.create_all(DB_URL)