from PyQt6.QtWidgets import QWidget

from ui import distance_ui


class DistanceWindow(QWidget, distance_ui.Ui_DistanceWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_calc.clicked.connect(self.calc)

    def closeEvent(self, event):
        self.parent.window().setEnabled(True)
        event.accept()

    def calc(self):
        try:
            xx = (float(self.line_x2.text()) - float(self.line_x1.text()))**2
            yy = (float(self.line_y2.text()) - float(self.line_y1.text()))**2
            dist = (xx + yy)**0.5
            self.label_result.setText(f"{dist:.2f}")
        except ValueError:
            self.label_result.setText("Ошибка!")
