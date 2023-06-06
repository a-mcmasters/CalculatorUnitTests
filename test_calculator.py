import unittest, math
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(123456, 543210), 666666)
        self.assertEqual(self.calc.add(0, 0), 0)

        with self.assertRaises(TypeError):
            self.calc.add("1", 2)
        with self.assertRaises(TypeError):
            self.calc.add(2, "1")
        with self.assertRaises(TypeError):
            self.calc.add(2, "a")
        with self.assertRaises(TypeError):
            self.calc.add('%', 1)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)

        with self.assertRaises(TypeError):
            self.calc.subtract("1", 2)
        with self.assertRaises(TypeError):
            self.calc.subtract(2, "1")
        with self.assertRaises(TypeError):
            self.calc.subtract(2, "a")
        with self.assertRaises(TypeError):
            self.calc.subtract('%', 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(0.1, 100), 10)

        with self.assertRaises(TypeError):
            self.calc.multiply("1", 2)
        with self.assertRaises(TypeError):
            self.calc.multiply(2, "1")
        with self.assertRaises(TypeError):
            self.calc.multiply(2, "a")
        with self.assertRaises(TypeError):
            self.calc.multiply('%', 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        self.assertEqual(self.calc.divide(0, 100), 0)
        self.assertEqual(self.calc.divide(2, -2), -1)
        self.assertEqual(self.calc.divide(2, -0.2), -10)

        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

        with self.assertRaises(TypeError):
            self.calc.divide("1", 2)
        with self.assertRaises(TypeError):
            self.calc.divide(2, "1")
        with self.assertRaises(TypeError):
            self.calc.divide(2, "a")
        with self.assertRaises(TypeError):
            self.calc.divide('%', 1)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(-2, 3), -8)
        self.assertEqual(self.calc.power(-2, 0), 1)
        self.assertEqual(self.calc.power(0, 10), 0)

        with self.assertRaises(TypeError):
            self.calc.power("1", 2)
        with self.assertRaises(TypeError):
            self.calc.power(2, "1")
        with self.assertRaises(TypeError):
            self.calc.power(2, "a")
        with self.assertRaises(TypeError):
            self.calc.power('%', 1)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(4), 2)
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(0), 0)
        self.assertEqual(self.calc.sqrt(1), 1)

        with self.assertRaises(ValueError):
            self.calc.sqrt(-1)

        with self.assertRaises(TypeError):
            self.calc.sqrt("1")
        with self.assertRaises(TypeError):
            self.calc.sqrt("a")
        with self.assertRaises(TypeError):
            self.calc.sqrt('%')

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)

        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
        with self.assertRaises(ValueError):
            self.calc.factorial(3.5)

        with self.assertRaises(TypeError):
            self.calc.factorial("1")
        with self.assertRaises(TypeError):
            self.calc.factorial("a")
        with self.assertRaises(TypeError):
            self.calc.factorial('%')

    def test_sin(self):
        self.assertAlmostEqual(self.calc.sin(0), 0)
        self.assertAlmostEqual(self.calc.sin(math.pi / 2), 1)
        self.assertAlmostEqual(self.calc.sin(math.pi), 0)

        with self.assertRaises(TypeError):
            self.calc.sin("1")
        with self.assertRaises(TypeError):
            self.calc.sin("a")
        with self.assertRaises(TypeError):
            self.calc.sin('%')

    def test_cos(self):
        self.assertAlmostEqual(self.calc.cos(0), 1)
        self.assertAlmostEqual(self.calc.cos(math.pi / 2), 0)
        self.assertAlmostEqual(self.calc.cos(math.pi), -1)
        self.assertAlmostEqual(self.calc.cos(-math.pi / 2), 0)

        with self.assertRaises(TypeError):
            self.calc.cos("1")
        with self.assertRaises(TypeError):
            self.calc.cos("a")
        with self.assertRaises(TypeError):
            self.calc.cos('%')

    def test_tan(self):
        self.assertAlmostEqual(self.calc.tan(0), 0)
        self.assertAlmostEqual(self.calc.tan(math.pi / 4), 1)
        self.assertAlmostEqual(self.calc.tan(math.pi), 0)
        self.assertAlmostEqual(self.calc.tan(-math.pi / 4), -1)

        with self.assertRaises(TypeError):
            self.calc.tan("1")
        with self.assertRaises(TypeError):
            self.calc.tan("a")
        with self.assertRaises(TypeError):
            self.calc.tan('%')

    def test_asin(self):
        self.assertAlmostEqual(self.calc.asin(0), 0)
        self.assertAlmostEqual(self.calc.asin(1), math.pi / 2)
        self.assertAlmostEqual(self.calc.asin(-1), -math.pi / 2)
        self.assertAlmostEqual(self.calc.asin(0.5), math.pi / 6)

        with self.assertRaises(ValueError):
            self.calc.asin(-1.5)
        with self.assertRaises(ValueError):
            self.calc.asin(2)

        with self.assertRaises(TypeError):
            self.calc.asin("1")
        with self.assertRaises(TypeError):
            self.calc.asin("a")
        with self.assertRaises(TypeError):
            self.calc.asin('%')

    def test_acos(self):
        self.assertAlmostEqual(self.calc.acos(1), 0)
        self.assertAlmostEqual(self.calc.acos(0), math.pi / 2)
        self.assertAlmostEqual(self.calc.acos(-1), math.pi)
        self.assertAlmostEqual(self.calc.acos(0.5), math.pi / 3)

        with self.assertRaises(ValueError):
            self.calc.acos(-1.5)
        with self.assertRaises(ValueError):
            self.calc.acos(2)

        with self.assertRaises(TypeError):
            self.calc.acos("1")
        with self.assertRaises(TypeError):
            self.calc.acos("a")
        with self.assertRaises(TypeError):
            self.calc.acos('%')

    def test_atan(self):
        self.assertAlmostEqual(self.calc.atan(0), 0)
        self.assertAlmostEqual(self.calc.atan(1), math.pi / 4)
        self.assertAlmostEqual(self.calc.atan(-1), -math.pi / 4)
        self.assertAlmostEqual(self.calc.atan(0.5), math.atan(0.5))

        with self.assertRaises(TypeError):
            self.calc.atan("1")
        with self.assertRaises(TypeError):
            self.calc.atan("a")
        with self.assertRaises(TypeError):
            self.calc.atan('%')

    def test_log(self):
        self.assertAlmostEqual(self.calc.log(1), 0)
        self.assertAlmostEqual(self.calc.log(math.e), 1)

        with self.assertRaises(ValueError):
            self.calc.log(0)
        with self.assertRaises(ValueError):
            self.calc.log(-1)

        with self.assertRaises(TypeError):
            self.calc.log("1")
        with self.assertRaises(TypeError):
            self.calc.log("a")
        with self.assertRaises(TypeError):
            self.calc.log('%')

    def test_log10(self):
        self.assertAlmostEqual(self.calc.log10(1), 0)
        self.assertAlmostEqual(self.calc.log10(10), 1)

        with self.assertRaises(ValueError):
            self.calc.log10(0)
        with self.assertRaises(ValueError):
            self.calc.log10(-1)

        with self.assertRaises(TypeError):
            self.calc.log10("1")
        with self.assertRaises(TypeError):
            self.calc.log10("a")
        with self.assertRaises(TypeError):
            self.calc.log10('%')

    def test_exp(self):
        self.assertAlmostEqual(self.calc.exp(0), 1)
        self.assertAlmostEqual(self.calc.exp(1), math.e)
        self.assertAlmostEqual(self.calc.exp(-1), 1 / math.e)
        self.assertAlmostEqual(self.calc.exp(2), math.e ** 2)

        with self.assertRaises(TypeError):
            self.calc.exp("1")
        with self.assertRaises(TypeError):
            self.calc.exp("a")
        with self.assertRaises(TypeError):
            self.calc.exp('%')


if __name__ == '__main__':
    unittest.main()
