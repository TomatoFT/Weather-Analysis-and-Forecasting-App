import streamlit as st
import pandas as pd
import plotly_express as px
from datetime import datetime, timedelta
from tensorflow.keras.models import load_model
import numpy as np
from scripts.TimeCalc import *

st.title('Weather forecasting system')
df = pd.read_csv('Total_weather_dataset_in_HCM.csv')
place_list = ['HCM', 'HN', 'DN']
place = st.selectbox('Type your place in here: ',place_list)
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Temperature", "Humidity", "Pressure", "Dew Point", "Wind Speed"])

with tab1:
    st.header("Temperature")
    item = "Temperature"
    model = load_model(f'/home/tomato/Desktop/UIT/DS105/model/model_temperature_{place}.h5')
    now = df.iloc[-1].Date
    print(now)
    timestep = sorted([ConvertTo24h(daytime) for daytime in set(df.Time)])
    df[item]=round((df[item]-32)*5/9,1)
    test = np.array(df[item][28598:])
    test=test.reshape(-1,1)
    step = 8
    test = np.append(test,np.repeat(test[-1,],step))
    testX,testY =convertToMatrix(test,step)
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    finalTest = np.reshape(np.asarray(testX[-1][-1].tolist()),(1,1,step))
    predicted = []
    for i in range(0,50,1):
        pred_temp = model.predict(finalTest)
        tempTest = finalTest[-1][-1].tolist()
        tempTest = tempTest[1:]
        tempTest.append(round(pred_temp[0][0],1))
        finalTest =np.reshape(np.asarray(tempTest), (1,1,step))
        predicted.append(round(min(pred_temp[0][0],100),1))
    df_temp = pd.DataFrame({'Time':timestep,'Forecasting (degree in Celcius)':predicted})
    df_temp['Date'] = Tommorow(now)
    fig = px.line(df_temp, x="Time", y="Forecasting (degree in Celcius)")
    fig.update_traces(textposition="bottom right")
    st.plotly_chart(fig,use_container_width=True)
with tab2:
    st.header("Humidity")
    item = "Humidity"
    model = load_model(f'/home/tomato/Desktop/UIT/DS105/model/model_humid_{place}.h5')
    now = df.iloc[-1].Date
    timestep = sorted([ConvertTo24h(daytime) for daytime in set(df.Time)])
    test = np.array(df[item][28598:])
    test=test.reshape(-1,1)
    step = 8
    test = np.append(test,np.repeat(test[-1,],step))
    testX,testY =convertToMatrix(test,step)
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    finalTest = np.reshape(np.asarray(testX[-1][-1].tolist()),(1,1,step))
    predicted = []
    for i in range(0,50,1):
        pred_temp = model.predict(finalTest)
        tempTest = finalTest[-1][-1].tolist()
        tempTest = tempTest[1:]
        tempTest.append(round(pred_temp[0][0],1))
        finalTest =np.reshape(np.asarray(tempTest), (1,1,step))
        predicted.append(round(min(pred_temp[0][0],100),1))
    df_temp = pd.DataFrame({'Time':timestep,'Forecasting (degree in Celcius)':predicted})
    df_temp['Date'] = Tommorow(now)
    fig = px.line(df_temp, x="Time", y="Forecasting (degree in Celcius)")
    fig.update_traces(textposition="bottom right")
    st.plotly_chart(fig,use_container_width=True)
with tab3:
    st.header("Pressure")
    item = "Pressure"
    model = load_model(f'/home/tomato/Desktop/UIT/DS105/model/model_Pressure_{place}.h5')
    now = df.iloc[-1].Date
    timestep = sorted([ConvertTo24h(daytime) for daytime in set(df.Time)])
    test = np.array(df[item][28598:])
    test=test.reshape(-1,1)
    step = 8
    test = np.append(test,np.repeat(test[-1,],step))
    testX,testY =convertToMatrix(test,step)
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    finalTest = np.reshape(np.asarray(testX[-1][-1].tolist()),(1,1,step))
    predicted = []
    for i in range(0,50,1):
        pred_temp = model.predict(finalTest)
        tempTest = finalTest[-1][-1].tolist()
        tempTest = tempTest[1:]
        tempTest.append(round(pred_temp[0][0],1))
        finalTest =np.reshape(np.asarray(tempTest), (1,1,step))
        predicted.append(round(min(pred_temp[0][0],100),1))
    df_temp = pd.DataFrame({'Time':timestep,'Forecasting (degree in Celcius)':predicted})
    df_temp['Date'] = Tommorow(now)
    fig = px.line(df_temp, x="Time", y="Forecasting (degree in Celcius)")
    fig.update_traces(textposition="bottom right")
    st.plotly_chart(fig,use_container_width=True)
with tab4:
    st.header("Dew Point")
    item = "Dew Point"
    model = load_model(f'/home/tomato/Desktop/UIT/DS105/model/model_dew_{place}.h5')
    now = df.iloc[-1].Date
    timestep = sorted([ConvertTo24h(daytime) for daytime in set(df.Time)])
    df[item]=round((df[item]-32)*5/9,1)
    test = np.array(df[item][28598:])
    test=test.reshape(-1,1)
    step = 8
    test = np.append(test,np.repeat(test[-1,],step))
    testX,testY =convertToMatrix(test,step)
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    finalTest = np.reshape(np.asarray(testX[-1][-1].tolist()),(1,1,step))
    predicted = []
    for i in range(0,50,1):
        pred_temp = model.predict(finalTest)
        tempTest = finalTest[-1][-1].tolist()
        tempTest = tempTest[1:]
        tempTest.append(round(pred_temp[0][0],1))
        finalTest =np.reshape(np.asarray(tempTest), (1,1,step))
        predicted.append(round(min(pred_temp[0][0],100),1))
    df_temp = pd.DataFrame({'Time':timestep,'Forecasting (degree in Celcius)':predicted})
    df_temp['Date'] = Tommorow(now)
    fig = px.line(df_temp, x="Time", y="Forecasting (degree in Celcius)")
    fig.update_traces(textposition="bottom right")
    st.plotly_chart(fig,use_container_width=True)
with tab5:
    st.header("Wind Speed")
    item = "Wind Speed"
    model = load_model(f'/home/tomato/Desktop/UIT/DS105/model/model_wind_speed_{place}.h5')
    now = df.iloc[-1].Date
    timestep = sorted([ConvertTo24h(daytime) for daytime in set(df.Time)])
    df[item]=round((df[item]-32)*5/9,1)
    test = np.array(df[item][28598:])
    test=test.reshape(-1,1)
    step = 8
    test = np.append(test,np.repeat(test[-1,],step))
    testX,testY =convertToMatrix(test,step)
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    finalTest = np.reshape(np.asarray(testX[-1][-1].tolist()),(1,1,step))
    predicted = []
    for i in range(0,50,1):
        pred_temp = model.predict(finalTest)
        tempTest = finalTest[-1][-1].tolist()
        tempTest = tempTest[1:]
        tempTest.append(round(pred_temp[0][0],1))
        finalTest =np.reshape(np.asarray(tempTest), (1,1,step))
        predicted.append(round(min(pred_temp[0][0],100),1))
    df_temp = pd.DataFrame({'Time':timestep,'Forecasting':predicted})
    df_temp['Date'] = Tommorow(now)
    fig = px.line(df_temp, x="Time", y="Forecasting")
    fig.update_traces(textposition="bottom right")
    st.plotly_chart(fig,use_container_width=True)

# st.dataframe(pred_df)
