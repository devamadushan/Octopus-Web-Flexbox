

##################################################################################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,DATE, ForeignKey,DateTime,Enum
from sqlalchemy.orm import relationship
from flask import Flask

from datetime import datetime
from conn import Base, DB_URL
##################################################################################################################


class Historique(Base):
    __tablename__ = 'historique'

    id =  Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    action = Column(String(255), nullable=False)
    object_id = Column(Integer, nullable=False)
    object_name = Column(String(255), nullable=False)
    details = Column(String(255))

Base.metadata.create_all(DB_URL)