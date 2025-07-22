#import packages

import urllib.request
import urllib.parse
import json

#Asking user for city
city = input("Enter your city name: ").strip()

#Encode the city name to handle spaces
encoded_city = urllib.parse.quote(city)

#Constructing the URL
api_key = "5b5d70712bd0889d72ff59d4d11a7182" #REplace with actual API Key
base_url = "http://api.openweathermap.org/data/2.5/weather?"
units = "imperial"
full_url = base_url + "q=" + city + "&appid=" + api_key + "&units=" + units

#Send Request and Get Response
try:
    response  = urllib.request.urlopen(full_url)
    data = response.read().decode()
    parsed = json.loads(data)

    #check if city was found
    if parsed.get("cod") != 200:
        print("Error:", parsed.get("message"))
    else:
        temp = parsed['main']['temp']
        desc = parsed['weather'][0]['description']
        humidity = parsed['main']['humidity']
        wind_speed = parsed['wind']['speed']

    print(f"\nweather in {city}:")
    print(f"Temperature: {temp}\u00B0F")
    print(f"Description: {desc.capitalize()}")
    print(f"Humidity {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

except Exception as e:
    print("Something went wrong:", e)
