def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"   # For Celsius
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nWeather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f" Wind Speed: {data['wind']['speed']} m/s")
        print(f" Condition: {data['weather'][0]['description'].capitalize()}")
    else:
        print(" City not found or error fetching data.")

if _name_ == "_main_":
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    get_weather(city, api_key)
