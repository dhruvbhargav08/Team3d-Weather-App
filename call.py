import requests
api_key = "30d4741c779ba94c470ca1f63045390a"
def calling(City):
    city = City
    city_response = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}")
    lat = city_response.json()[0]["lat"]
    lon = city_response.json()[0]["lon"]
    response=requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude"
            f"=minutely,hourly,alerts%units=metric&appid={api_key}")
    return response 