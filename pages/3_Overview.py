import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
from datetime import datetime
from plotly.subplots import make_subplots

st.title('Weather in the past')
df_HCM = pd.read_csv('Total_weather_dataset_in_HCM.csv')
df_HN = pd.read_csv('Total_weather_dataset_in_HN.csv')
df_DN = pd.read_csv('Total_weather_dataset_in_DN.csv')

df_HCM_1 = pd.read_csv('Total_weather_dataset_in_HCM.csv')
df_HN_1 = pd.read_csv('Total_weather_dataset_in_HN.csv')
df_DN_1 = pd.read_csv('Total_weather_dataset_in_DN.csv')
# df['DateTime']=pd.to_datetime(df['Date'] + ' ' + df['Time'])
listDate = set(df_HCM.Date)
df_HCM = df_HCM.groupby(by='Date').mean()
df_DN = df_DN.groupby(by='Date').mean()
df_HN = df_HN.groupby(by='Date').mean()

df_HN['Date'] = df_HN.index
df_HCM['Date'] = df_HCM.index
df_DN['Date'] = df_DN.index


df_HN['Place'] = 'HN'
df_HCM['Place'] = 'HCM'
df_DN['Place'] = 'DN'

df = pd.concat([df_HCM,df_DN,df_HN])
sections = ['Temperature', 'Dew Point', 'Humidity', 'Wind Speed', 'Wind Gust', 'Pressure']
print(sections)
section = st.selectbox('Choose your section to overview here: ',sections)

fig = px.line(df, x='Date', y=f'{section}', color='Place')
fig = make_subplots(rows=3, cols=1, subplot_titles=['HCM','DN','HN'])

fig.append_trace(go.Scatter(
    x=df_HCM['Date'],
    y=df_HCM['Temperature'],
), row=1, col=1)

fig.append_trace(go.Scatter(
    x=df_DN['Date'],
    y=df_DN['Temperature'],
), row=2, col=1)

fig.append_trace(go.Scatter(
    x=df_HN['Date'],
    y=df_HN['Temperature'],
), row=3, col=1)
fig.update_layout(height=400, width=600, title_text="Comparion about Temperature")


fig_humid = make_subplots(rows=3, cols=1, subplot_titles=['HCM','DN','HN'])

fig_humid.append_trace(go.Scatter(
    x=df_HCM['Date'],
    y=df_HCM['Humidity'],
), row=1, col=1)

fig_humid.append_trace(go.Scatter(
    x=df_DN['Date'],
    y=df_DN['Humidity'],
), row=2, col=1)

fig_humid.append_trace(go.Scatter(
    x=df_HN['Date'],
    y=df_HN['Humidity'],
), row=3, col=1)
fig_humid.update_layout(height=400, width=600, title_text="Comparion about Humidity")

fig_ws = make_subplots(rows=3, cols=1, subplot_titles=['HCM','DN','HN'])

fig_ws.append_trace(go.Scatter(
    x=df_HCM['Date'],
    y=df_HCM['Wind Speed'],
), row=1, col=1)

fig_ws.append_trace(go.Scatter(
    x=df_DN['Date'],
    y=df_DN['Wind Speed'],
), row=2, col=1)

fig_ws.append_trace(go.Scatter(
    x=df_HN['Date'],
    y=df_HN['Wind Speed'],
), row=3, col=1)
fig_ws.update_layout(height=400, width=600, title_text="Comparion about Wind Speed")

fig_dew = make_subplots(rows=3, cols=1, subplot_titles=['HCM','DN','HN'])

fig_dew.append_trace(go.Scatter(
    x=df_HCM['Date'],
    y=df_HCM['Dew Point'],
), row=1, col=1)

fig_dew.append_trace(go.Scatter(
    x=df_DN['Date'],
    y=df_DN['Dew Point'],
), row=2, col=1)

fig_dew.append_trace(go.Scatter(
    x=df_HN['Date'],
    y=df_HN['Dew Point'],
), row=3, col=1)
fig_dew.update_layout(height=400, width=600, title_text="Comparion about Dew Point")
# fig = go.Figure(df)
# fig.show()
lb1, vl1 = df_HCM_1['Wind'].value_counts().keys, df_HCM_1['Wind'].value_counts().values
df_HCM_pie = df_HCM_1.Wind.value_counts()
df_HN_pie = df_HN_1.Wind.value_counts()
df_DN_pie = df_DN_1.Wind.value_counts()

df_HCM_pie_1 = df_HCM_1.Condition.value_counts()
df_HN_pie_1 = df_HN_1.Condition.value_counts()
df_DN_pie_1 = df_DN_1.Condition.value_counts()


fig_w = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]])
fig_w.add_trace(go.Pie(labels=df_HCM_pie.index, values=df_HCM_pie.values, name="HCM"),1, 1)
fig_w.add_trace(go.Pie(labels=df_HN_pie.index, values=df_HN_pie.values, name="HN"),1, 2)
fig_w.add_trace(go.Pie(labels=df_DN_pie.index, values=df_DN_pie.values, name="DN"),1, 3)

# Use `hole` to create a donut-like pie chart
fig_w.update_traces(hole=.4, hoverinfo="label+percent+name")

fig_w.update_layout(
    title_text="Wind types in 2019-2022",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='HCM', x=0.1, y=0.5, font_size=20, showarrow=False),
                 dict(text='HN', x=0.50, y=0.5, font_size=20, showarrow=False),
                 dict(text='DN', x=0.85, y=0.5, font_size=20, showarrow=False)])

# fig_c = make_subplots(rows=1, cols=3)
# # fig_c.add_trace(go.Figure(labels=df_HCM_pie_1.index, values=df_HCM_pie_1.values, name="HCM"),1, 1)
# # fig_c.add_trace(go.Figure(labels=df_HN_pie_1.index, values=df_HN_pie_1.values, name="HN"),1, 2)
# # fig_c.add_trace(go.Figure(labels=df_DN_pie_1.index, values=df_DN_pie_1.values, name="DN"),1, 3)
# fig_c.add_trace(go.Pie(labels=df_HCM_pie_1.index, values=df_HCM_pie_1.values),1, 1)
# fig_c.add_trace(go.Pie(labels=df_HN_pie_1.index, values=df_HN_pie_1.values),1, 2)
# fig_c.add_trace(go.Pie(labels=df_DN_pie_1.index, values=df_DN_pie_1.values),1, 3)
# # Use `hole` to create a donut-like pie chart
# fig_c.update_traces(hole=.4, hoverinfo="label+percent+name")

# fig_c.update_layout(
#     title_text="Conditions in 2019-2022",
#     # Add annotations in the center of the donut pies.
#     annotations=[dict(text='HCM', x=0.1, y=0.5, font_size=20, showarrow=False),
#                  dict(text='HN', x=0.50, y=0.5, font_size=20, showarrow=False),
#                  dict(text='DN', x=0.85, y=0.5, font_size=20, showarrow=False)])


fig1 = px.pie(df_HCM_pie_1, values='Condition',names=df_HCM_pie_1.index, labels=df_HCM_pie_1.index, title='Condition distribution in HCM')
fig1.update_traces(textposition='inside')
fig1.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig2 = px.pie(df_HN_pie_1, values='Condition',names=df_HN_pie_1.index, labels=df_HN_pie_1.index, title='Condition distribution in HN')
fig2.update_traces(textposition='inside')
fig2.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig3 = px.pie(df_DN_pie_1, values='Condition',names=df_DN_pie_1, labels=df_DN_pie_1.index, title='Condition distribution in DN')
fig3.update_traces(textposition='inside')
fig3.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.plotly_chart(fig_humid, use_container_width=True)
col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(fig_ws, use_container_width=True)
with col4:
    st.plotly_chart(fig_dew, use_container_width=True)

st.plotly_chart(fig_w, use_container_width=True)
# col7, col8, col9 = st.columns(3)
# with col7:
st.plotly_chart(fig1, use_container_width=True)
# with col8:
st.plotly_chart(fig2, use_container_width=True)
# with col9:
st.plotly_chart(fig3, use_container_width=True)