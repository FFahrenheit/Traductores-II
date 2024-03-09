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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 465)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
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

        self.gridLayout_2.addWidget(self.clear_button, 2, 1, 1, 1)

        self.run_button = QPushButton(self.groupBox)
        self.run_button.setObjectName(u"run_button")

        self.gridLayout_2.addWidget(self.run_button, 2, 0, 1, 1)

        self.input_text = QPlainTextEdit(self.groupBox)
        self.input_text.setObjectName(u"input_text")
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.input_text.setFont(font)

        self.gridLayout_2.addWidget(self.input_text, 1, 0, 1, 1)

        self.output_text = QPlainTextEdit(self.groupBox)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setEnabled(True)
        self.output_text.setFont(font)
        self.output_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.output_text.setReadOnly(True)

        self.gridLayout_2.addWidget(self.output_text, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 810, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Analizador sem\u00e1ntico", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
        self.input_text.setPlainText(QCoreApplication.translate("MainWindow", u"suma = 1 + 2;\n"
"resta = 1 - 2;\n"
"multiplicacion = 3 * 4;\n"
"resultado = suma + multiplicacion;", None))
        self.output_text.setPlainText(QCoreApplication.translate("MainWindow", u"<Esperando an\u00e1lisis...>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

