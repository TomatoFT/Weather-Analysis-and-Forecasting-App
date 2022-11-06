import streamlit as st
import pandas as pd
import plotly_express as px
from datetime import datetime
st.title('Weather in the past')
df = pd.read_csv('Total_weather_dataset_in_HCM.csv')

day = st.selectbox('Type your day in here: ', sorted(set(df['Date']),reverse=True))
df = df.loc[df["Date"] == day]
col1, col2 = st.columns(2)
fig_pre = px.line(df, x='Time', y='Pressure', width=10)
fig_humid = px.bar(df, x='Time', y='Humidity')
fig_temp = px.bar(df, x='Time', y='Temperature')
fig_wind = px.line(df, x='Time', y='Wind Speed')

with col1:
    st.plotly_chart(fig_humid, use_container_width=True)
    st.plotly_chart(fig_pre, use_container_width=True)

with col2:
    st.plotly_chart(fig_temp, use_container_width=True)
    st.plotly_chart(fig_wind, use_container_width=True)
# print(df)