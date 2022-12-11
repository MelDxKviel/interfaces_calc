from PyQt6.QtWidgets import QWidget

from ui import sum_div_ui


class SumDivWindow(QWidget, sum_div_ui.Ui_SumDivWindow):
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
            if self.rad_sum.isChecked():
                self.label_result.setText(f"{float(self.line_firstNum.text()) + float(self.line_secondNum.text())}")
            elif self.rad_div.isChecked():
                self.label_result.setText(
                    f"{(float(self.line_firstNum.text()) / float(self.line_secondNum.text())):.2f}")
        except (ValueError, ZeroDivisionError):
            self.label_result.setText("Ошибка!")
