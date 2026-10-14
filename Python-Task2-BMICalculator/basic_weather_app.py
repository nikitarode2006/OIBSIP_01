print("Basic Weather App")

city = input("Enter city name: ").strip().title()

weather_data = {
    "Pune": "Sunny, 28°C",
    "Mumbai": "Cloudy, 30°C",
    "Delhi": "Sunny, 32°C",
    "Bangalore": "Rainy, 24°C"
}

if city in weather_data:
    print("Weather in", city + ":", weather_data[city])
else:
    print("Weather data not available for this city.")
