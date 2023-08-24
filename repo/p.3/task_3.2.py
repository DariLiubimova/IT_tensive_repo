'''
Загрузите данные по итогам марафона https://video.ittensive.com/python-advanced/marathon-data.csv
Приведите время половины и полной дистанции к секундам.
Найдите, данные каких серии данных коррелируют (используя диаграмму pairplot в Seaborn).
Найдите коэффициент корреляции этих серий данных, используя scipy.stats.pearsonr.
Постройте график jointplot для коррелирующих данных.
'''
import pandas as pd
import matplotlib as plt
import seaborn as sns
from scipy.stats import stats

#обработка данных
def get_seconds(time_delta):
    return time_delta.seconds

data=pd.read_csv('https://video.ittensive.com/python-advanced/marathon-data.csv', delimiter=',')
print(data.head())
datatypes = data.dtypes #узнаем тип данных в столбцах
data['split'] = pd.to_datetime(data['split'])
data['final'] = pd.to_datetime(data['final'])
data['split']=data['split'].dt.second+60*data['split'].dt.minute+3600*data['split'].dt.hour
data['final']=data['final'].dt.second+60*data['final'].dt.minute+3600*data['final'].dt.hour
#построение диаграмм
sns.set_context("paper", font_scale=2)
sns.pairplot(data[['age','gender','split','final']], hue="age", height=4)

sns.jointplot(data, x="split", y="final", height=5, kind="kde")
print (round(stats.pearsonr(data["split"], data["final"])[0], 2))