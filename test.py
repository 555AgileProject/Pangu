import Project as p
import unittest
import sys
import logging


class UserStoryTest(unittest.TestCase):
    test = p.Repository('./Trump_Fam.ged')
    func_name = ''
    for func_name in ['us01', 'us02', 'us03', 'us04', 'us05', 'us06', 'us07', 'us08', 'us09', 'us10', 'us14', 'us15']:
        getattr(test, func_name)()

    def test_us01(self):
        expect = {'@F4@', '@I30@', '@I34@', '@I6@', '@I13@', '@I32@', '@I31@'}
        self.assertEqual(self.test.us01(), expect)

    def test_us02(self):
        expect = ["@F1@"]
        self.assertEqual(expect, self.test.us02())

    def test_us03(self):
        expect = ["@F1@"]
        self.assertEqual(expect, self.test.us02())

    def test_us04(self):
        expect = ['@F4@']
        self.assertEqual(expect, self.test.us04())

    def test_us05(self):
        expect = {'@F4@'}
        self.test.us05()
        self.assertEqual(self.test.us05(), expect)

    def test_us06(self):
        expect = ['@F4@']
        self.assertEqual(expect, self.test.us06())

    def test_us07(self):
        expect = ['@I11@', '@I12@']
        self.assertEqual(expect, self.test.us07())

    def test_us08(self):
        expect = ['@F4@', '@F4@']
        self.assertEqual(expect, self.test.us08())

    def test_us09(self):
        expect = ['@F8@']
        self.assertEqual(expect, self.test.us09())

    def test_us10(self):
        expect = ['@F1@', '@F8@']
        self.assertEqual(expect, self.test.us10())

    def test_us14(self):
        expect = ['@F8@']
        self.assertEqual(expect, self.test.us09())

    def test_us15(self):
        expect = ['@F8@']
        self.assertEqual(expect, self.test.us09())

    def test_us19(self):
        expect = ['@I31@', '@I32@']
        self.assertEqual(expect, self.test.us19())

    def test_us20(self):
        expect = ['@I33@', '@I34@']
        self.assertEqual(expect, self.test.us20())

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2, buffer=True)
