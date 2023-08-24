'''
Получите данные по безработице в Москве:
Найдите, с какого года процент людей с ограниченными возможностями (UnemployedDisabled) среди всех безработных (UnemployedTotal) стал меньше 2%.
'''
data=pd.read_csv('https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv', delimiter=';')
data=data[['Year', 'UnemployedDisabled','UnemployedTotal']]
data=data.set_index('Year')
data['Procent']=round(data['UnemployedDisabled']*100/data['UnemployedTotal'], 1)
print(data.index [data['Procent']<2 ].tolist ()[0])