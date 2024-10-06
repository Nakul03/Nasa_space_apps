from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

app = Flask(__name__)

# Load the Excel data into a DataFrame
df = pd.read_excel('CH4-CO2_Benchmark_Metadata.xlsx')


def alert(latitude, longitude, df):
    """Function to check for proximity to gas plumes."""
    proximity_threshold = 0.1
    for index, row in df.iterrows():
        try:
            plume_latitude = float(row['Plume Latitude']) if isinstance(row['Plume Latitude'], float) else float(str(row['Plume Latitude']).strip())
            plume_longitude = float(row['Plume Longitude']) if isinstance(row['Plume Longitude'], float) else float(str(row['Plume Longitude']).strip())
        except ValueError:
            continue
        if (abs(latitude - plume_latitude) < proximity_threshold and
                abs(longitude - plume_longitude) < proximity_threshold):
            return True
    return False


def get_coordinates(city_name, api_key):
    """Get latitude and longitude using OpenWeatherMap API."""
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    url = BASE_URL + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url).json()
    if response.get("coord"):
        longitude = response['coord']['lon']
        latitude = response['coord']['lat']
        return latitude, longitude
    else:
        return None, None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plume_alert', methods=['POST'])
def plume_alert():
    data = request.json
    city_name = data.get("city")
    api_key = 'acd476291ae29843ed1b64695aebaecc'  # Default API key for OpenWeatherMap

    latitude, longitude = get_coordinates(city_name, api_key)
    if latitude is None or longitude is None:
        return jsonify({"error": "Invalid city name or no data available"}), 400

    if alert(latitude, longitude, df):
        return jsonify({"message": "Gas alert! You are near a potential plume."})
    else:
        return jsonify({"message": "No gas alert needed."})


if __name__ == '__main__':
    app.run(debug=True)
