from widgets.sum_div import SumDivWindow


def test_window_is_visible(qtbot):
    window = SumDivWindow()
    qtbot.addWidget(window)
    window.show()
    assert window.isVisible()


class TestSum:
    def setup_method(self):
        self.window = SumDivWindow()
        self.window.show()

    def test_sum(self, qtbot):
        self.window.line_firstNum.setText("1")
        self.window.line_secondNum.setText("2")
        self.window.rad_sum.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "3.0"

    def test_sum_error(self, qtbot):
        self.window.line_firstNum.setText("1")
        self.window.line_secondNum.setText("ф")
        self.window.rad_sum.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"

    def test_sum_error2(self, qtbot):
        self.window.line_firstNum.setText("a")
        self.window.line_secondNum.setText("0")
        self.window.rad_sum.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"

    def test_sum_not_input(self, qtbot):
        self.window.rad_div.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"


class TestDiv:
    def setup_method(self):
        self.window = SumDivWindow()
        self.window.show()

    def test_div(self, qtbot):
        self.window.line_firstNum.setText("1")
        self.window.line_secondNum.setText("2")
        self.window.rad_div.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "0.50"

    def test_div2(self, qtbot):
        self.window.line_firstNum.setText("5")
        self.window.line_secondNum.setText("0.5")
        self.window.rad_div.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "10.00"

    def test_div_not_zero(self, qtbot):
        self.window.line_firstNum.setText("1")
        self.window.line_secondNum.setText("2")
        self.window.rad_div.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() != "Ошибка!"

    def test_div_error(self, qtbot):
        self.window.line_firstNum.setText("1")
        self.window.line_secondNum.setText("ф")
        self.window.rad_div.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"

    def test_div_zero_division(self, qtbot):
        self.window.line_firstNum.setText("1")
        self.window.line_secondNum.setText("0")
        self.window.rad_div.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"

    def test_div_not_input(self, qtbot):
        self.window.rad_div.setChecked(True)
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"
