import Project as p
import unittest

class UserStoryTest(unittest.TestCase):
    test=p.Repository('./Trump_Fam.ged')
    def test_us06(self):
        expect=['@F4@']
        self.assertEqual(self.test.us06(),expect)

    def test_us07(self):
        expect=['@I11@', '@I12@']
        self.assertEqual(self.test.us07(), expect)



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2,buffer=True)
