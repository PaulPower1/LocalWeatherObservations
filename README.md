App to look up current weather observations for a given location
================================================================
This postman collection takes a location(City,StateCode,CountryCode), looks up the latitude and longitude of this location and sets these as environment variables for use in subsequent requests.
The WeatherObservationsBasedonLocation /get request outputs observations in json. 

Notes:
1. temperatures are reported back as Kelvin which can be converted to celsius simply by subtracting the response temp from absolute zero (273.15 - response_temp_in_kelvin).
2. these requests use https://openweathermap.org/ apis
