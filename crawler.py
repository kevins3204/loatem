import requests
import sys
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, QDate, Qt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('로아템')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.lbl = QLabel(self)
        self.lbl.move(100, 100)
        self.name = ''

        self.qle = QLineEdit(self)
        self.qle.move(60, 40)
        # qle.textChanged[str].connect(self.onChanged)

        lbl = QLabel('템렙 : ', self)
        lbl.move(60, 93)
        btn1 = QPushButton('찾기', self)
        btn1.move(180, 40)
        btn2 = QPushButton('Quit', self)
        btn2.move(180, 100)
        btn1.clicked.connect(self.crawl)
        btn2.clicked.connect(QCoreApplication.instance().quit)
        
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text): 
        # print(type(self.lbl.text()))
        self.lbl.setText(text)
        self.lbl.adjustSize()
    
    def crawl(self):
        self.name = self.qle.text()
        # print(self.name)
        url = 'https://loahae.com/profile/' + self.name
        # print(url)
        src = requests.get(url)
        p_txt = src.text
        soup = BeautifulSoup(p_txt, 'html.parser')
        item_lvl = str(soup.select('body > div.c-content.c-max-w > div.s-profile > div.profile-info > div.b2 > div:nth-child(3) > span')).replace('</span>]','').replace('[<span>','')
        self.lbl.setText(item_lvl)
        self.lbl.adjustSize()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())