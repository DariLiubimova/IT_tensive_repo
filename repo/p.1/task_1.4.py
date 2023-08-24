'''
Постройте модель линейной регрессии по годам среднего значения отношения
 UnemployedDisabled к UnemployedTotal (процента людей с ограниченными возможностями) за месяц и ответьте,
 какое ожидается значение процента безработных инвалидов в 2020 году при сохранении текущей политики города Москвы?
'''
# UnemployedDisabled к UnemployedTotal
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv', delimiter=';')
#пересобираем фрейм, оставляем только нужное
data=data[['Year', 'UnemployedDisabled', 'UnemployedTotal', 'Period']]
#группировка по году, оставляем только те годы, где >= 6 строк записей
data_gr=data.groupby('Year').filter(lambda x: x['Period'].count()>=6)
# назначаем индексом колонку год
data_gr=data_gr.set_index('Year')
# вычисляем средние значения в кажом столбце по каждому году
data_gr=data_gr.groupby('Year').mean()
# заполняем столбец с отношением
data_gr['mean']=data_gr['UnemployedDisabled']*100/data_gr['UnemployedTotal']
# удаляем лишние колонки, они болььше не нужны
data_gr=data_gr.drop(['UnemployedTotal', 'UnemployedDisabled'], axis=1)
# делаем из фрейма двумерный массив numpy
x=np.array(data_gr.index).reshape(len(data_gr.index), 1)
y=np.array(data_gr['mean']).reshape(len(data_gr.index), 1)

plt.scatter(x,y)
#строим модель линейно регресии
model=LinearRegression()
model.fit(x,y)
#добавляем 2020 год
x = np.append(x, [2020]).reshape(len(data_gr.index)+1, 1)
# длаем предсказание
val=model.predict((np.array(2020).reshape(1, 1)))

plt.plot(x, model.predict(x), color="red", linewidth=3)
plt.grid()
plt.show()
#вывод результата
print('Ожидаемое значение процента\nбезработных инвалидов в 2020 году:', str(round(val[0][0],2))+'%')