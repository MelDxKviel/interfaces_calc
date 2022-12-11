from PyQt6.QtWidgets import QApplication, QMainWindow

import sys

from ui import main_ui
from widgets.sum_div import SumDivWindow
from widgets.distance import DistanceWindow
from widgets.quadratic import QuadraticWindow


class MainWindow(QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setupUi(self)
        self.sum_div.clicked.connect(self.sum_div_clicked)
        self.dist.clicked.connect(self.distance_clicked)
        self.quadratic.clicked.connect(self.quadratic_clicked)
        self.sum_div_window = SumDivWindow(parent=self)
        self.distance_window = DistanceWindow(parent=self)
        self.quadratic_window = QuadraticWindow(parent=self)

    def sum_div_clicked(self):
        self.sum_div_window.show()
        self.window().setEnabled(False)

    def distance_clicked(self):
        self.distance_window.show()
        self.window().setEnabled(False)

    def quadratic_clicked(self):
        self.quadratic_window.show()
        self.window().setEnabled(False)

    def closeEvent(self, event):
        self.sum_div_window.close()
        self.distance_window.close()
        self.quadratic_window.close()
        event.accept()


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
