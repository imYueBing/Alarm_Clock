import requests

DEFAULT_CITY = "Seoul"
API_KEY = "1267b1d7a73e19a8bf0404c280eb8085"

def get_weather(city=DEFAULT_CITY):
    """
    获取天气信息
    :param city: str，城市名称
    :return: str，天气信息
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            return f"날씨: {weather}\n온도: {temp}°C\n습도: {humidity}%\n바람 속도: {wind_speed} m/s"
        else:
            return f"오류: {data.get('message', '날씨 정보를 가져올 수 없습니다.')}"
    except Exception as e:
        return f"오류 발생: {e}"
