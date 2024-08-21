import streamlit as st
import requests

url = "https://api.nasa.gov/planetary/apod"
API_KEY= "/?api_key=DGnULqxH5VAKKlT22eur4XXzvqiANbbmYfxORA7y"

request = requests.get(url + API_KEY)

data = request.json()

date = data["date"]
title = data["title"]
content = data["explanation"]
image_url = data["url"]

# Image
image_filepath= "img.png"
request2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(request2.content)

# Streamlit website layout
st.title(title)
st.text(date)
st.image(image_filepath)
st.write(content)



