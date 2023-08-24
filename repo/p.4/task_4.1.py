'''
Используя данные по посещаемости библиотек в районах Москвы
https://video.ittensive.com/python-advanced/data-7361-2019-11-28.utf.json
постройте круговую диаграмму суммарной посещаемости (NumOfVisitors) 20 наиболее популярных районов Москвы.
Создайте PDF отчет, используя файл
https://video.ittensive.com/python-advanced/title.pdf
как первую страницу. На второй странице выведите итоговую диаграмму, самый популярный район Москвы и число посетителей библиотек в нем.
'''
# pyPDF2 / pyMuPDF (fitz) / ReportLab / PyFPDF: data -> PDF
# pdfminer / pdfminer.six / pdfquery: PDF -> data
# pyhtmldoc / xhtml2pdf / pdfkit: (data ->) HTML -> PDF
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

PDF = canvas.Canvas("title.pdf", pagesize = pagesizes.A4)
print (PDF.getAvailableFonts())
pdfmetrics.registerFont(TTFont("Trebuchet", "Trebuchet.ttf"))
PDF.setFont("Trebuchet", 13)
PDF.drawString(30, 820, "ITtensive/")
PDF.drawString(197, 820, "Python PDF")
PDF.drawString(430, 20, "от команды ITtensive")
PDF.drawString(550, 820, "1")
PDF.setFont("Trebuchet", 48)
PDF.drawString(180, 550, "Культурная")
PDF.drawString(185, 490, "статистика")
PDF.drawString(215, 430, "Москвы")
PDF.save()