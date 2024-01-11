

##################################################################################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,DATE, ForeignKey,DateTime,Enum
from sqlalchemy.orm import relationship
from flask import Flask
from conn import Base, DB_URL
from datetime import datetime

##################################################################################################################


class Historique(Base):
    __tablename__ = 'historique'

    id =  Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    action = Column(Enum('ajout', 'modification', 'suppression'), nullable=False)
    object_id = Column(Integer, nullable=False)
    table_name = Column(String(255), nullable=False)
    details = Column(String(255))

Base.metadata.create_all(DB_URL)