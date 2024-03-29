'''

Flask  SQLALchemy : pip install Flask-SQLAlchemy
SQLALchemy : pip install SQLAlchemy
pip install Flask-Bcrypt

'''
##############################################################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from flask import Flask
from Connexion import Base, DB_URL, session,Session
from flask_bcrypt import Bcrypt,generate_password_hash,check_password_hash

##############################################################################################

# Auteur: Luca

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50),nullable=False)
    userpassword = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, default='utilisateur')

    bcrypt = Bcrypt()

    # Hash the created password
    def set_password(self, password):
        self.userpassword = self.bcrypt.generate_password_hash(password).decode('utf-8')

    # Compare hash password with raw password
    def check_password(self, password):
        return self.bcrypt.check_password_hash(self.userpassword, password)

Base.metadata.create_all(DB_URL)


# For create user
# adminuser = Utilisateur(username='',role='')
# adminuser.set_password('')

# UtilisateurAdmin

# add user
# session.add(adminuser)
# session.commit()
