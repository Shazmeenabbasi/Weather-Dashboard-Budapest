from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
API_KEY = "fec734c51bd96203d583749fb62d52e6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def home():
    return jsonify({"message": "Backend is running!"})

@app.route('/weather/budapest')
def weather_budapest():
    city = "Budapest"
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  # Units in Celsius
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"]
        })
    else:
        return jsonify({"error": "Unable to fetch weather data"}), response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
