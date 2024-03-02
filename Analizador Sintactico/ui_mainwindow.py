# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 404)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.clear_button = QPushButton(self.groupBox)
        self.clear_button.setObjectName(u"clear_button")

        self.gridLayout_2.addWidget(self.clear_button, 1, 1, 1, 1)

        self.run_button = QPushButton(self.groupBox)
        self.run_button.setObjectName(u"run_button")

        self.gridLayout_2.addWidget(self.run_button, 1, 0, 1, 1)

        self.input_text = QPlainTextEdit(self.groupBox)
        self.input_text.setObjectName(u"input_text")
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.input_text.setFont(font)

        self.gridLayout_2.addWidget(self.input_text, 0, 0, 1, 1)

        self.output_text = QPlainTextEdit(self.groupBox)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setEnabled(True)
        self.output_text.setFont(font)
        self.output_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.output_text.setReadOnly(True)

        self.gridLayout_2.addWidget(self.output_text, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Analizador sint\u00e1ctico", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
        self.input_text.setPlainText(QCoreApplication.translate("MainWindow", u"suma = 1 + 2;\n"
"resta = 1 - 2;\n"
"multiplicacion = 3 * 4;\n"
"resultado = suma + multiplicacion;", None))
        self.output_text.setPlainText(QCoreApplication.translate("MainWindow", u"<Esperando an\u00e1lisis>", None))
    # retranslateUi

