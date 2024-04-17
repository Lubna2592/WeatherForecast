# WeatherForecast

The project aims to create a weather forecasting application using Python and Streamlit, which allows users to visualize the weather forecast for the next five days. The application retrieves weather data from the OpenWeatherMap API and presents it in an intuitive and user-friendly interface.

Key Features:

User Input: Users can input the name of a city and select the temperature unit (Celsius or Fahrenheit) and graph type (Line Graph or Bar Graph) through the application's interface.

Weather Forecast: The application fetches the 5-day weather forecast data with 3-hour intervals using the PyOWM library. It displays the temperature forecast for the selected city using either a line graph, depending on the user's preference.

Additional Weather Information: Along with the temperature forecast, the application provides additional weather updates such as cloud coverage, wind speed, humidity, and impending weather conditions (rain, clear skies, fog, clouds, snow, storm, tornado).

Sunrise and Sunset Times: Users can also view the sunrise and sunset times for the selected city in GMT.

Deployment:
The application can be deployed on the Heroku platform for free. After creating a Heroku account and setting up the necessary files (requirements.txt, Procfile), the application can be deployed using the Heroku Command Line Interface (CLI).

Overall, this weather forecasting application provides users with comprehensive weather information and empowers them to make informed decisions based on the forecasted weather conditions. It demonstrates the integration of various Python libraries and APIs to create a practical and interactive data visualization tool.
