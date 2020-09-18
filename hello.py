import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My SUPER app")

        label = QLabel("this is a pyqt5 label")

        self.setCentralWidget(label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
