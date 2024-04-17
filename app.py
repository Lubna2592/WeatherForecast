# app.py

import os
import pytz
import pyowm
import streamlit as st
from matplotlib import dates
from datetime import datetime
from matplotlib import pyplot as plt

# Set Streamlit page configuration
st.set_page_config(
    page_title="5 Day Weather Forecast",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Placeholder Text
st.title("5 Day Weather Forecast")
st.markdown("### Write the name of a City and select the Temperature Unit from the sidebar")

# Search bar for city name
place = st.text_input("Enter the name of the city:", "")
if not place:
    st.warning("Please enter a city name.")

# Selection Forms
unit = st.selectbox("Select Temperature Unit", ("Celsius", "Fahrenheit"))

# Get OpenWeatherMap API key
owm = pyowm.OWM('b2bcf7e809ddea5ada480c0b4a337e0f')
mgr = owm.weather_manager()

# Placeholder for displaying weather data
weather_placeholder = st.empty()

def display_weather_conditions(w):
    conditions = {
        "Rain": "rain" in w.detailed_status.lower(),
        "Clear Skies": "clear" in w.detailed_status.lower(),
        "Fog": "fog" in w.detailed_status.lower(),
        "Clouds": "clouds" in w.detailed_status.lower(),
        "Snow": "snow" in w.detailed_status.lower(),
        "Storm": "storm" in w.detailed_status.lower(),
        "Tornado": "tornado" in w.detailed_status.lower()
    }

    st.subheader("Specific Weather Conditions:")

    # Create a dropdown menu for the specific weather conditions
    condition = st.selectbox("Select a condition", conditions.keys())

    # Display the value of the selected condition
    st.write(f"{condition}: {'Yes' if conditions[condition] else 'No'}")

# Function to get weather data and display
def get_weather(place, unit):
    try:
        with st.spinner('Fetching weather data...'):
            forecast = mgr.forecast_at_place(place, '3h').forecast
            times = []
            temps = []

            for weather in forecast:
                times.append(weather.reference_time('iso'))
                temp = weather.temperature(unit=unit.lower())
                temps.append(temp['temp'])

            plot_line_chart(times, temps, unit, place)

            # Display current weather
            current_weather = mgr.weather_at_place(place)
            w = current_weather.weather
            st.write("### Current Weather:")
            st.write("Status:", w.status)
            st.write("Detailed Status:", w.detailed_status)
        
            # Temperature
            temperature = w.temperature(unit=unit.lower())
            st.write("Temperature:", temperature["temp"], unit)
        
            # Wind
            wind = w.wind()
            st.write("Wind Speed:", wind["speed"], "m/s")
        
            # Cloud coverage
            st.write("Cloud Coverage:", w.clouds, "%")
            
            # Humidity
            st.write("Humidity:", w.humidity, "%")
            
            # Display sunrise and sunset times
            sunrise = w.sunrise_time(timeformat='iso')
            sunset = w.sunset_time(timeformat='iso')
            st.write("Sunrise Time (GMT):", sunrise)
            st.write("Sunset Time (GMT):", sunset)

            display_weather_conditions(w)
            # Check for specific weather conditions
            #st.write("Impending Rain:", "Yes" if "rain" in w.detailed_status.lower() else "No")
            #st.write("Clear Skies:", "Yes" if "clear" in w.detailed_status.lower() else "No")
            #st.write("Fog:", "Yes" if "fog" in w.detailed_status.lower() else "No")
            #st.write("Clouds:", "Yes" if "clouds" in w.detailed_status.lower() else "No")
            #st.write("Snow:", "Yes" if "snow" in w.detailed_status.lower() else "No")
            #st.write("Storm:", "Yes" if "storm" in w.detailed_status.lower() else "No")
            #st.write("Tornado:", "Yes" if "tornado" in w.detailed_status.lower() else "No")

    except Exception as e:
        st.write("An error occurred:", e)

# Function to plot Line Chart 
def plot_line_chart(times, temps, unit, place):
    fig, ax = plt.subplots()
    ax.plot(times, temps, color='blue', linewidth=2)  # Adjust line color and thickness
    ax.xaxis.set_major_locator(dates.HourLocator())
    ax.xaxis.set_major_formatter(dates.DateFormatter('%d-%m-%Y %H:%M'))
    plt.xticks(rotation=45, fontsize=10)  # Adjust tick mark font size
    plt.yticks(fontsize=10)
    plt.xlabel('Time', fontsize=12)  # Adjust label font size
    plt.ylabel('Temperature ({})'.format(unit), fontsize=12)
    plt.title('Temperature Forecast for {}'.format(place), fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.5)  # Add grid lines
    plt.tight_layout()  # Adjust layout to prevent overlapping elements
    st.pyplot(fig)


# Call the function to display weather data
if place:
    get_weather(place, unit)

