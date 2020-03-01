import Project as p
import unittest

class UserStoryTest(unittest.TestCase):
    test = p.Repository('./Trump_Fam.ged')
    # def test_us06(self):
    #     expect=[]
    #     test.us06

    def test_us02(self):
        expect = ["@F1@"]
        self.assertEqual(expect,self.test.us02())

    def test_us03(self):
        expect = ["@F1@"]
        self.assertEqual(expect,self.test.us02())

    def test_us07(self):
        expect = ['@I11@', '@I12@']
        self.assertEqual(expect,self.test.us07())

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
        expect = ['@F4@', '@F4@']
        self.assertEqual(expect, self.test.us08())




if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2,buffer=True)
