import unittest


class NegativeValueError(ValueError):
    pass


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


class TestRectangle(unittest.TestCase):
    def test_width(self):
        r = Rectangle(width=5)
        self.assertEqual(r.width, 5)

    def test_height(self):
        r = Rectangle(width=3, height=4)
        self.assertEqual(r.height, 4)

    def test_perimeter(self):
        r = Rectangle(width=5)
        self.assertEqual(r.perimeter(), 20)

    def test_area(self):
        r = Rectangle(width=3, height=4)
        self.assertEqual(r.area(), 12)

    def test_addition(self):
        r1 = Rectangle(width=5)
        r2 = Rectangle(width=3, height=4)
        r3 = r1 + r2
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 9.0)

    def test_subtraction(self):
        r1 = Rectangle(width=10)
        r2 = Rectangle(width=3, height=4)
        r3 = r1 - r2
        self.assertEqual(r3.width, 7)
        self.assertEqual(r3.height, 6.0)

    def test_negative_width(self):
        with self.assertRaises(NegativeValueError):
            Rectangle(width=-5)

    def test_negative_height(self):
        with self.assertRaises(NegativeValueError):
            Rectangle(width=5, height=-4)

    def test_set_width(self):
        r = Rectangle(width=5)
        r.width = 10
        self.assertEqual(r.width, 10)

    def test_set_negative_width(self):
        r = Rectangle(width=5)
        with self.assertRaises(NegativeValueError):
            r.width = -10

    def test_set_height(self):
        r = Rectangle(width=3, height=4)
        r.height = 6
        self.assertEqual(r.height, 6)

    def test_set_negative_height(self):
        r = Rectangle(width=3, height=4)
        with self.assertRaises(NegativeValueError):
            r.height = -6

    def test_subtraction_negative_result(self):
        r2 = Rectangle(width=10)
        r1 = Rectangle(width=3, height=4)
        with self.assertRaises(NegativeValueError):
            r3 = r1 - r2

    def test_subtraction_same_perimeter(self):
        r1 = Rectangle(width=5)
        r2 = Rectangle(width=3, height=4)
        r3 = r1 - r2
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 1.0)


if __name__ == '__main__':
    unittest.main()