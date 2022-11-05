import streamlit as st
import pandas as pd
import plotly_express as px
from datetime import datetime
df = pd.read_csv('Total_weather_dataset_in_HCM.csv')

day = st.selectbox('Type your day in here: ', sorted(set(df['Date']),reverse=True))
df = df.loc[df["Date"] == day]
col1, col2 = st.columns(2)
fig = px.bar(df, x='Time', y='Pressure')
with col1:
    st.line_chart(df,x='Time', y='Humidity')
    st.line_chart(df, x='Time', y='Pressure')
    # st.plotly_chart(fig, use_container_width=True)
with col2:
    st.line_chart(df, x='Time', y='Wind Speed')
    st.line_chart(df, x='Time', y='Temperature')
# print(df)