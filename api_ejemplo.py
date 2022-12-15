import os
import streamlit as st
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY=os.getenv("API_KEY", "123APIKEY")

ubicación = "Santiago,cl"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={ubicación}&APPID={WEATHER_API_KEY}&lang=es"
datos = requests.get(URL)

datos_json = datos.json()

st.set_page_config(
  layout="wide"
)

st.header("Información desde API")

st.info("Temperaturas de una Comuna")
st.success(f"El clima ahora está: {datos_json['weather'][0]['description']}")
