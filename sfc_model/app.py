
from flask import Flask, jsonify, request
from data_analysis_page import data_analysis_page

app = Flask(__name__)
app.register_blueprint(data_analysis_page)


@app.route('/')
def home_page():
    str = '''
    
    <br><br> <b> SFC Model Flask </b> <br><br>
    
    <br><br>

    '''

    return str
