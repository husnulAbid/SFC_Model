from flask import Blueprint, jsonify, request

from data_analysis.meat_consumption import get_country_stat_on_all_type_consumption, get_countries, get_available_years


data_analysis_page = Blueprint('data_analysis_page', __name__, template_folder='templates')


# sample : {base_url}/analysis/meat_consumption_time?country=NZL&start=1991&end=1995
@data_analysis_page.route('/analysis/meat_consumption_time', methods=['GET'])
def meat_consumption_pie():
    args = request.args

    country_name = args.get('country')
    time_start = int(args.get('start'))
    time_end = int(args.get('end'))

    result = get_country_stat_on_all_type_consumption(country_name, time_start, time_end)

    return jsonify(result)


# sample : {base_url}/analysis/meat_consumption_time/countries
@data_analysis_page.route('/analysis/meat_consumption_time/countries', methods=['GET'])
def meat_consumption_available_countries():
    available_countries = get_countries()

    return jsonify(available_countries)


# sample : {base_url}/analysis/meat_consumption_time/start_and_end_year
@data_analysis_page.route('/analysis/meat_consumption_time/start_and_end_year', methods=['GET'])
def meat_consumption_pie_start_and_end_year():
    available_years = get_available_years()

    return jsonify(available_years)