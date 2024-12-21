import requests

API_KEY = "your_api_key_here"  # 替换为您的 OpenWeatherMap API 密钥
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    获取指定城市的天气信息
    :param city: str，城市名称
    :return: str，天气描述和温度
    """
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "kr"  # 返回韩语描述
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"{city}의 날씨: {weather_desc}, 온도: {temperature}°C"
    except requests.exceptions.RequestException as e:
        return f"날씨 정보를 가져올 수 없습니다: {e}"
