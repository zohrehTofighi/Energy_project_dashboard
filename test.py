# Packages 
import pandas as pd 
import numpy as np 
import streamlit as st 
import plotly.express as px 
from PIL import Image
import plotly.graph_objects as go 
import altair as alt 

st.set_page_config(
    page_title= "Energy Analysis Dashboard",
    page_icon="🔋", 
    layout= "wide",
    initial_sidebar_state= "expanded"
)

alt.themes.enable("dark")

# Loading file and converting the date into the right format  
data = pd.read_csv(r"C:\...\Panel format.csv")
data["Year"] = pd.to_datetime(data["Year"],format="%Y")

with st.sidebar:
    st.title("🌩️Energy Dashboard")
    st.markdown("---")

    sidebar_image = Image.open(r"C:\...\Energy1.jpeg")
    st.sidebar.image(sidebar_image, use_column_width= True)

    country = st.sidebar.selectbox("Select a country:", data["Country"].unique())
    st.markdown("---")
    st.write("Use this dashboard to explore energy production trends over time in different country.")
    st.markdown("---") 



country_data = data[data["Country"]== country]

st.title(f"Energy Production Time series Analysis for {country} ")
st.markdown("""
This dashboard provides a detailed overview of various energy production trends in the selected country. Navigate using the sidebar to choose a different country.
""")

main_image = Image.open(r"C:\...\Energy1.jpeg")
st.image(main_image, caption= "Energy Sources" ,use_column_width= True)

def create_chart(data,y,title,yaxis_title):
    fig = px.line(data,
                  x = "Year",
                  y = y,
                  title = title,
                  markers = True,
                  line_shape="spline",
                  color_discrete_sequence=px.colors.qualitative.Dark24
                 )
    

    fig.add_annotation(
            x=data['Year'].iloc[-1], 
            y=data[y].iloc[-1], 
            text="Latest Value", 
            showarrow=True, 
            arrowhead=2,
            font=dict(color="#E74C3C", size=12)
        )
    
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title=yaxis_title,
        template='plotly_white',
        font=dict(
            family="Arial, sans-serif",
            size=16,
            color="#2C3E50"
        ),
        title=dict(
            text=title,
            font=dict(size=22)
        ),
        margin=dict(l=0, r=0, t=80, b=0),
        legend=dict(
            title="Legend",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode="x unified",
        xaxis=dict(
            rangeslider=dict(visible=True),  # Adding range slider
            showline=True,
            linewidth=2,
            linecolor='black',
            mirror=True,
            gridcolor='LightGrey'  # Grid lines on x-axis
        ),
        yaxis=dict(
            showline=True,
            linewidth=2,
            linecolor='black',
            mirror=True,
            gridcolor='LightGrey'  # Grid lines on y-axis
        )
    )

    fig.update_traces(
        hovertemplate='<b>Year</b>: %{x}<br><b>Value</b>: %{y}<extra></extra>'
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("📈 Population Over Time")
create_chart(country_data, 'pop', 'Population over Time', 'Population')

st.subheader("🌊 Hydro Energy Production Over Time")
create_chart(country_data, 'hydro_ej', 'Hydro Energy Production (Exajoules)', 'Exajoules')

st.subheader("⚛️ Nuclear Energy Production Over Time")
create_chart(country_data, 'nuclear_ej', 'Nuclear Energy Production (Exajoules)', 'Exajoules')

st.subheader("♻️ Renewable Energy Production Over Time")
create_chart(country_data, 'ren_power_ej', 'Renewable Energy Production (Exajoules)', 'Exajoules')

st.subheader("☀️ Solar Energy Production Over Time")
create_chart(country_data, 'solar_ej', 'Solar Energy Production (Exajoules)', 'Exajoules')