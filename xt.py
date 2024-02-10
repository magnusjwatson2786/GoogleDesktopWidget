from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui import *

import sys,requests,json,fake_useragent,concurrent.futures
ua=fake_useragent.UserAgent()
headers = {"user-agent": ua.firefox}
url1='https://google.com/complete/search?client=firefox&q='
url2='https://suggestqueries.google.com/complete/search?output=firefox&q='

class CompleterDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # Custom painting logic here
        item_text = index.data()
        # Set font size
        font = QFont(option.font)
        font.setPointSize(12)  # Font size 14
        painter.setFont(font)
        left, top, right, bottom = option.rect.getCoords()
        # Create a new QRect with the same left and top, but adjusted bottom for a height of 40
        new_rect = QRect(left, top, right, top + 40)
        #text_rect = option.rect#.marginsAdded(QMargins(-10,10,10,10));#.(adjusted(10,40,0,-40))
        #rectNew = painter.boundingRect(text_rect, Qt.AlignLeft, item_text).marginsAdded(QMargins(10,10,10,10))
        # painter.drawRect(text_rect)
        
        # Draw rounded rectangle on hover
        if option.state & QStyle.State_MouseOver:
            # painter.setBrush()
            painter.fillRect(new_rect, QColor(173, 216, 230))
            # painter.drawText(text_rect, Qt.AlignVCenter, item_text)

        painter.drawText(new_rect, Qt.AlignVCenter, item_text)
        # else:
        #     painter.setBrush(option.palette.color(QPalette.Window))
        
    # def paint(self, painter,option, index):
    #     # super(CompleterDelegate, self).initStyleOption(option, index)
    #     font = QFont(option.font)
    #     font.setPointSize(14)  # Adjust the font size as needed
    #     painter.setFont(font)
    #     # option.backgroundBrush = QColor("#f1f1f1")
    #     # option.palette.setBrush(QPalette.Text, QColor("blue"))
    #     # option.displayAlignment = Qt.AlignLeft
    #     painter.setRenderHint(QPainter.Antialiasing)
        
    #     # # Add left padding
    #     border_radius = 10  # Adjust the border radius as needed # Adjust the left padding as needed
    #     rect = option.rect.adjusted(5, 5, 0, 5)
    #     rect.setHeight(40)
    #     painter.drawRoundedRect(rect, border_radius, border_radius, mode=Qt.AbsoluteSize)
    #     item_text = index.data()
    #     # # Draw text with left padding
    #     # text_rect.setHeight(40)
    #     text_rect = option.rect.adjusted(10, 0, 0, 0)
    #     painter.drawText(text_rect, Qt.AlignVCenter, item_text)
    # def sizeHint(self, option, index):
    #     # Custom size hint logic here
    #     return QSize(100, 30)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.textChanged.connect(self.updatesuggest)
        # self.ui.listWidget.setVisible(False)  
        self.autosuggest_completer = QCompleter()
        self.autosuggest_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.delegate = CompleterDelegate(self.ui.lineEdit)
        self.autosuggest_completer.popup().setStyleSheet("height:200px;")
        self.autosuggest_completer.popup().setItemDelegate(self.delegate)
        self.ui.lineEdit.setCompleter(self.autosuggest_completer)
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.search_btn.clicked.connect(self.search)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setWindowOpacity(0.8)
        # self.set_window_position()
        # width,height = QGuiApplication().primaryScreen().size().toTuple()
        # window_width = self.frameGeometry().width()
        # window_height = self.frameGeometry().height()
        # x = (width - window_width) // 2
        # y = (2 * height) // 3 - window_height // 2
        # self.move(x, y)
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.frame.mouseMoveEvent = moveWindow
        self.show()

    def updatesuggest(self):
        rps= requests.get(url2+self.ui.lineEdit.text(), headers=headers, verify=False)
        sgs=json.loads(rps.text)
        # for i in sgs[1][:5]:
        #     self.ui.listWidget.addItem(i)
        model = QStringListModel()
        model.setStringList(sgs[1][:5])
        self.autosuggest_completer.setModel(model)

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
    sys.exit(app.exec())
        