from flask import Blueprint, jsonify, request

from data_analysis.meat_consumption import get_country_stat


data_analysis_page = Blueprint('data_analysis_page', __name__, template_folder='templates')


# sample : http://127.0.0.1:5000/analysis/meat_consumption_time?country=NZL&start=1991&end=1995

@data_analysis_page.route('/analysis/meat_consumption_time', methods=['GET'])
def meat_consumption_pie():
    args = request.args

    country_name = args.get('country')
    time_start = int(args.get('start'))
    time_end = int(args.get('end'))

    result = get_country_stat(country_name, time_start, time_end)

    return jsonify(result)
