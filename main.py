from PySide2.QtWidgets import QMainWindow, QApplication
from mainwindow import MainWindow
import sys

app = QApplication()

window = MainWindow()
# window.setStyleSheet("background-color: #F5F0FF;")

window.show()

sys.exit(app.exec_())
