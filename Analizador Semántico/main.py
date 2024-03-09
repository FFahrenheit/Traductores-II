from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

if __name__ == '__main__':
    # Crear aplicación QT
    app = QApplication()
    # Crear ventana
    window = MainWindow()
    window.setWindowTitle("Analizador sintáctico")
    # Se hace visible
    window.show()
    # Qt loop
    sys.exit(app.exec())