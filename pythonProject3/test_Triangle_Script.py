import unittest
from Triangle_Script import classify_triangle
class test_Classify_Triangle(unittest.TestCase):
    def test_Equilateral_triangle(self):
        self.assertEqual(classify_triangle(60,60,60), "Equilateral")

    def test_Isosceles_triangle(self):
        self.assertEqual(classify_triangle(40,40,60), "Isosceles")

    def test_Scalene_triangle(self):
        self.assertEqual(classify_triangle(60,30,90), "Scalene")

    def test_Right_triangle(self):
        self.assertEqual(classify_triangle(30,40,50), "Scalene and Right")

    def test_If_triangle(self):
        self.assertEqual(classify_triangle(0,40,50), "Not a triangle")


if __name__ == '__main__':
    unittest.main()
