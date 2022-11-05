from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

driver = webdriver.Firefox()
date, place = '2022-10-1', 'tan-binh'
driver.get(f'https://www.wunderground.com/history/daily/vn/{place}/VVTS/date/{date}')
time.sleep(8)
content = driver.find_elements(By.XPATH, value="/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]")
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
    count,prev,wind = 0,0,0
    col = []
    for i in range(0,len(element)):
        if element[i] == ' ':
            count +=1
        else:
            continue
        if count % 2 == 0:
            col.append(element[prev:i])
            prev = i+1
            count = 0
            wind+=1
        if wind == 4:
            element = element[:i] + ' ' + element[i:]
            wind+=1
    print(col)
    real_data.append(col)


file = open('Text_file.csv', "w")
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
driver.close()