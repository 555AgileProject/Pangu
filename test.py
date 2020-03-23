import Project as p
import unittest


class UserStoryTest(unittest.TestCase):
    test = p.Repository('./Trump_Fam.ged')
    func_name = ''
    for func_name in ['us01', 'us02', 'us03', 'us04', 'us05', 'us06', 'us07', 'us08', 'us09', 'us10']:
        getattr(test, func_name)()

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
        expect = ['@F7@']
        self.assertEqual(expect, self.test.us09())

    def test_us10(self):
        expect = ['@F1@', '@F7@']
        self.assertEqual(expect, self.test.us10())

    def test_us04(self):
        expect = ['@F4@']
        self.assertEqual(expect, self.test.us04())

    def test_us08(self):
        expect = ['@F4@', '@F4@', '@F4@']
        self.assertEqual(expect, self.test.us08())

    def test_us01(self):
        expect = {'@I6@', '@I13@', '@F4@'}
        self.assertEqual(self.test.us01(), expect)

    def test_us05(self):
        expect = {'@F4@'}
        self.test.us05()
        self.assertEqual(self.test.us05(), expect)
        
    def test_us14(self):
        expect = ['@F7@']
        self.assertEqual(expect, self.test.us09())

    def test_us15(self):
        expect = ['@F3@']
        self.assertEqual(expect, self.test.us09())

    def test_us12(self):
        result= self.test.us12()
        self.assertIn('@F4@',result)
        self.assertIn('@F3@', result)
        self.assertIn('@F2@', result)

    def test_us16(self):
        result = self.test.us16()
        self.assertIn('@F4@', result)
        self.assertIn('@F5@', result)
        self.assertIn('@F2@', result)

    def test_us17(self):
        expect = ['@F9@']
        self.test.us17()
        self.assertEqual(expect, self.test.us17())

    def test_us18(self):
        expect = ['@F10@']
        self.test.us18()
        self.assertEqual(expect, self.test.us18()) #nice




if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2, buffer=True)
