# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basemNeVdA.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(803, 295)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setStyleSheet(u"QLineEdit {\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: #f1f1f1;\n"
"border: 1px solid #d1d1d1;\n"
"padding: 8px;\n"
"border-radius: 16px;  /* Adjust the border-radius to make it more or less rounded */\n"
"}\n"
"QLineEdit:focus {\n"
"border: 2px solid #4285f4;\n"
"}\n"
"QPushButton {\n"
"font: 12pt \"Segoe UI\";\n"
"background-color: white;\n"
"color: #4285f4;\n"
"padding: 8px;\n"
"border: none;\n"
"border-radius: 16px;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover {\n"
"border: 2px solid #3a77c7;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setStyleSheet(u"QPushButton {\n"
"background-color: #4285f4;\n"
"color: white;\n"
"padding: 8px;\n"
"border: none;\n"
"border-radius: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #3a77c7;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.search_btn = QPushButton(self.frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(32, 32))
        self.search_btn.setMaximumSize(QSize(40, 40))
        self.search_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.search_btn.setStyleSheet(u"image: url(:/icons/icons/cil-magnifying-glass.png);\n"
"")
        self.search_btn.setText(u"")
        self.search_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.search_btn)

        self.close_btn = QPushButton(self.frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(32, 32))
        self.close_btn.setMaximumSize(QSize(40, 40))
        self.close_btn.setContextMenuPolicy(Qt.NoContextMenu)
        self.close_btn.setStyleSheet(u"QPushButton{image: url(:/icons/icons/icon_close.png);}\n"
"QPushButton:hover {\n"
"	background-color:#e92d18; ; \n"
"}\n"
"\\\n"
"")

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QuickGoogle", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Google", None))
#if QT_CONFIG(shortcut)
        self.search_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.close_btn.setText("")
#if QT_CONFIG(shortcut)
        self.close_btn.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

