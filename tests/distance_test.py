from widgets.distance import DistanceWindow


def test_window_is_visible(qtbot):
    window = DistanceWindow()
    qtbot.addWidget(window)
    window.show()
    assert window.isVisible()


class TestDistance:
    def setup_method(self):
        self.window = DistanceWindow()
        self.window.show()

    def test_distance(self, qtbot):
        self.window.line_x1.setText("1")
        self.window.line_y1.setText("2")
        self.window.line_x2.setText("3")
        self.window.line_y2.setText("4")
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "2.83"

    def test_distance_error(self, qtbot):
        self.window.line_x1.setText("1")
        self.window.line_y1.setText("ф")
        self.window.line_x2.setText("3")
        self.window.line_y2.setText("4")
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"

    def test_distance_error2(self, qtbot):
        self.window.line_x1.setText("a")
        self.window.line_y1.setText("2")
        self.window.line_x2.setText("3")
        self.window.line_y2.setText("4")
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"

    def test_distance_error4(self, qtbot):
        self.window.line_x1.setText("1")
        self.window.line_y1.setText("2")
        self.window.line_x2.setText("3")
        self.window.line_y2.setText("a")
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"

    def test_distance_error_not_input(self, qtbot):
        self.window.btn_calc.click()

        assert self.window.label_result.text() == "Ошибка!"
