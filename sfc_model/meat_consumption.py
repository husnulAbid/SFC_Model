from flask import Blueprint, jsonify


meat_consumption_page = Blueprint('meat_consumption_page', __name__, template_folder='templates')


@meat_consumption_page.route('/analysis/meat_consumption_pie', methods=['GET'])
def meat_consumption_pie():
    result = { 'popularity': '70%', 'avg consumption': '1.3 kg'}

    return jsonify(result)
