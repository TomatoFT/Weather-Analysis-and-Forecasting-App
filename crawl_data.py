from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from datetime import timedelta
import pandas as pd
import os
class Data_Processing: 
    def __init__(self, days=1000, driver=webdriver.Firefox()):
        self.days = days
        self.driver = driver
        self.time_step = []
        self.list_file = []
        self.board = 0

    def crawl_data(self, start_from='now'):
        for i in range(0,self.days):
            now = datetime.now() if start_from =='now' else datetime(start_from[0], start_from[1], start_from[2])
            time = now.strftime("%Y-%m-%d")
            time = datetime.strptime(time, "%Y-%m-%d")
            time = time - timedelta(days=i)
            self.time_step.append(time.date())
    
        for date in self.time_step:
            place = 'tan-binh'
            self.board +=1
            sleep_time = 4.5
            if self.board % 150 == 0:
                sleep_time += 0.5
            self.driver.get(f'https://www.wunderground.com/history/daily/vn/{place}/VVTS/date/{date}')
            print(f'https://www.wunderground.com/history/daily/vn/{place}/VVTS/date/{date}')
            sleep(sleep_time)
            content = self.driver.find_elements(By.XPATH, value="/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]")
            header, data, real_data = [], [], []

            for con in content:
                content = con.text
            content = content.split('\n')
            c = 0
            for con in content:
                if c < 10:
                    header.append(con)
                else: 
                    data.append(con)
                c+=1
            
            for element in data:
                count,prev,wind,item = 0,0,0,0
                col = []
                for i in range(0,len(element)):
                    if element[i] == ' ':
                        count +=1
                    else:
                        continue
                    if wind == 4:
                        count+=1
                        wind=5
                    if count % 2 == 0:
                        col.append(element[prev:i])
                        prev,count = i+1, 0
                        wind+=1
                        item+=1
                    if item == 9:
                        col.append(element[i+1:])
                        break
                # print(col)
                real_data.append(col)


            file = open(f'dataset/Weather_data_of_HCM_{place}_at_date_{date}.csv', "w")
            for head in header:
                file.write(head)
                file.write(', ')
            file.write('\n')

            for clean in real_data:
                for da in clean:
                    file.write(da)
                    file.write(', ')
                file.write('\n')
            file.close()
            self.list_file.append(f'dataset/Weather_data_of_HCM_{place}_at_date_{date}.csv')
        self.driver.close()

    def pre_processing(self):
        filelist = self.list_file
        c = 0
        # for file in filelist:
        #     filelist[c] = 'dataset/' + file
        #     c+=1
        filelist = sorted(filelist, key=os.path.getctime)

        for file in filelist:
            df = pd.read_csv(file,  on_bad_lines='skip')
            print(df.columns)
            df.columns = ['Time', 'Temperature', 'Dew Point', 'Humidity', 'Wind','Wind Speed', 'Wind Gust', 'Pressure', 'Precip.', 'Condition',' ']
            if ' ' in df.columns:
                del df[' ']
            if 'Unnamed 0' in df.columns:
                del df['Unnamed 0']
            df['Date']=file[-14:-4]
            for i in range(0, len(df['Temperature'])):
                df['Temperature'][i] = float(df['Temperature'][i][1:-3])
                df['Dew Point'][i] = float(df['Dew Point'][i][1:-3])
                df['Humidity'][i] = int(df['Humidity'][i][1:-2])
                df['Wind Speed'][i] = int(df['Wind Speed'][i][1:-4])
                df['Pressure'][i] = float(df['Pressure'][i][1:-3])
                df['Precip.'][i] = float(df['Precip.'][i][1:-2])
                df['Wind Gust'][i] = float(df['Wind Gust'][i][1:-3])
            df['DateTime']=pd.to_datetime(df['Date'] + ' ' + df['Time'])
            # df['Temperature']=round(float((df['Temperature']-32)*5/9),1)
            # df['Dew Point']=round(float((df['Dew Point']-32))*5/9,1)
            df.to_csv(file)

    def merge_data(self):
        filelist = os.listdir('dataset')
        c = 0
        for file in filelist:
            filelist[c] = 'dataset/' + file
            c+=1
        filelist = sorted(filelist, key=os.path.getctime)
        df_list = []

        for file in filelist:
            df = pd.read_csv(file)
            if ' ' in df.columns:
                del df[' ']
            if 'Unnamed: 0' in df.columns:
                del df['Unnamed: 0']
            df_list.append(df)

        new_df = pd.concat(df_list, ignore_index=True)
        new_df.to_csv('Total_weather_dataset_in_HCM.csv')