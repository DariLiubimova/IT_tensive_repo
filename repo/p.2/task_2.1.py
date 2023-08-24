'''
Изучите API Геокодера Яндекса
tech.yandex.ru/maps/geocoder/doc/desc/concepts/input_params-docpage/
и получите ключ API для него в кабинете разработчика.
Выполните запрос к API и узнайте долготу точки на карте (Point) для города Самара.
'''
import requests
import json
request_headers={
    'Content-Type' : 'application/json',
    'Accept' : 'application/json; caharset=UTF-8'
}
url='https://geocode-maps.yandex.ru/1.x/?format=json&apikey=514dc5bd-ce7e-4dbe-a7cc-0eea96f46fc3&geocode=Самара'
response=requests.get(url,headers=request_headers)
print(response.status_code)
response=json.loads(response.content)
print(response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(" ")[0])