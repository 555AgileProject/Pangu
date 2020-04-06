import Project as p
import unittest
import sys


class UserStoryTest(unittest.TestCase):
    if (sys.platform == "win32"):
        test = p.Repository('C:\\Users\\arunn\\Desktop\\Masters!\\SSW-555_Agile\\TeamProject\\Trump_Fam.ged')
    else:
        test = p.Repository('./Trump_Fam.ged')

    def test_us01(self):
        expect = {'@I32@', '@F4@', '@I6@', '@I31@', '@I7@', '@I14@', '@I34@'}
        self.assertEqual(self.test.us01(), expect)

    def test_us02(self):
        expect = ["@F1@"]
        self.assertEqual(expect, self.test.us02())

    def test_us03(self):
        expect = ["@I10@"]
        self.assertEqual(expect, self.test.us03())

    def test_us04(self):
        expect = ['@F4@']
        self.assertEqual(expect, self.test.us04())

    def test_us05(self):
        expect = {'@F4@'}
        self.assertEqual(self.test.us05(), expect)

    def test_us06(self):
        expect = ['@F4@']
        self.assertEqual(expect, self.test.us06())

    def test_us07(self):
        expect = ['@I12@', '@I13@']
        self.assertEqual(expect, self.test.us07())

    def test_us08(self):
        expect = ['@F4@', '@F4@']
        self.assertEqual(expect, self.test.us08())

    def test_us09(self):
        expect = ['@F9@']
        self.assertEqual(expect, self.test.us09())

    def test_us10(self):
        expect = ['@F1@', '@F9@']
        self.assertEqual(expect, self.test.us10())

    def test_us11(self):
        expect = {'@I1@'}
        self.assertEqual(expect, self.test.us11())

    def test_us12(self):
        result = self.test.us12()
        self.assertIn('@F4@', result)
        self.assertIn('@F2@', result)

    def test_us13(self):
        expect = {'@F2@', '@F5@'}
        self.assertEqual(expect, self.test.us13())

    def test_us14(self):
        expect = ['@F2@']
        self.assertEqual(expect, self.test.us14())

    def test_us15(self):
        expect = ['@F2@']
        self.assertEqual(expect, self.test.us15())

    def test_us16(self):
        result = self.test.us16()
        self.assertIn('@F5@', result)
        self.assertIn('@F2@', result)

    def test_us17(self):
        expect = ['@F12@']
        self.test.us17()
        self.assertEqual(expect, self.test.us17())

    def test_us18(self):
        expect = ['@F13@']
        self.test.us18()
        self.assertEqual(expect, self.test.us18())

    def test_us19(self):
        expect = ['@I31@', '@I32@']
        self.assertEqual(expect, self.test.us19())

    def test_us20(self):
        expect = ['@I33@', '@I34@', '@I36@', '@I11@']
        self.assertEqual(expect, self.test.us20())

    def test_us30(self):
        expect = ['@I33@', '@I34@', '@I36@', '@I11@']
        self.assertEqual(expect, self.test.us30())

    def test_us31(self):
        expect = ['@I33@', '@I34@', '@I36@', '@I11@']
        self.assertEqual(expect, self.test.us31())

    def test_us22(self):
        expect = ([], [])
        self.assertEqual(expect, self.test.us22())

    def test_us23(self):
        expect = ['@I41@', '@I42@', '@I42@', '@I41@']
        self.assertEqual(expect, self.test.us23())

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)  # , buffer=True)  to hid print messages
