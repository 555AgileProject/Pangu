import Project as p
import unittest


class UserStoryTest(unittest.TestCase):
    test = p.Repository('./Trump_Fam.ged')

    def test_us02(self):
        expect = ["@F1@"]
        self.assertEqual(expect, self.test.us02())

    def test_us03(self):
        expect = ["@F1@"]
        self.assertEqual(expect, self.test.us02())

    def test_us06(self):
        expect = ['@F4@']
        self.assertEqual(expect, self.test.us06())

    def test_us07(self):
        expect = ['@I11@', '@I12@']
        self.assertEqual(expect, self.test.us07())

    def test_us09(self):
        expect = ['@F8@']
        self.assertEqual(expect, self.test.us09())

    def test_us10(self):
        expect = ['@F1@', '@F8@']
        self.assertEqual(expect, self.test.us10())

    def test_us04(self):
        expect = ['@F4@']
        self.assertEqual(expect, self.test.us04())

    def test_us08(self):
        expect = ['@F4@', '@F4@', '@F4@']
        self.assertEqual(expect, self.test.us08())

    def test_us01(self):
        expect = {'@I6@', '@I13@', '@F4@', '@F5@'}
        self.assertEqual(self.test.us01(), expect)

    def test_us05(self):
        expect = {'@F4@'}
        self.test.us05()
        self.assertEqual(self.test.us05(), expect)

    def test_us14(self):
        expect = ['@F8@']
        self.assertEqual(expect, self.test.us09())

    def test_us15(self):
        expect = ['@F8@']
        self.assertEqual(expect, self.test.us09())

    def test_us12(self):
        result = self.test.us12()
        self.assertIn('@F4@', result)
        self.assertIn('@F2@', result)

    def test_us16(self):
        result = self.test.us16()
        self.assertIn('@F5@', result)
        self.assertIn('@F2@', result)

    def test_us17(self):
        expect = ['@F9@']
        self.test.us17()
        self.assertEqual(expect, self.test.us17())

    def test_us18(self):
        expect = ['@F10@']
        self.test.us18()
        self.assertEqual(expect, self.test.us18())

    def test_us19(self):
        res=self.test.us19()
        self.assertIn('@I31@',res)
        self.assertIn('@I32@', res)

    def test_us20(self):
        expect = ['@I33@', '@I34@']
        self.test.us20()
        self.assertEqual(expect, self.test.us20())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)  # , buffer=True)  to hid print messages
