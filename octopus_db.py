from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from conn import utilisateur, password, base_de_donne, port, Base

from Experiences import Experiences
from Cellules import Cellule


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{utilisateur}:{password}@localhost:{port}/{base_de_donne}'
db = SQLAlchemy()

def init_app(app):
    db.init_app(app)




if __name__ == "__main__":
    app.run(host="",port=8000, debug=True)
