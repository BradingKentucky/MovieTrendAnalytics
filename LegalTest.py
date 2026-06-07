import unittest
import pandas
from matplotlib.testing.compare import make_test_filename

import UndertheHood


class MyTestCase(unittest.TestCase):

    @classmethod
    #cls is shortnening of class. doesn't call new instance of class basicly
    def setUpClass(cls):
        """Load test data once before all tests run"""
        cls.test = pandas.read_csv("Test.csv")
        cls.Testdata = UndertheHood.UnderTheHood(cls.test)

    def test_correct_count(self):
        """Make sure all of 8 genres are present"""
        GenreDict = self.Testdata.genretotalcounter()
        self.assertEqual(len(GenreDict), 8)

    def test_incorrect_count_Documentary(self):
        """Make sure there are 2 documentary films counted"""
        GenreDict = self.Testdata.genretotalcounter()
        self.assertEqual(GenreDict["Documentary"], 2)

    def test_average(self):
        """Make sure the average genre is correct"""
        average = self.Testdata.genretotalcounter()
        self.assertEqual(average["Comedy"], 5)

    def test_lessthan(self):
        """Make sure the film count is correct when given a budget constraint"""
        count = self.Testdata.sortbylessthan(1500000)
        self.assertEqual(len(count), 3)

    def test_lessthan_and_genre(self):
        """Make sure budget constraint and genre is correct"""
        count = self.Testdata.sortbylessthanandgenre(1500000,"Comedy")
        self.assertEqual(len(count), 1)

    def test_years(self):
        """Make sure that year classifcation works"""
        years = self.Testdata.sortbyyears(1975,1989)
        self.assertEqual(len(years), 2)
    def test_income_req(self):
        """Make sure that income requirements work"""
        self.assertEqual(len(self.Testdata.sortbyearnings(2)),6)


if __name__ == '__main__':
    unittest.main()
