import sys
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPageLayout, QPageSize
from PyQt5.QtWidgets import QApplication

a = 'https://www.fontanka.ru/24hours_news.html'
b = 'https://habr.com/ru/'
c = 'https://ria.ru/'
d = 'https://www.autonews.ru/'
e = 'https://iz.ru/'

f = 'https://www.bloomberg.com/europe'
g = 'https://www.bbc.com/news'
h = 'https://tvnews.vanderbilt.edu/explore_category?category=weather'
i = 'https://www.foxnews.com/'
j = 'https://www.sbs.com.au/news/'

massive = [a,b,c,d,e,f,g,h,i,j]

print('You can choose one from 10 web pages of news / or select 10 to specify'
      '')
print('Russian:\n'
      '0 - fontanka\n'
      '1 - habrahabr\n'
      '2 - RIA\n'
      '3 - autonews\n'
      '4 - izdaniya\n'
      'Worldwide:\n'
      '5 - bloomberg news\n'
      '6 - bbc news\n'
      '7 - tvnews\n'
      '8 - foxnews\n'
      '9 - sbs news')
g = input()
if g == '10':
      source = input()
else:
      source = massive[int(g)]

app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()
loader.setZoomFactor(1)
layout = QPageLayout()
layout.setPageSize(QPageSize(QPageSize.A4Extra))
layout.setOrientation(QPageLayout.Portrait)
loader.load(QUrl(source))
loader.page().pdfPrintingFinished.connect(lambda *args: QApplication.exit())

def emit_pdf(finished):
        loader.page().printToPdf("news.pdf", pageLayout=layout)
        print('Open news.pdf file')

loader.loadFinished.connect(emit_pdf)
print('Done')
sys.exit(app.exec_())

