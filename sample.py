import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets

def window():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(100, 100, 300, 200)
    window.setWindowTitle('My PyQt5 Application')

    label = QtWidgets.QLabel(window)
    label.setText('Hello World!')
    label.move(110, 85)

    window.show()
    sys.exit(app.exec_())

window()
