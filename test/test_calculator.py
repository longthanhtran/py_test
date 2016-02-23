from lib.calculator import Calculator

def test_calculator_add_method_returns_correct_result():
    calc = Calculator()
    result = calc.add(2,2)
    assert result == 4

# def test_calculator_rejects_if_arguments_is_not_numeric():
#     calc = Calculator()
#     self.assertEqual()

# if __name__ == '__main__':
#     unittest.main()
