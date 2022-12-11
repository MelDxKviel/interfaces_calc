from PyQt6.QtWidgets import QWidget

from ui import quadratic_ui


class QuadraticWindow(QWidget, quadratic_ui.Ui_QuadraticWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.btn_calc.clicked.connect(self.calc)

    def closeEvent(self, event):
        self.parent.window().setEnabled(True)
        event.accept()

    def calc(self):
        self.label_x2.setText("")
        self.label_x1.setText("")
        try:
            a = float(self.line_a.text())
            b = float(self.line_b.text())
            c = float(self.line_c.text())

            if a == 0:
                self.label_x1.setText("Не квадратное уравнение")
                return

            d = b ** 2 - 4 * a * c
            if d > 0:
                x1 = (-b + d ** 0.5) / (2 * a)
                x2 = (-b - d ** 0.5) / (2 * a)
                self.label_x1.setText(f"x1 = {x1:.2f}")
                self.label_x2.setText(f"x2 = {x2:.2f}")
            elif d == 0:
                x = -b / (2 * a)
                self.label_x1.setText(f"x = {x:.2f}")
            else:
                self.label_x1.setText("Нет корней")
        except ValueError:
            self.label_x1.setText("Ошибка!")
