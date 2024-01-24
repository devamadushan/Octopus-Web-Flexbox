'''
Flask  SQLALchemy : pip install Flask-SQLAlchemy
SQLALchemy : pip install SQLAlchemy
'''

##################################################################################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,DATE, ForeignKey,DateTime,Enum
from Cells import Cells
from Experiment import Experiment
from datetime import datetime
from Connexion import Base, DB_URL

##################################################################################################################

# Auteur: Deva

class Historiy_cells(Base):
    __tablename__ = 'history_cells'

    id =  Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    cells_id= Column(Integer, ForeignKey('cells.id'))
    cells_experiment_id = Column(Integer, ForeignKey('experiment.id'))
    status = Column(String(255), nullable=False)
    action = Column(String(255), nullable=False)
    

Base.metadata.create_all(DB_URL)