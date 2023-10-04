
from flask import Flask, jsonify, request
from flask_cors import CORS

from data_analysis_meat_consumption_page import data_analysis_meat_consumption_page
from data_analysis_war_effect_bd import data_analysis_war_effect_bd_page

import sys
sys.executable

app = Flask(__name__)
app.register_blueprint(data_analysis_meat_consumption_page)
app.register_blueprint(data_analysis_war_effect_bd_page)
CORS(app, origins="*")


@app.route('/')
def home_page():
    str = '''

    <br><br> <b> SFC Model Flask </b> <br><br>

    <br><br>

    '''

    return str