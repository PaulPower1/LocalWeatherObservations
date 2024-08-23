App to look up current weather observations for a given location
================================================================
This postman collection takes a location (city, stateCode, countryCode), looks up the latitude and longitude of this location and sets these as environment variables for use in subsequent requests.
e.g. get/ http://api.openweathermap.org/geo/1.0/direct?q={{City}},{{StateCode}},{{CountryCode}}&limit=10&appid={{API_KEY}}
   
where 
      City       = "Melbourne"
      StateCode  = "VIC"
      CoutryCode = "AU"
      API_KEY = needs to be obtained from https://openweathermap.org/ which is free to developers up to a request limit
      
The WeatherObservationsBasedonLocation /get request outputs weather observations in json using.
e.g. https://api.openweathermap.org/data/2.5/weather?lat={{latitude}}&lon={{longitude}}&appid={{API_KEY}}

 where 
    lat  = "latitude obtained from the Get/ GeoLocationLookup request"
    long = "longitutde obtained from the Get/ GeoLocationLookup request"
    API_KEY = needs to be obtained from https://openweathermap.org/ which is free to developers up to a request limit
      
Notes:
1. temperatures are expressed as kelvin in the api responses which can be converted to celsius simply by subtracting the response temp from absolute zero (273.15 - response_temp_in_kelvin).
2. these requests use https://openweathermap.org/ apis
