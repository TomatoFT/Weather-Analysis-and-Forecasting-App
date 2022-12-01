import pandas as pd
import os

filelist = os.listdir('dataset')
c = 0
for file in filelist:
    filelist[c] = 'dataset/' + file
    c+=1
filelist = sorted(filelist, key=os.path.getctime)

for file in filelist:
    df = pd.read_csv(file,  on_bad_lines='skip')
    df.columns = ['Time', 'Temperature', 'Dew Point', 'Humidity', 'Wind',
        'Wind Speed', 'Wind Gust', 'Pressure', 'Precip.', 'Condition',' ']
    if 'Condition' in df.columns:
        del df['Condition']
    if ' ' in df.columns:
        del df[' ']
    df['Date']=file[-14:-4]
    df.to_csv(file)

        