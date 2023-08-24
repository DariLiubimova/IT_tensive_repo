'''Используя данные по посещаемости библиотек в районах Москвы
https://video.ittensive.com/python-advanced/data-7361-2019-11-28.utf.json
постройте круговую диаграмму суммарной посещаемости (NumOfVisitors) 20 наиболее популярных районов Москвы.
Создайте PDF отчет, используя файл
https://video.ittensive.com/python-advanced/title.pdf
как первую страницу. На второй странице выведите итоговую диаграмму, самый популярный район Москвы и число посетителей библиотек в нем.'''
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
import seaborn as sns
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfMerger, PdfReader
from PIL import Image

def extract_district (x):
    return list(map(lambda a: a["District"], x))[0]

#обработка данных
url='https://video.ittensive.com/python-advanced/data-7361-2019-11-28.utf.json'
response=requests.get(url)
print(response.status_code)
response=json.loads(response.content)
data=pd.DataFrame(response, columns=['NumOfVisitors','ObjectAddress']).fillna(value=0)
data['ObjectAddress']=data['ObjectAddress'].apply(extract_district)
data=data.rename(columns={'ObjectAddress':'District'})
data=data.groupby("District").sum().sort_values(by='NumOfVisitors', ascending=False)
datapop=data.iloc[:20]
print(datapop)

#построение круговой диаграммы

fig = plt.figure(figsize=(10,2))
area = fig.add_subplot(1, 1, 1)
colors = sns.color_palette('pastel')[ 0:20 ]
datapop[0:20]["NumOfVisitors"].plot.pie(ax = area, labels=[""]*20, label="Посещаемость", colors=colors)
plt.legend(datapop[0:20].index, bbox_to_anchor=(1.5,1,0.1,0))
plt.savefig('libraries.png')
plt.show()


#создание pdf
pdfmetrics.registerFont(TTFont('Trebuchet', 'Trebuchet.ttf'))
PDF = canvas.Canvas("libraries.pdf", pagesize=pagesizes.A4)
PDF.setFont("Trebuchet", 30)
PDF.drawString(60, 750, "Популярные районы Москвы ")
PDF.drawString(60, 650, "по числу посетителей библиотек")
PDF.setFont("Trebuchet", 13)
PDF.drawString(550, 820, "2")
PDF.drawImage(ImageReader("libraries.png"), -300, 200)

PDF.setFont("Trebuchet", 20)
PDF.drawString(100, 150, "Самый популярный район")
PDF.setFont("Trebuchet", 24)
PDF.drawString(100, 120, datapop.index[0])
PDF.setFont("Trebuchet", 20)
PDF.drawString(100, 90, "Посетителей: " + str(int(datapop["NumOfVisitors"].values[0])))
PDF.save()

#объединение pdf

files = ["title.pdf", "libraries.pdf"]
merger = PdfMerger()
for filename in files:
    merger.append(PdfReader(open(filename, "rb")))
merger.add_metadata({
    '/Producer': "ITtensive",
    '/Author': "Daria_L",
    '/Creator': "ITtensive Python Advanced - www.ittensive.com",
    '/Copyright': "ITtensive 2023",
    '/Title': "Культурная статистика Москвы"
})
merger.write("report.pdf")
