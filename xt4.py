from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import shiboken6
from ui import *

import sys,requests,json,fake_useragent,concurrent.futures
if sys.platform == 'win32':
    import ctypes
    HWND_BOTTOM = 1
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
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.search_btn.clicked.connect(self.search)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.clearsuggest()
        # ctypes.windll.user32.SetWindowPos(self.winId(), HWND_BOTTOM, 0, 0, 0, 0, 0x3)
        current_flags = self.windowFlags()
        self.setWindowFlags(current_flags | Qt.Tool | Qt.WindowStaysOnBottomHint)

    def clearsuggest(self):
        for i in reversed(range(self.ui.verticalLayout_2.count())):
            widget = self.ui.verticalLayout_2.itemAt(i).widget()
            if widget:
                shiboken6.delete(widget)

    def updatesuggest(self):
        rps= requests.get(url2+self.ui.lineEdit.text(), headers=headers, verify=False)
        sgs=json.loads(rps.text)
        self.clearsuggest()

        for i in sgs[1][:5]:
            button = QPushButton(i)
            button.clicked.connect(self.selectsuggest)
            self.ui.verticalLayout_2.addWidget(button)
    
    def selectsuggest(self):
        btn = self.sender()
        self.ui.lineEdit.setText(btn.text())

    def search(self):
        url = QUrl("https://www.google.com/search?q="+self.ui.lineEdit.text())
        QDesktopServices.openUrl(url)
        self.resetSearchBar()
        
    def resetSearchBar(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setPlaceholderText('Google')

    # def changeEvent(self, event):
    #     if event.type() == QEvent.WindowStateChange:
    #         print(self.windowState())
    #         if event.oldState() and Qt.WindowMinimized:
    #             print("WindowMinimized")
    #         elif event.oldState() == Qt.WindowNoState or self.windowState() == Qt.WindowMaximized:
    #             print("WindowMaximized")


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
    window.lower()
    sys.exit(app.exec())
        