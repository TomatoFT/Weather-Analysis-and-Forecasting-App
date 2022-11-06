import streamlit as st
import pandas as pd
import plotly_express as px
from datetime import datetime
st.title('Weather in the past')
df = pd.read_csv('Total_weather_dataset_in_HCM.csv')
df['DateTime']=pd.to_datetime(df['Date'] + ' ' + df['Time'])
sections = df.columns.values.tolist()
# print(sections)
sections.remove('Unnamed: 0')
sections.remove('Date')
sections.remove('Time')
sections.remove('DateTime')
section = st.selectbox('Type your section to overview here: ', sections)
# df = df.loc[df["Date"] == day]
# col1, col2 = st.columns(2)
fig_pre = px.bar(df, x='DateTime', y=section,color_discrete_sequence=px.colors.qualitative.Dark2)

st.plotly_chart(fig_pre, use_container_width=False)
