'''
Загрузите данные по ЕГЭ за последние годы
https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv
выберите данные за 2018-2019 учебный год.
Выберите тип диаграммы для отображения результатов по административному округу Москвы, постройте выбранную диаграмму для количества школьников, написавших ЕГЭ на 220 баллов и выше.
Выберите тип диаграммы и постройте ее для районов Северо-Западного административного округа Москвы для количества школьников, написавших ЕГЭ на 220 баллов и выше.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#обработка данных
data=pd.read_csv('https://video.ittensive.com/python-advanced/data-9722-2019-10-14.utf.csv', delimiter=';')
data=data.drop(['EDU_NAME', 'ID', 'global_id', 'Unnamed: 8', 'PASSER_UNDER_160'], axis=1)
data['AdmArea']=data['AdmArea'].str.replace('административный округ', '')
data['District']=data['District'].str.replace('район', '')
data=data.loc[data['YEAR'] =='2018-2019']
data=data.drop(['YEAR'], axis=1)
pupils=data.groupby('AdmArea').mean()['PASSES_OVER_220']

#диаграмма для количества школьников, написавших ЕГЭ на 220 баллов и выше по округам Москвы
fig = plt.figure(figsize=(12, 12))
area = fig.add_subplot(2, 1, 1)
fig.tight_layout(pad=11) #задаем расстояние между графиками
pupils.plot.area(ax=area, label="Количество школьников,\nнаписавших ЕГЭ на 220 баллов и выше", color="orange")
area.legend()
j=0
for i in pupils:
    area.annotate(round(i), xy=(j-0.1,i*1.02))
    j += 1
pupils=pupils.reset_index()
plt.xticks(ticks=np.arange(0,12,step=1), labels=pupils['AdmArea'])
plt.xticks(rotation = 90)
area.set_xlabel("Округ г. Москвы")

plt.tick_params(axis='x', which='major', labelsize=8)

#для северо-западного округа

sz_data=data[data['AdmArea'].str.contains('Северо-Западный')].drop(['AdmArea'], axis=1)
otvet=sz_data[sz_data['District'].str.contains('Строгино')].groupby('District').sum()['PASSES_OVER_220']
print(otvet)
sz_data=sz_data.groupby('District').sum()['PASSES_OVER_220']
print(sz_data)

#построение графика
area = fig.add_subplot(2, 1, 2)
#adm = data.groupby("AdmArea").filter(lambda x:x["Calls"].count() > 2)
#adm = adm.groupby("AdmArea").mean()["Calls"]
total = sum(sz_data)
print(total)
sz_data.plot.pie(ax=area, label="", autopct=lambda x: int(total * x/100))
plt.show()