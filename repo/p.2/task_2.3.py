'''
Используя парсинг данных с маркетплейса beru.ru, найдите, на сколько литров
 отличается общий объем холодильников Саратов 263 и Саратов 452?
 Для парсинга можно использовать зеркало страницы beru.ru с результатами для холодильников Саратов
  по адресу: video.ittensive.com/data/018-python-advanced/beru.ru/
'''
import requests
from bs4 import BeautifulSoup
headers={"User-Agent": "ittensive-python-course/1.0 (+http://ittensive.com)"}
r=requests.get('https://video.ittensive.com/data/018-python-advanced/beru.ru/', headers=headers)
html=BeautifulSoup(r.content)
print(html)
links=html.find_all("a", {"class": "grid-snippet__react-link"})
print(links)
link_263=''
link_452=''
for link in links:
    if str(link).find('Саратов 263')>-1:
        print('hello')
        link_263=link['href']
    if str(link).find('Саратов 452')>-1:
        link_452=link['href']
if link_263 and link_452:
    r=requests.get('https://video.ittensive.com/data/018-python-advanced/beru.ru/' + link_263)
    html=BeautifulSoup(r.content)
    volume=html.find_all('span', {'class:' "_112Tad-7AP"})
    volume=volume[2].get_text()
    print(volume)
