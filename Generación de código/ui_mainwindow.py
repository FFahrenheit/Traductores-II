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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(959, 647)
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
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.clear_button = QPushButton(self.groupBox)
        self.clear_button.setObjectName(u"clear_button")

        self.gridLayout.addWidget(self.clear_button, 4, 1, 1, 1)

        self.run_button = QPushButton(self.groupBox)
        self.run_button.setObjectName(u"run_button")

        self.gridLayout.addWidget(self.run_button, 4, 0, 1, 1)

        self.symbol_table = QTableWidget(self.groupBox)
        if (self.symbol_table.columnCount() < 3):
            self.symbol_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.symbol_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.symbol_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.symbol_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.symbol_table.setObjectName(u"symbol_table")
        self.symbol_table.setEnabled(False)

        self.gridLayout.addWidget(self.symbol_table, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.asm_text = QPlainTextEdit(self.groupBox)
        self.asm_text.setObjectName(u"asm_text")
        self.asm_text.setFont(font)

        self.gridLayout.addWidget(self.asm_text, 3, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.input_text = QPlainTextEdit(self.groupBox)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setFont(font)

        self.gridLayout.addWidget(self.input_text, 1, 0, 1, 2)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.output_text = QPlainTextEdit(self.groupBox)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setEnabled(True)
        self.output_text.setFont(font)
        self.output_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.output_text.setReadOnly(True)

        self.gridLayout.addWidget(self.output_text, 1, 2, 3, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 22))
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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Generaci\u00f3n de c\u00f3digo", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"Compilar", None))
        ___qtablewidgetitem = self.symbol_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"S\u00edmbolo", None));
        ___qtablewidgetitem1 = self.symbol_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem2 = self.symbol_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tabla de s\u00edmbolos", None))
        self.asm_text.setPlainText(QCoreApplication.translate("MainWindow", u"<Esperando compilaci\u00f3n...>\n"
"", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pseudoensamblador", None))
        self.input_text.setPlainText(QCoreApplication.translate("MainWindow", u"suma = 1 + 2;\n"
"resta = 1 - 2;\n"
"multiplicacion = 3 * 4;\n"
"resultado = suma + multiplicacion;", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00c1rbol sint\u00e1ctico", None))
        self.output_text.setPlainText(QCoreApplication.translate("MainWindow", u"<Esperando an\u00e1lisis...>", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

