from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from conn import utilisateur,session, password, base_de_donne, port, Base

from Experiences import Experience
from Cellules import Cellule



nova = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Nova")
alfa = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Alfa")
pactol = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Pactrol")
red = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Red")
green = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Green")
black = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Black")
rose = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Rose")
yellow = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Yellow")
grey = Experience(date_debut='2024/01/15', date_fin='2024/02/13', nom="Grey")



E1C1 = Cellule(nom="E1C1", experience_id=1)
E1C2 = Cellule(nom="E1C2", experience_id=4)
E1C3 =Cellule(nom="E1C3", experience_id=8)

E2C1 = Cellule(nom="E2C1", experience_id=4)
E2C2 = Cellule(nom="E2C2", experience_id=7)
E2C3 =Cellule(nom="E2C3", experience_id=2)

E3C1 = Cellule(nom="E3C1", experience_id=6)
E3C2 = Cellule(nom="E3C2", experience_id=6)
E3C3 =Cellule(nom="E3C3", experience_id=6)

E4C1 = Cellule(nom="E4C1", experience_id=6)
E4C2 = Cellule(nom="E4C2", experience_id=6)
E4C3 = Cellule(nom="E4C3", experience_id=6)

E5C1 = Cellule(nom="E5C1", experience_id=6)
E5C2 = Cellule(nom="E5C2", experience_id=6)
E5C3 = Cellule(nom="E5C3", experience_id=6)

E6C1 = Cellule(nom="E6C1", experience_id=6)
E6C2 = Cellule(nom="E6C2", experience_id=6)
E6C3 = Cellule(nom="E6C3", experience_id=6)



session.add_all([E1C1,E1C2,E1C3,E2C1,E2C2,E2C3,E3C1,E3C2,E3C3,E4C1,E4C2,E4C3,E5C1,E5C2,E5C3,E6C1,E6C2,E6C3,nova,alfa,pactol,red,green,black,rose,yellow,grey])




session.commit()



    

