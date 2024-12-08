import requests
from разработка_логики import check_bad_weather
from API import api_key

def get_weather_by_location(lat, lon):
    location_url = f'https://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={api_key}&q={lat},{lon}'
    location_response = requests.get(location_url)
    location_data = location_response.json()
    location_key = location_data['Key']

    weather_url = f'https://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}&details=true'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    weather_information = {
        "Время наблюдения": weather_data[0]['LocalObservationDateTime'],
        "Температура (°C)": weather_data[0]['Temperature']['Metric']['Value'],
        "Ощущается как (°C)": weather_data[0]['RealFeelTemperature']['Metric']['Value'],
        "Влажность (%)": weather_data[0]['RelativeHumidity'],
        "Скорость ветра (км/ч)": weather_data[0]['Wind']['Speed']['Metric']['Value'],
        "Направление ветра": weather_data[0]['Wind']['Direction']['Localized'],
        "Видимость (км)": weather_data[0]['Visibility']['Metric']['Value'],
        "Давление (мбар)": weather_data[0]['Pressure']['Metric']['Value'],
        "Осадки (мм)": weather_data[0]['PrecipitationSummary']['Precipitation']['Metric']['Value']
    }

    return weather_information


def get_weather_by_city(city_name):
    location_url = f'https://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city_name}'
    location_response = requests.get(location_url)
    location_data = location_response.json()
    location_key = location_data[0]['Key']

    weather_url = f'https://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}&details=true'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    weather_information = {
        "Время наблюдения": weather_data[0]['LocalObservationDateTime'],
        "Температура (°C)": weather_data[0]['Temperature']['Metric']['Value'],
        "Ощущается как (°C)": weather_data[0]['RealFeelTemperature']['Metric']['Value'],
        "Влажность (%)": weather_data[0]['RelativeHumidity'],
        "Скорость ветра (км/ч)": weather_data[0]['Wind']['Speed']['Metric']['Value'],
        "Направление ветра": weather_data[0]['Wind']['Direction']['Localized'],
        "Видимость (км)": weather_data[0]['Visibility']['Metric']['Value'],
        "Давление (мбар)": weather_data[0]['Pressure']['Metric']['Value'],
        "Осадки (мм)": weather_data[0]['PrecipitationSummary']['Precipitation']['Metric']['Value']
    }

    return weather_information


print(get_weather_by_location(10, 10))
print(check_bad_weather(get_weather_by_location(10, 10)))
print(get_weather_by_city('Moscow'))
print(check_bad_weather(get_weather_by_city('Moscow')))