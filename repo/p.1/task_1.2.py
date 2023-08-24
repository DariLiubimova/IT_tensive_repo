'''
Получите данные по безработице в Москве:
Объедините эти данные индексами (Месяц/Год) с данными из предыдущего задания (вызовы пожарных) для Центральный административный округ:
Найдите значение поля UnemployedMen в том месяце, когда было меньше всего вызовов в Центральном административном округе.
'''
data_1=pd.read_csv('https://video.ittensive.com/python-advanced/data-5283-2019-10-04.utf.csv', delimiter=';', na_values="NaN") #вызовы пожарных
data_2=pd.read_csv('https://video.ittensive.com/python-advanced/data-9753-2019-07-25.utf.csv',  delimiter=';', na_values="NaN") #уровень безработицы
center_area = data_1[data_1["AdmArea"].str.contains("Центральный административный округ")]
center_area=center_area[['Year', 'Month', 'Calls']]
fire_calls=center_area.set_index(['Year', 'Month'])
Unemployed=data_2[['Year', 'Period', 'UnemployedMen']]
Unemployed= Unemployed.rename(columns = {"Period":"Month"}) #переименовать название колонки
Unemployed=Unemployed.set_index(['Year', 'Month'])
new_data=pd.merge(fire_calls, Unemployed, left_index=True, right_index=True)
#способ 1
'''min_calls=new_data['Calls'].min()
print(min_calls)
men_count=new_data.UnemployedMen.where(new_data.Calls==min_calls)
print(men_count)'''
#способ 2
new_data=new_data.reset_index()
new_data=new_data.set_index(['Calls'])
new_data=new_data.sort_index() #сортировка по индексу
print(new_data['UnemployedMen'][0:1]) # вывод первой  строки