import Project as p
import unittest
import os.path


class UserStoryTest(unittest.TestCase):
    test = p.Repository(os.path.join('.', 'Trump_Fam.ged'))

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
        expect = ['@I13@']
        self.assertEqual(expect, self.test.us07())

    def test_us08(self):
        expect = ['@F1@', '@F1@', '@F4@', '@F4@', '@F4@', '@F4@']
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
        expect = {'@F2@', '@F1@','@F4@','@F6@'}
        self.assertEqual(expect, self.test.us13())

    def test_us14(self):
        expect = ['@F2@']
        self.assertEqual(expect, self.test.us14())

    def test_us15(self):
        expect = ['@F2@']
        self.assertEqual(expect, self.test.us15())

    def test_us16(self):
        result = self.test.us16()
        self.assertIn('@F6@', result)
        self.assertIn('@F2@', result)

    def test_us17(self):
        expect = ['@F13@']
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
        expect = ['@I33@', '@I34@']
        self.assertEqual(expect, self.test.us20())

    def test_us24(self):
        expect = {'@F8@', '@F7@'}
        self.assertEqual(expect, self.test.us24())

    def test_us25(self):
        expect = {'@F2@', '@F4@'}
        self.assertEqual(expect, self.test.us25())

    def test_us30(self):
        expect = ['@I1@', '@I2@', '@I3@', '@I4@', '@I5@', '@I6@', '@I7@', '@I8@', '@I9@', '@I12@', '@I14@', '@I16@',
                  '@I31@', '@I32@', '@I33@', '@I34@', '@I35@', '@I36@', '@I37@', '@I38@', '@I39@', '@I43@', '@I44@',
                  '@I46@']
        self.assertEqual(expect, self.test.us30())

    def test_us31(self):
        expect = ['@I17@', '@I41@', '@I42@']
        self.assertEqual(expect, self.test.us31())

    def test_us22(self):
        expect = ([], [])
        self.assertEqual(expect, self.test.us22())

    def test_us23(self):
        expect = ['@I26@', '@I28@', '@I28@', '@I26@', '@I41@', '@I42@', '@I42@', '@I41@']
        self.assertEqual(expect, self.test.us23())

    def test_us21(self):
        expect = ['@I5@']
        self.assertEqual(expect, self.test.us21())

    def test_us27(self):
        expect = [('@I1@', 73), ('@I2@', 39), ('@I3@', 71), ('@I5@', 11), ('@I12@', 71), ('@I16@', 64), ('@I17@', 50),
                  ('@I18@', 30), ('@I19@', 30), ('@I20@', 30), ('@I22@', 30), ('@I23@', 30), ('@I24@', 30),
                  ('@I25@', 30), ('@I26@', 30), ('@I27@', 29), ('@I28@', 30), ('@I33@', 18), ('@I41@', 70),
                  ('@I42@', 70), ('@I45@', 11), ('@I46@', 10)]


        self.assertEqual(expect, self.test.us27())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)  # , buffer=True)  to hid print messages
