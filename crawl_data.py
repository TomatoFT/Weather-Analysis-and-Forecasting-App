from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
from datetime import datetime
from datetime import timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
class Data_Processing: 
    def __init__(self, list_file=[] ,place='tan-binh',bale='VVTS', days=1000, driver=webdriver.Firefox()):
        self.days = days
        self.driver = driver
        self.time_step = []
        self.list_file = list_file
        self.board = 0
        self.place = place
        self.bale = bale

    def crawl_data(self, start_from='now'):
        for i in range(0,self.days):
            now = datetime.now() if start_from =='now' else datetime(start_from[0], start_from[1], start_from[2])
            timer = now.strftime("%Y-%m-%d")
            timer = datetime.strptime(timer, "%Y-%m-%d")
            timer = timer - timedelta(days=i)
            self.time_step.append(timer.date())
        countDate = 0
        for date in self.time_step:
            countDate +=1
            start = time.time()
            self.board +=1
            sleep_time = 4.5
            if self.board % 150 == 0:
                sleep_time += 0.5
            self.driver.get(f'https://www.wunderground.com/history/daily/vn/{self.place}/{self.bale}/date/{date}')
            print(f'https://www.wunderground.com/history/daily/vn/{self.place}/{self.bale}/date/{date}')
            content = WebDriverWait(self.driver, 3000).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]")))
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


            file = open(f'datasetDN/dataset/Weather_data_of_HCM_{self.place}_at_date_{date}.csv', "w+")
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
            self.list_file.append(f'datasetDN/dataset/Weather_data_of_HCM_{self.place}_at_date_{date}.csv')
            print('processing_time:', time.time() - start, ' seconds. ', 'Completed: ',countDate, '/ ', self.days)
        self.driver.close()

    def pre_processing(self):
        filelist = self.list_file
        print(filelist)
        unnamed_list = []
        filelist = sorted(filelist, key=os.path.getctime)
        c=0
        for file in filelist:
            df = pd.read_csv(file,  on_bad_lines='skip', encoding= 'unicode_escape')
            # df.columns = ['Time', 'Temperature', 'Dew Point', 'Humidity', 'Wind','Wind Speed', 'Wind Gust', 'Pressure', 'Precip.', 'Condition',' ']
            df.rename(columns={' Temperature': 'Temperature', ' Dew Point': 'Dew Point', ' Humidity': 'Humidity', ' Wind': 'Wind',' Wind Speed': 'Wind Speed',
                                ' Wind Gust': 'Wind Gust', ' Pressure': 'Pressure', ' Precip.': 'Precip.', ' Condition': 'Condition'}, inplace=True)
            if ' ' in df.columns:
                del df[' ']
            for col in df.columns:
                if 'Unnamed: 0' in col:
                    unnamed_list.append(col)
            for unname in unnamed_list:
                try: 
                    del df[unname]
                except:
                    pass
            df['Date']=file[-14:-4]
            for i in range(0, len(df['Temperature'])):
                try:
                    df['Temperature'][i] = float(df['Temperature'][i].replace('°F','').replace(' ',''))
                    df['Dew Point'][i] = float(df['Dew Point'][i].replace('°F','').replace(' ',''))
                    df['Humidity'][i] = float(df['Humidity'][i].replace('%','').replace(' ',''))
                    df['Wind Speed'][i] = float(df['Wind Speed'][i].replace('mph','').replace(' ',''))
                    df['Pressure'][i] = float(df['Pressure'][i].replace('in','').replace(' ',''))
                    df['Wind Gust'][i] = float(df['Wind Gust'][i].replace('mph','').replace(' ',''))
                except:
                    continue
            df['DateTime']=pd.to_datetime(df['Date'] + ' ' + df['Time'])                                                     
            df.to_csv(file)

    def merge_data(self):
        # filelist = os.listdir('dataset')
        filelist = self.list_file
        c = 0
        name_list = []
        # for file in filelist:
        #     filelist[c] = 'dataset/' + file
        #     c+=1
        filelist = sorted(filelist, key=os.path.getctime)
        df_list = []

        for file in filelist:
            df = pd.read_csv(file)
            if ' ' in df.columns:
                del df[' ']
            if 'Unnamed: 0' in df.columns:
                del df['Unnamed: 0']
            df_list.append(df)
            name_list.append(df.columns)
        # print(name_list)
        
        new_df = pd.concat(df_list, ignore_index=True)
        new_df = new_df.sort_values(by='DateTime')
        
        new_df.to_csv('Total_weather_dataset_in_HN.csv')