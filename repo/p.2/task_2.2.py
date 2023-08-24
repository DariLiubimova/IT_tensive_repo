'''
Получите данные по котировкам акций со страницы: mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019
и найдите, по какому тикеру был максимальный рост числа сделок (в процентах) за 1 ноября 2019 года.
'''
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
import requests

url='https://mfd.ru/marketdata/?id=5&group=16&mode=3&sortHeader=name&sortOrder=1&selectedDate=01.11.2019'
response=requests.get(url)
#print(response)
with open('/birzha.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')
table=soup.find('table', {'id':'marketDataList'})
data=[]
for tr in table.find_all("tr"):
    data.append([td.get_text(strip=True) for td in tr.find_all("td")])
data=pd.DataFrame(data)
#оставляем только нужные столбцы
data=data.iloc[:,0:5]
data=data.drop(data.columns[[1,2,3]], axis=1)
data.columns=['tiker', 'increase']
data['increase']=data['increase'].str.slice(0,-1)
data['increase']=data['increase'].str.replace('−', '-')
data=data.dropna(how='all')
#удаление строк, которые содержат опреленное значение
values=[' ','']
data = data[data.increase.isin (values) == False ]
data['increase']=data['increase'].astype('float')
data=data.sort_values (by = ['increase', 'tiker'], ascending = [ False , True ])
print('максимальный рост числа сделок 1.11.2019 был по тикеру:', data.iloc[0]['tiker'],)