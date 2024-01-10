'''
pip install flask
pip install json
pip instal requests

'''

#####################################################################################################

from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, abort
import json
import random

#####################################################################################################

with open('config.json', 'r') as config:
    config = json.load(config)
    ip = config['IP']
    port = config['Port']
    debug = config['Debug']

#####################################################################################################

ecolabs = {

        "ecolab_2": {
            'Cellule_1': {
                "name": "E2C1",
                "fins": {
                    "ip": "192.168.0.21",
                    "port": 9600,
                    "dst_net_addr": 2,
                    "dst_node_num": 2,
                    "dst_unit_addr": 0
                },
                "params": {
                    "temperature_reprise": 12,
                    "temperature_eau_pluie": 14,
                    "temperature_consigne": 0
                }
            },
            'Cellule_2':{
                    "name": "E2C2",
                    "fins": {
                        "ip": "192.168.0.2",
                        "port": 9600,
                        "dst_net_addr": 1,
                        "dst_node_num": 1,
                        "dst_unit_addr": 0
                    },
                    "params": {
                        "temperature_reprise": 20,
                        "temperature_eau_pluie":22,
                        "temperature_consigne": 5
                    }
            },
            'Cellule_3':{
                    "name": "E2C3",
                    "fins": {
                        "ip": "192.168.0.3",
                        "port": 9600,
                        "dst_net_addr": 1,
                        "dst_node_num": 1,
                        "dst_unit_addr": 0
                    },
                    "params": {
                        "temperature_reprise": 2,
                        "temperature_eau_pluie":4,
                        "temperature_consigne":0
                    }
            }
        }

    }

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return ecolabs

if __name__ == "__main__":
    app.run(host=ip, port=port, debug=debug)