def check_bad_weather(weather_data):
    temperature = weather_data["Температура (°C)"]
    wind_speed = weather_data["Скорость ветра (км/ч)"]
    precipitation_probability = weather_data["Осадки (мм)"]
    humidity = weather_data["Влажность (%)"]
    pressure = weather_data["Давление (мбар)"]

    if temperature < 0 or temperature > 35: return "Неблагоприятные условия"
    if wind_speed > 50: return "Неблагоприятные условия"
    if precipitation_probability > 70: return "Неблагоприятные условия"
    if humidity and humidity > 85 and temperature > 30: return "Неблагоприятные условия"
    if pressure < 980 or pressure > 1030: return "Неблагоприятные условия"
    if wind_speed > 30 and temperature < 5: return "Неблагоприятные условия"
    if precipitation_probability > 50 and wind_speed > 30: return "Неблагоприятные условия"
    return "Благоприятные условия"