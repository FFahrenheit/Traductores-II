#  C:/Python39/Lib/site-packages/PySide6/uic mainwindow.ui > ui_mainwindow.py -g python
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from syntax import parse_input, get_errors

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.run_button.clicked.connect(self.start_analysis)

    @Slot()
    def start_analysis(self):
        code = self.ui.input_text.toPlainText()
        result = parse_input(code)
        if result is None:
            errors = get_errors()
            print(errors)
            return
        
        self.ui.output_text.setPlainText(str(result))

    @Slot()
    def clear_input(self):
        self.ui.input_text.clear()
        self.ui.output_text.setPlainText('<Esperando análisis>')