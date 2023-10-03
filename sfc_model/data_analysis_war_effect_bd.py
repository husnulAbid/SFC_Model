from flask import Blueprint, jsonify, request
from data_analysis.war_effect_on_bd import get_query_data

data_analysis_war_effect_bd_page = Blueprint('data_analysis_war_effect_bd_page', __name__, template_folder='templates')

# sample : {base_url}/analysis/war_effect_data?metric_name=GDP&year_duration=15
@data_analysis_war_effect_bd_page.route('/analysis/war_effect_data', methods=['GET'])
def meat_consumption_pie():
    args = request.args

    metric_name = args.get('metric_name')
    year_duration = int(args.get('year_duration'))
     
    result = get_query_data(metric_name, year_duration)

    return jsonify(result)
