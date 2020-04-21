import Project as p
import unittest
import os.path


class UserStoryTest(unittest.TestCase):
    test = p.Repository(os.path.join('.', 'Trump_Fam.ged'))
    
    def test_us01(self):
        expect = {'@I32@', '@F4@', '@I8@', '@I35@', '@I7@', '@I33@', '@I15@'}
        self.assertEqual(self.test.us01(), expect)

    def test_us02(self):
        expect = ["@F1@"]
        self.assertEqual(expect, self.test.us02())

    def test_us03(self):
        expect = ['@I7@', '@I11@']
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
        expect = ['@I14@']
        self.assertEqual(expect, self.test.us07())

    def test_us08(self):
        expect = ['@F1@', '@F1@', '@F4@', '@F4@', '@F4@', '@F4@']
        self.assertEqual(expect, self.test.us08())

    def test_us09(self):
        expect = ['@F6@','@F6@','@F9@']
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
        expect = []
        self.test.us18()
        self.assertEqual(expect, self.test.us18())

    def test_us19(self):
        expect = ['@I32@', '@I33@']
        self.assertEqual(expect, self.test.us19())

    def test_us20(self):
        expect = ['@I34@', '@I35@']
        self.assertEqual(expect, self.test.us20())

    def test_us21(self):
        expect = ['@I6@']
        self.assertEqual(expect, self.test.us21())

    def test_us22(self):
        expect = ([], [])
        self.assertEqual(expect, self.test.us22())

    def test_us23(self):
        expect = ['@I27@', '@I29@', '@I29@', '@I27@', '@I42@', '@I43@', '@I43@', '@I42@']
        self.assertEqual(expect, self.test.us23())

    def test_us24(self):
        expect = {'@F8@', '@F7@'}
        self.assertEqual(expect, self.test.us24())

    def test_us25(self):
        expect = {'@F2@', '@F4@'}
        self.assertEqual(expect, self.test.us25())

    def test_us27(self):
        expect = [('@I1@', 73), ('@I2@', 39), ('@I3@', 71), ('@I5@', 11), ('@I6@', 10), ('@I13@', 71), ('@I17@', 64),
                  ('@I18@', 50), ('@I19@', 30), ('@I20@', 30), ('@I21@', 30), ('@I23@', 30), ('@I24@', 30),
                  ('@I25@', 30), ('@I26@', 30), ('@I27@', 30), ('@I28@', 29), ('@I29@', 30), ('@I34@', 18),
                  ('@I42@', 70), ('@I43@', 70), ('@I46@', 12)]
        self.assertEqual(expect, self.test.us27())

    def test_us28(self):
        expect = {'@F1@': ['@I46@', '@I5@'], '@F2@': ['@I19@', '@I20@', '@I21@', '@I23@', '@I24@', '@I25@', '@I26@', '@I27@', '@I29@', '@I28@', '@I34@', '@I11@', '@I7@'], '@F4@': ['@I1@', '@I42@', '@I43@', '@I16@'], '@F6@': ['@I35@', '@I32@'], '@F7@': ['@I33@'], '@F9@': ['@I18@']}
        self.assertEqual(expect, self.test.us28())

    def test_us29(self):
        expect = ['@I7@', '@I11@', '@I14@', '@I15@', '@I16@', '@I47@']
        self.assertEqual(expect, self.test.us29())
    
    def test_us30(self):
        expect = ['@I1@', '@I2@', '@I3@', '@I4@', '@I5@', '@I6@', '@I8@', '@I9@', '@I10@', '@I13@', '@I15@',
                  '@I17@', '@I32@', '@I33@', '@I34@', '@I35@', '@I36@', '@I37@', '@I38@', '@I39@', '@I40@', '@I44@',
                  '@I45@']
        self.assertEqual(expect, self.test.us30())

    def test_us31(self):
        expect = ['@I18@', '@I42@', '@I43@']
        self.assertEqual(expect, self.test.us31())

    def test_us36(self):
        expect = ['@I7@']
        self.assertEqual(expect, self.test.us36())

    def test_us37(self):
        expect_spouse = '@I8@'
        expect_kids = {'@I35@', '@I32@'}
        self.assertEqual((expect_spouse, expect_kids), self.test.us37())

    def test_us32(self):
        expect = ['@F1@', '@F2@', '@F4@', '@F6@', '@F12@']
        self.assertEqual(expect, self.test.us32())

    def test_us39(self):
        expect = [('@I1@', '@I3@'), ('@I10@', '@I9@'), ('@I15@', '@I9@'), ('@I44@', '@I45@')]
        self.assertEqual(expect, self.test.us39())

    def test_us33(self):
        expect = []
        self.assertEqual(expect, self.test.us33())

    def test_us34(self):
        expect = [('@I13@', '@I14@'), ('@I7@', '@I8@'), ('@I16@', '@I17@'), ('@I32@', '@I33@'), ('@I34@', '@I35@')]
        self.assertEqual(expect, self.test.us34())
    
    def test_us41(self):
        expect = {'@I47@', '@F15@'}
        self.assertEqual(expect, self.test.us41())
        
    def test_us42(self):
        expect = {'@I45@'}
        self.assertEqual(expect, self.test.us42())
  
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)  # , buffer=True)  to hid print messages
