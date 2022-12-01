import pandas as pd
df = pd.read_csv('Total_weather_dataset_in_HN.csv')
print(sorted(set(df['Date'])))
