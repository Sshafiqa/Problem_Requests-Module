# Weather API Interaction using Requests Module

### Overview
This Python project interacts with the OpenWeatherMap public API to retrieve and display the current weather for a list of cities. Users can **add**, **update**, or **delete** cities from the list, and the script handles different HTTP methods (GET, POST, PUT, DELETE) accordingly. The application uses the `requests` module to make API calls and display weather data such as temperature, humidity, wind speed, and weather description for each city.

### Features
- **Retrieve weather data** for all cities in the list.
- **Add** a new city to the list.
- **Update** an existing city name.
- **Delete** a city from the list.
- **Menu-driven interface** for interacting with the program.

### API Information
The project uses the [OpenWeatherMap API](https://openweathermap.org/api) to get real-time weather data.
- API Base URL: `http://api.openweathermap.org/data/2.5/weather`
- API Key: You'll need an API key from OpenWeatherMap (replace the placeholder `API_KEY` in the code with your key).

### Requirements

- Python 3.x
- `requests` module (You can install it via pip: `pip install requests`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sshafiqa/Problem_Requests-Module.git
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

3. **Set your OpenWeatherMap API key:**
   Replace the value of `API_KEY` in the code with your actual OpenWeatherMap API key.

4. **Run the program:**
   ```bash
   python weather.py
   ```

### Workflow
1. When you run the program, a menu will appear with options to either fetch weather data for all cities, add a new city, update an existing city, delete a city, or exit the program.
2. Upon selecting an option, the script will interact with the OpenWeatherMap API (in case of fetching weather data) or modify the list of cities.
3. The weather data retrieved includes the following:
   - Description (e.g., clear sky, rain)
   - Temperature (in Celsius)
   - Humidity (in percentage)
   - Wind speed (in meters/second)

### Sample Output

Here’s an example of how the program output will look based on user actions:

#### 1. Fetch Weather for All Cities (GET)
```
Fetching weather for all cities:
--------------------------------
Weather in Chennai:
Description: clear sky
Temperature: 32.0°C
Humidity: 62%
Wind Speed: 3.6 m/s

Weather in New York:
Description: overcast clouds
Temperature: 15.6°C
Humidity: 75%
Wind Speed: 5.2 m/s

Weather in London:
Description: light rain
Temperature: 10.3°C
Humidity: 88%
Wind Speed: 4.1 m/s
```

#### 2. Add a City (POST)
```
Enter city name to add: San Francisco
City 'San Francisco' added successfully.

Fetching weather for all cities:
--------------------------------
Weather in Chennai:
Description: clear sky
Temperature: 32.0°C
Humidity: 62%
Wind Speed: 3.6 m/s

Weather in San Francisco:
Description: mist
Temperature: 12.3°C
Humidity: 90%
Wind Speed: 1.2 m/s
```

#### 3. Update a City (PUT)
```
Enter city name to update: Chennai
Enter new city name: Mumbai
City 'Chennai' updated to 'Mumbai'.

Fetching weather for all cities:
--------------------------------
Weather in Mumbai:
Description: clear sky
Temperature: 33.5°C
Humidity: 55%
Wind Speed: 2.8 m/s
```

#### 4. Delete a City (DELETE)
```
Enter city name to delete: London
City 'London' deleted successfully.

Fetching weather for all cities:
--------------------------------
Weather in Mumbai:
Description: clear sky
Temperature: 33.5°C
Humidity: 55%
Wind Speed: 2.8 m/s
```

### How to Use
1. Run the script, and you will see the following menu:

   ```
   1. Get weather for all cities (GET)
   2. Add a city (POST)
   3. Update a city (PUT)
   4. Delete a city (DELETE)
   5. Exit
   ```

2. Choose the desired option:
   - **Get weather for all cities**: Retrieves and displays weather data for all cities in the list.
   - **Add a city**: Add a city to the list.
   - **Update a city**: Update the name of an existing city.
   - **Delete a city**: Remove a city from the list.
   - **Exit**: Exit the program.

### Code Walkthrough

- **Weather Retrieval (`GET`)**:
  The `get_weather()` function sends a GET request to the OpenWeatherMap API, fetches the weather details, and displays them.

- **Add City (`POST`)**:
  The `add_city()` function simulates a POST request, allowing the user to add a city to the list.

- **Update City (`PUT`)**:
  The `update_city()` function simulates a PUT request, enabling the user to rename a city.

- **Delete City (`DELETE`)**:
  The `delete_city()` function simulates a DELETE request, removing a city from the list.

### Example Usage

```python
# Add a new city
add_city('San Francisco')

# Get weather for all cities
get_all_weather()

# Update city name
update_city('Chennai', 'Mumbai')

# Delete a city
delete_city('New York')
```

### Notes
- Ensure that the city names you enter are valid and correctly spelled to avoid API errors.
- The default list of cities includes `Chennai`, `New York`, and `London`. You can modify this list in the `cities` variable.
