from widgets.quadratic import QuadraticWindow


def test_window_is_visible(qtbot):
    window = QuadraticWindow()
    qtbot.addWidget(window)
    window.show()
    assert window.isVisible()


class TestQuadratic:
    def setup_method(self):
        self.window = QuadraticWindow()
        self.window.show()

    def test_quadratic_two_roots(self, qtbot):
        self.window.line_a.setText("1")
        self.window.line_b.setText("5")
        self.window.line_c.setText("6")
        self.window.btn_calc.click()

        assert self.window.label_x1.text() == "x1 = -2.00"
        assert self.window.label_x2.text() == "x2 = -3.00"

    def test_quadratic_one_root(self, qtbot):
        self.window.line_a.setText("1")
        self.window.line_b.setText("2")
        self.window.line_c.setText("1")
        self.window.btn_calc.click()

        assert self.window.label_x1.text() == "x = -1.00"

    def test_quadratic_no_roots(self, qtbot):
        self.window.line_a.setText("1")
        self.window.line_b.setText("2")
        self.window.line_c.setText("3")
        self.window.btn_calc.click()

        assert self.window.label_x1.text() == "Нет корней"

    def test_quadratic_error(self, qtbot):
        self.window.line_a.setText("a")
        self.window.line_b.setText("2")
        self.window.line_c.setText("3")
        self.window.btn_calc.click()

        assert self.window.label_x1.text() == "Ошибка!"

    def test_quadratic_error2(self, qtbot):
        self.window.line_a.setText("1")
        self.window.line_b.setText("a")
        self.window.line_c.setText("3")
        self.window.btn_calc.click()

        assert self.window.label_x1.text() == "Ошибка!"

    def test_quadratic_error3(self, qtbot):
        self.window.line_a.setText("1")
        self.window.line_b.setText("2")
        self.window.line_c.setText("a")
        self.window.btn_calc.click()

        assert self.window.label_x1.text() == "Ошибка!"

    def test_quadratic_error_not_input(self, qtbot):
        self.window.btn_calc.click()

        assert self.window.label_x1.text() == "Ошибка!"

    def test_not_quadratic(self):
        self.window.line_a.setText("0")
        self.window.line_b.setText("2")
        self.window.line_c.setText("3")
        self.window.btn_calc.click()

        assert self.window.label_x1.text() == "Не квадратное уравнение"
