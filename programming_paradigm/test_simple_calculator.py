class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method of the calculator."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Basic positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Positive + Negative
        self.assertEqual(self.calc.add(-5, -3), -8)  # Negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)  # Edge case with zero

    def test_subtraction(self):
        """Test the subtract method of the calculator."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Basic positive numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)  # Negative - Positive
        self.assertEqual(self.calc.subtract(-5, -3), -2)  # Negative numbers
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Edge case with zero

    def test_multiplication(self):
        """Test the multiply method of the calculator."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Basic multiplication
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # Negative * Positive
        self.assertEqual(self.calc.multiply(-5, -3), 15)  # Negative * Negative
        self.assertEqual(self.calc.multiply(0, 100), 0)  # Edge case with zero

    def test_division(self):
        """Test the divide method of the calculator."""
        self.assertEqual(self.calc.divide(6, 3), 2)  # Basic division
        self.assertEqual(self.calc.divide(-6, 3), -2)  # Negative / Positive
        self.assertEqual(self.calc.divide(-6, -3), 2)  # Negative / Negative
        self.assertEqual(self.calc.divide(0, 1), 0)  # Zero divided by a number
        self.assertIsNone(self.calc.divide(1, 0))  # Division by zero case

if __name__ == '__main__':
    unittest.main()
