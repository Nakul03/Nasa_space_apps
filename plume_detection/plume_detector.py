

import pandas as pd
import numpy as np

df = pd.read_excel('CH4-CO2_Benchmark_Metadata.xlsx')
df

import pandas as pd
import numpy as np


def alert(latitude, longitude, df):


  proximity_threshold = 0.1

  for index, row in df.iterrows():

    try:
      plume_latitude = float(row['Plume Latitude']) if isinstance(row['Plume Latitude'], float) else float(str(row['Plume Latitude']).strip())
      plume_longitude = float(row['Plume Longitude']) if isinstance(row['Plume Longitude'], float) else float(str(row['Plume Longitude']).strip())
    except ValueError:
      print(f"Warning: Skipping row {index} due to invalid latitude or longitude value.")
      continue

    try:
      latitude = float(latitude)
      longitude = float(longitude)
    except ValueError:
      print(f"Invalid Detection {index} ")
      continue

    if (abs(latitude - plume_latitude) < proximity_threshold and
        abs(longitude - plume_longitude) < proximity_threshold):
      return True

  return False



from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_location():
  try:
    geo = Nominatim(user_agent="geoapiExercises")
    loc = geo.geocode("My current location")
    if loc:
      return (loc.latitude, loc.longitude)
  except GeocoderTimedOut:
    print("Geocoder timed out. Please check your internet connection or try again later.")
  except Exception as e:
    print(f"Error getting location: {e}")
  return None

import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = 'acd476291ae29843ed1b64695aebaecc'
CITY = str(input("Enter the city name:")).upper()
print(CITY)

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()



longitude = response['coord']['lon']

latitude =  response['coord']['lat']

print(longitude,latitude)

current_location = latitude, longitude

if current_location:

  if alert(latitude, longitude, df):
    print(f"Gas alert! You are near a potential plume.")
  else:
    print("No gas alert needed.")
else:
  print("Unable to determine your current location.")

print("\nOr Making it available on latitude or longitude \n ")
try:
  if latitude and longitude:
    if alert(latitude, longitude, df):
      print(f"Gas alert! You are near a potential plume.")
    else:
      print("No gas alert needed.")
  else:
    print("Unable to determine your current location.")
except NameError:
  print("Namer Erro")