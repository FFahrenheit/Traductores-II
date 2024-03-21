#  C:/Python39/Lib/site-packages/PySide6/uic mainwindow.ui > ui_mainwindow.py -g python
from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from ui_mainwindow import Ui_MainWindow
from syntax import parse_input, get_errors, get_symbol_table

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.run_button.clicked.connect(self.start_analysis)
        self.ui.clear_button.clicked.connect(self.clear_input)

        self.ui.actionAbrir.triggered.connect(self.open_file)
        self.ui.actionGuardar.triggered.connect(self.save_file)
        self.errors = []
        self.symbol_table = {}

    @Slot()
    def save_file(self):
        path = QFileDialog.getSaveFileName(
            self,
            'Guardar archivo',
            './examples',
            'Text Files (*.txt)'
        )[0]

        with open(path, 'w') as file:
            file.write(self.ui.input_text.toPlainText())

    @Slot()
    def open_file(self):
        path = QFileDialog.getOpenFileName(
            self,
            "Abrir archivo",
            "./examples",
            "Text Files (*.txt);;All Files (*)"
        )[0]

        with open(path, 'r') as file:
            self.ui.input_text.setPlainText(file.read())

    @Slot()
    def start_analysis(self):
        self.ui.output_text.clear()
        self.ui.symbol_table.clearContents()
        self.ui.symbol_table.setRowCount(0)
        code = self.ui.input_text.toPlainText()
        result = parse_input(code)
        self.errors = get_errors()
        cursor = self.ui.output_text.textCursor()
        format = cursor.charFormat()

        if len(self.errors) > 0:
            format.setForeground(QColor(255, 0, 0))
            cursor.setCharFormat(format)
            cursor.insertText("ERROR:\n")

            format.setForeground(QColor(0, 0, 0))
            cursor.setCharFormat(format)
            for error in self.errors:
                cursor.insertText(error + '\n')
            cursor.setPosition(0)
            self.ui.output_text.setTextCursor(cursor)
            return
        
        format.setForeground(QColor(0, 200, 0))
        cursor.setCharFormat(format)
        cursor.insertText("Compilación exitosa:\n")
        format.setForeground(QColor(0, 0, 0))
        cursor.setCharFormat(format)
        tree = self.format_ast(result)
        cursor.insertText(tree)
        cursor.setPosition(0)
        self.ui.output_text.setTextCursor(cursor)

        # Evaluation
        self.symbol_table = get_symbol_table()
        self.evaluate_symbol_table(result)
        for error in self.errors:
            self.print_error("Error de ejecución", error)
        
        self.ui.symbol_table.setRowCount(len(self.symbol_table.keys()))
        for index, key in enumerate(self.symbol_table.keys()):
            self.ui.symbol_table.setItem(index, 0, QTableWidgetItem(key))
            self.ui.symbol_table.setItem(index, 1, QTableWidgetItem(str(self.symbol_table[key])))

    @Slot()
    def clear_input(self):
        self.ui.input_text.clear()
        self.ui.output_text.setPlainText('<Esperando análisis...>')
        self.ui.symbol_table.clearContents()
        self.ui.symbol_table.setRowCount(0)

    def format_ast(self, node, indent=0):
        result = ''
        if isinstance(node, tuple):
            result += '  ' * indent + f'<{node[0]}>\n'
            for child in node[1:]:
                result += self.format_ast(child, indent + 1)
        else:
            result += '  ' * (indent + 1) + f'{node}\n'
        return result
    
    def evaluate_symbol_table(self, node):
        if isinstance(node, tuple):
            if node[0] == 'program':
                for statement in node[1:]:
                    self.evaluate_symbol_table(statement)
            elif node[0] == 'assignment':
                variable_name = node[1]
                expression = node[2]
                value = self.evaluate_tree(expression)
                if value is not None:
                    self.symbol_table[variable_name] = value
                else:
                    self.errors.append(f"Error al evaluar la expresión para la variable '{variable_name}'")
        else:
            self.errors.append(f"Error semántico: Nodo de programa inválido {node}")
    
    def evaluate_tree(self, node):
        if isinstance(node, tuple):
            if node[0] == 'number':
                return node[1]
            elif node[0] == 'identifier':
                # Verificar si la variable está definida
                if node[1] not in self.symbol_table:
                    self.errors.append(f"Error semántico: Variable '{node[1]}' no está definida")
                    return None
                return self.symbol_table[node[1]]
            elif node[0] == 'binop':
                left_value = self.evaluate_tree(node[2])
                right_value = self.evaluate_tree(node[3])
                if left_value is None or right_value is None:
                    return None
                if node[1] == '+':
                    return left_value + right_value
                elif node[1] == '-':
                    return left_value - right_value
                elif node[1] == '*':
                    return left_value * right_value
                elif node[1] == '/':
                    if right_value == 0:
                        self.errors.append("Error semántico: División por cero")
                        return None
                    return left_value / right_value
            else:
                self.errors.append("Error semántico: Tipo de nodo desconocido")
                return None
        else:
            self.errors.append("Error semántico: Nodo inválido")
            return None

    def print_error(self, title, message):
        QMessageBox.critical(self, title, message)