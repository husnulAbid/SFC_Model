from flask import Blueprint, jsonify


data_analysis_page = Blueprint('data_analysis_page', __name__, template_folder='templates')


@data_analysis_page.route('/analysis/meat_consumption_pie', methods=['GET'])
def meat_consumption_pie():
    

    result = { 'popularity': '70%', 'avg consumption': '1.3 kg'}

    return jsonify(result)
