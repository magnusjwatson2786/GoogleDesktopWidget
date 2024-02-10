from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui import *

import sys,requests,json,fake_useragent,concurrent.futures
ua=fake_useragent.UserAgent()
headers = {"user-agent": ua.firefox}
url1='https://google.com/complete/search?client=firefox&q='
url2='https://suggestqueries.google.com/complete/search?output=firefox&q='

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.textChanged.connect(self.updatesuggest)
        # self.ui.listWidget.setVisible(False)  
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.search_btn.clicked.connect(self.search)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.listmodel = QStandardItemModel()
        self.ui.listView.setModel(self.listmodel)

    def updatesuggest(self):
        self.listmodel.clear()
        rps= requests.get(url2+self.ui.lineEdit.text(), headers=headers, verify=False)
        sgs=json.loads(rps.text)
        for i in sgs[1][:5]:
            item = QStandardItem(i)
            self.listmodel.appendRow(item)

    def search(self):
        url = QUrl("https://www.google.com/search?q="+self.ui.lineEdit.text())
        QDesktopServices.openUrl(url)
        self.resetSearchBar()

    def resetSearchBar(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setPlaceholderText('Google')

    def handleExit(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    width,height = app.primaryScreen().size().toTuple()
    window = MainWindow()
    window_width = window.frameGeometry().width()
    window_height = window.frameGeometry().height()
    x = (width - window_width) // 2
    y = (height-window_height)* 1//4
    window.move(x, y)
    window.show()
    sys.exit(app.exec())
        