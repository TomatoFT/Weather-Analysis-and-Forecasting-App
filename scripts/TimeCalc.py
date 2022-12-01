from datetime import datetime, timedelta
import numpy as np
def ConvertTo24h(m2):
  in_time = datetime.strptime(m2, "%I:%M %p")
  out_time = datetime.strftime(in_time, "%H:%M")
  return out_time
def Tommorow(timer):
  timer = timer.split('-')
  timer = [int(timeInAday) for timeInAday in timer]
  timer = datetime(timer[0],timer[1],timer[2])
  timer = timer.strftime("%Y-%m-%d")
  timer = datetime.strptime(timer, "%Y-%m-%d")
  timer = timer + timedelta(days=1)
  timer = timer.strftime("%Y-%m-%d")
  return timer

def convertToMatrix(data, step):
  X, Y =[], []
  for i in range(len(data)-step):
    d=i+step  
    X.append(data[i:d,])
    Y.append(data[d,])
  return np.array(X), np.array(Y)