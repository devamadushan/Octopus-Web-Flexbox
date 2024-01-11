from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from conn import utilisateur,session, password, base_de_donne, port, Base

from Experiences import Experience
from Cellules import Cellule



nova = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Nova")
alfa = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Alfa")


EC21 = Cellule(nom="E2C1", experience_id=1)


session.add(nova)
session.add(EC21)
session.add(alfa)
session.commit()



    

