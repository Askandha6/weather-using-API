Features
Fetches current temperature, weather condition, and wind speed.
Simple command-line interface.
Uses OpenWeatherMap (free API).
Requirements
Python 3.x
requests library
Install requests if not already installed:
Copy code
Bash
pip install requests
Setup
Create a free account on OpenWeatherMap.
Generate your API Key.
Replace "YOUR_API_KEY" in the code with your actual API key.
Usage
Run the program in terminal:
Bash
python weather_app.py
Example:
Enter city name: London
Weather in London, GB:
 Temperature: 16°C
 Wind Speed: 4.5 m/s
 Condition: Clear sky
Notes
Ensure you have an active internet connection.
If a wrong city name is entered, the program will display an error message.
Units are in Celsius by default.
