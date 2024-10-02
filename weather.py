import requests

# Simulate a "database" for storing city names (in memory)
cities = ['Chennai', 'New York', 'London']

API_KEY = 'd575ef109b875ddb7c8337d914f92b12'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather(city_name):
    """Retrieve and display weather for a single city."""
    url = f'{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\nWeather in {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")
    elif response.status_code == 404:
        print(f"Error: City '{city_name}' not found.")
    else:
        print(f"Error: Unable to retrieve weather data for {city_name}. Status Code: {response.status_code}")


def get_all_weather():
    """Retrieve weather for all cities in the list."""
    if not cities:
        print("No cities to display.")
    else:
        for city in cities:
            get_weather(city)


def add_city(city_name):
    """Simulate POST request to add a city to the list."""
    if city_name not in cities:
        cities.append(city_name)
        print(f"City '{city_name}' added successfully.")
    else:
        print(f"City '{city_name}' is already in the list.")


def update_city(old_city, new_city):
    """Simulate PUT request to update an existing city in the list."""
    if old_city in cities:
        index = cities.index(old_city)
        cities[index] = new_city
        print(f"City '{old_city}' updated to '{new_city}'.")
    else:
        print(f"City '{old_city}' not found in the list.")


def delete_city(city_name):
    """Simulate DELETE request to remove a city from the list."""
    if city_name in cities:
        cities.remove(city_name)
        print(f"City '{city_name}' deleted successfully.")
    else:
        print(f"City '{city_name}' not found in the list.")


# Example usage
def menu():
    """Display options to the user and handle user input."""
    while True:
        print("\nMenu:")
        print("1. Get weather for all cities (GET)")
        print("2. Add a city (POST)")
        print("3. Update a city (PUT)")
        print("4. Delete a city (DELETE)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nFetching weather for all cities:")
            get_all_weather()

        elif choice == '2':
            city_name = input("Enter city name to add: ")
            add_city(city_name)

        elif choice == '3':
            old_city = input("Enter city name to update: ")
            new_city = input("Enter new city name: ")
            update_city(old_city, new_city)

        elif choice == '4':
            city_name = input("Enter city name to delete: ")
            delete_city(city_name)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    menu()
