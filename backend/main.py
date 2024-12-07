from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import requests
import os

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/', methods=['GET'] )
@cross_origin(supports_credentials=True)
def home ():
    return {"message" :"Hello"}

@app.route('/weather', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_weather():
    api_key = os.getenv('WEATHER_API_KE', 'fec734c51bd96203d583749fb62d52e6')
    city = "Budapest"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return jsonify({
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
            })
        else:
            return jsonify({"error": "Unable to fetch weather data"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
