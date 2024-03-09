#  C:/Python39/Lib/site-packages/PySide6/uic mainwindow.ui > ui_mainwindow.py -g python
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from ui_mainwindow import Ui_MainWindow
from syntax import parse_input, get_errors

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.run_button.clicked.connect(self.start_analysis)
        self.ui.clear_button.clicked.connect(self.clear_input)

    @Slot()
    def start_analysis(self):
        self.ui.output_text.clear()
        code = self.ui.input_text.toPlainText()
        result = parse_input(code)
        errors = get_errors()
        cursor = self.ui.output_text.textCursor()
        format = cursor.charFormat()

        if len(errors) > 0:
            format.setForeground(QColor(255, 0, 0))
            cursor.setCharFormat(format)
            cursor.insertText("ERROR:\n")

            format.setForeground(QColor(0, 0, 0))
            cursor.setCharFormat(format)
            for error in errors:
                cursor.insertText(error + '\n')            
        else:
            format.setForeground(QColor(0, 200, 0))
            cursor.setCharFormat(format)
            cursor.insertText("Análisis sintáctico exitoso:\n")

            format.setForeground(QColor(0, 0, 0))
            cursor.setCharFormat(format)
            cursor.insertText(self.format_ast(result))
        
        cursor.setPosition(0)
        self.ui.output_text.setTextCursor(cursor)

    @Slot()
    def clear_input(self):
        self.ui.input_text.clear()
        self.ui.output_text.setPlainText('<Esperando análisis...>')

    def format_ast(self, node, indent=0):
        result = ''
        if isinstance(node, tuple):
            result += '  ' * indent + f'<{node[0]}>\n'
            for child in node[1:]:
                result += self.format_ast(child, indent + 1)
        else:
            result += '  ' * (indent + 1) + f'{node}\n'
        return result