from flask import Flask, render_template, request
from funcs import check_bad_weather, validate_coordinates, validate_city_name, get_weather_by_coordinates, get_weather_by_city
from API import api_key

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('selection_form.html')

@app.route('/weather_choice', methods=['POST'])
def weather_choice():
    choice = request.form['choice']
    if choice == 'coordinates':
        return render_template('coordinates_form.html')
    elif choice == 'cities':
        return render_template('city_form.html')

@app.route('/weather_by_coordinates', methods=['POST'])
def weather_by_coordinates():
    lat1 = request.form['lat1']
    lon1 = request.form['lon1']
    lat2 = request.form['lat2']
    lon2 = request.form['lon2']

    is_valid1, error_message1 = validate_coordinates(lat1, lon1)
    is_valid2, error_message2 = validate_coordinates(lat2, lon2)

    if not is_valid1:
        return render_template('error.html', message=f"Ошибка для точки 1: {error_message1}")
    if not is_valid2:
        return render_template('error.html', message=f"Ошибка для точки 2: {error_message2}")

    weather_point1 = get_weather_by_coordinates(lat1, lon1)
    weather_point2 = get_weather_by_coordinates(lat2, lon2)

    if "error" in weather_point1 or "error" in weather_point2:
        error_message = weather_point1.get("error") or weather_point2.get("error")
        return render_template('error.html', message=error_message)

    bad_weather_point1 = check_bad_weather(weather_point1)
    bad_weather_point2 = check_bad_weather(weather_point2)

    return render_template('weather_result_two_points.html',
                            point1=weather_point1, result1=bad_weather_point1,
                            point2=weather_point2, result2=bad_weather_point2)

@app.route('/weather_by_cities', methods=['POST'])
def weather_by_cities():
    city1 = request.form['city1']
    city2 = request.form['city2']

    is_valid1, error_message1 = validate_city_name(city1)
    is_valid2, error_message2 = validate_city_name(city2)

    if not is_valid1:
        return render_template('error.html', message=f"Ошибка для города 1: {error_message1}")
    if not is_valid2:
        return render_template('error.html', message=f"Ошибка для города 2: {error_message2}")

    weather_city1 = get_weather_by_city(city1)
    weather_city2 = get_weather_by_city(city2)

    if "error" in weather_city1 or "error" in weather_city2:
        error_message = weather_city1.get("error") or weather_city2.get("error")
        return render_template('error.html', message=error_message)

    bad_weather_city1 = check_bad_weather(weather_city1)
    bad_weather_city2 = check_bad_weather(weather_city2)

    return render_template('weather_result_two_points.html',
                            point1=weather_city1, result1=bad_weather_city1,
                            point2=weather_city2, result2=bad_weather_city2)


if __name__ == '__main__':
    app.run(debug=True)
