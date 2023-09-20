
from flask import Flask, jsonify, request
from meat_consumption import meat_consumption_page

app = Flask(__name__)
app.register_blueprint(meat_consumption_page)


@app.route('/')
def home_page():
    str = '''
    
    <br><br> <b> SFC Model Flask </b> <br><br>
    
    <br><br>

    '''

    return str
