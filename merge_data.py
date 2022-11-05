import os
import pandas as pd

filelist = os.listdir('dataset')
c = 0
for file in filelist:
    filelist[c] = 'dataset/' + file
    c+=1
filelist = sorted(filelist, key=os.path.getctime)

df_list = []

for file in filelist:
    df = pd.read_csv(file)
    df_list.append(df)

new_df = pd.concat(df_list, ignore_index=True)
del new_df['Unnamed: 0']
new_df.to_csv('Total_weather_dataset_in_HCM.csv')