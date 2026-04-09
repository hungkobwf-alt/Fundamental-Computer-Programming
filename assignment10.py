import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    
    response = requests.get(url)
    
    data = response.json()
    
    print("Ban da bi dinh Chuck Norris joke hohihiho:")
    print(data["value"])

if __name__ == "__main__":
    get_chuck_norris_joke()

    import requests

def get_weather():
    city = input("Enter the nem of a municipality: ")

    api_key = "4d50cd82d656b98ab92033cfab0abf53" 
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        description = data["weather"][0]["description"]
        
        temp_kelvin = data["main"]["temp"]

        temp_celsius = temp_kelvin - 273.15
        
        print(f"\nWeather in {city}:")
        print(f"Condition: {description.capitalize()}")
        print(f"Temperature: {temp_celsius:.2f} °C")
    else:
        print("City not found or invalid API key.")

if __name__ == "__main__":
    get_weather()
    from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Tak 3: Prime Number Checker Service
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):

    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }

    return jsonify(result)

# Task 4: Airport Data Service
@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    try:

        with open('airports.json', 'r', encoding='utf-8') as file:
            airports_data = json.load(file)

        for airport in airports_data:
            if airport.get("icao", "").upper() == icao.upper():

                response = {
                    "icao": airport.get("icao"),
                    "name": airport.get("name"),
                    "city": airport.get("city"),
                    "country": airport.get("country")
                }
                return jsonify(response)

        return jsonify({"error": "Airport not found"}), 404
        
    except FileNotFoundError:
        return jsonify({"error": "Database file (airports.json) not found on server"}), 500

if __name__ == '__main__':
    app.run(debug=True)