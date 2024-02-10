# from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui import *

class CompleterDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(CompleterDelegate, self).initStyleOption(option, index)
        option.backgroundBrush = QColor("red")
        option.palette.setBrush(QPalette.Text, QColor("blue"))
        option.displayAlignment = Qt.AlignCenter

class Principal(QMainWindow):
    def __init__(self):
        super(Principal, self).__init__()
        # loadUi("uno.ui",self)
        completer = QCompleter(self)
        self.lineEdit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        delegate = CompleterDelegate(self.lineEdit)
        completer.popup().setStyleSheet("background-color:red;")
        completer.popup().setItemDelegate(delegate)
        self.get_data(model)

    def get_data(self,model):
        model.setStringList(["uno","dos","tres","cuatro","este es mi nombre"])

if __name__ == '__main__':
    import sys
    app  = QApplication(sys.argv)
    p = Principal()
    p.show()
    sys.exit(app.exec_())