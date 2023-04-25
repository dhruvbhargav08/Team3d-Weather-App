def temp(_current):
    temperature = round(_current.json()["current"]["temp"] - 273, 2)
    weather = _current.json()["current"]["weather"][0]["main"]
    wind_speed = _current.json()["current"]["wind_speed"]
    humidity = _current.json()["current"]["humidity"]
    feels_like = round(_current.json()["current"]["feels_like"] - 273, 2)
    return [temperature, weather, wind_speed, humidity, feels_like]