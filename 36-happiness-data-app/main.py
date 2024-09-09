import streamlit as st
import plotly as px
import pandas as pd

# Add a title widget
st.title("In Search for Happiness")

# Add two select boxes
select_x = st.selectbox(label="Select the data for the X-axis",
             options=["GDP", "Happiness", "Generosity"])

select_y = st.selectbox(label="Select the data for the Y-axis",
             options=["GDP", "Happiness", "Generosity"])

# Load the dataframe
df = pd.read_csv("36-happiness-data-app/happy.csv")
# Match the value of the first select box
match select_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

# Match the value of the second select box
match select_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

# Dynamic title for which data is displayed
st.subheader(f"{select_x} and {select_y}")

# Create and add the plot widget

data = x_array, y_array
figure1 = px.plot(x=x_array, y=y_array, kind="scatter", data_frame=data,
                     labels={"x": select_x, "y": select_y})
st.plotly_chart(figure1)