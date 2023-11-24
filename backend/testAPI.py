# Unit tests for gradRateAPI.py
### Many of the tests only cover one equivalence class/test case, because they only have one. 
### These tests are such because behavior will be the same no matter the input. 

import unittest

from gradRateAPI import *

class APITester(unittest.TestCase):
    
    ### Helper function to automate creation of a 'gradRateAPI' object
    def setUp(self):
        self.gradRate = gradRateAPI()

    ### Tests 2 equivalence classes: that the return type is a list and that there are fifty entries. 
    def test_findAllAverages(self):
        cohort = "ALL"
        self.assertEqual(type(self.gradRate.findAllAverages(cohort, self.gradRate.connection)), list)
        self.assertEqual(len(self.gradRate.findAllAverages(cohort, self.gradRate.connection)), 50)

    ### Tests that the function trims a list of tuples to the proper size. 
    ### The second equivalence case makes sure that trimming to a size larger than a current list
    ### will return an unchanged list. 
    def test_trimTuple(self):
        untrimmedTupleList = [("Graham", 15), ("Leo", 420), ("Ian", 69), ("Quoc", 888), ("Amy", 21)]

        maxListSize = 3
        trimmedTupleList = [("Graham", 15), ("Leo", 420), ("Ian", 69)]
        self.assertEqual(self.gradRate.trimTuple(untrimmedTupleList, maxListSize), trimmedTupleList)

        maxListSize = 8
        self.assertEqual(self.gradRate.trimTuple(untrimmedTupleList, maxListSize), untrimmedTupleList)

    ### Tests that findGradRate properly returns the data from the data set.
    def test_findGradRate(self):
        allBoazCityRate = 87
        self.assertEqual(allBoazCityRate, self.gradRate.findGradRate("Boaz City", "ALL", self.gradRate.connection))

    ### Tests if findAllGradRates returns the correct list of tuples from a given district. 
    def test_findAllGradRates(self):
        actualKeyportRates = [("ALL", 87), ("CWD", 75), ("ECD", 95), ("LEP", 0), ("MAS", 0), ("MBL", 0), ("MHI", 90), ("MWH", 92)]
        self.assertEqual(self.gradRate.findAllGradRates("Keyport School District", self.gradRate.connection), actualKeyportRates)

    ### Tests that the proper graduation rate is returned for a given state and cohort.
    def test_findStateAverage(self):
        state = "WASHINGTON"
        cohort = "ALL"
        washingtonAverage = 82.9522
        self.assertEqual(self.gradRate.findStateAverage(state, cohort, self.gradRate.connection), washingtonAverage)

    ### Assures that the function returns the proper list of tuples, with the right size
    ### and appropriate descending districts and rates.
    def test_listLowerDistricts(self):
        maxGradRate = 90.000001
        maxListSize = 2
        cohort = "ALL"
        self.assertEqual(self.gradRate.listLowerDistricts(maxGradRate, cohort, maxListSize, self.gradRate.connection), 
                         [('Dallas County', 90.0), ('Cherokee County', 90.0)])
        
    ### Assures that the function returns the proper list of tuples, with the right size
    ### and appropriate ascending districts and rates.
    def test_listHigherDistricts(self):
        minGradRate = 89.9999999999999
        maxListSize = 2
        cohort = "ALL"
        self.assertEqual(self.gradRate.listHigherDistricts(minGradRate, cohort, maxListSize, self.gradRate.connection), 
                         [('Dallas County', 90.0), ('Cherokee County', 90.0)])

    ### Assures that the function returns the proper list of tuples, with the right size
    ### and appropriate descending states and rates.
    def test_listLowerStates(self):
        cohort = "ALL"
        maxGradRate = 90.000001
        maxListSize = 2
        self.assertEqual(self.gradRate.listLowerStates(maxGradRate, cohort, maxListSize, self.gradRate.connection), 
                         [('DELAWARE', 88.8757), ('MASSACHUSETTS', 88.8426)])

    ### Assures that the function returns the proper list of tuples, with the right size
    ### and appropriate ascending states and rates.
    def test_listHigherStates(self):
        cohort = "ALL"
        minGradRate = 89.9999999
        maxListSize = 2
        self.assertEqual(self.gradRate.listHigherStates(minGradRate, cohort, maxListSize, self.gradRate.connection),
                [('WISCONSIN', 90.1034),('FLORIDA', 90.259)]) 

    ### Tests to make sure the helper function isValidCohort recognizes a valid cohort.
    def test_isValidCohort(self):
        cohort = "ALL"
        self.assertTrue(self.gradRate.isValidCohort(cohort))
    
    ### Tests to make sure that the helper function isValidCohort returns false upon an invalid input.
    def test_isNotValidCohort(self):
        cohort1 = "Invalid"
        cohort2 = 420
        self.assertFalse(self.gradRate.isValidCohort(cohort1))
        self.assertFalse(self.gradRate.isValidCohort(cohort2))
    
    ### Tests to make sure that convertRate throws a valid error when an improper rate is input.
    def test_invalidRate(self):
        badRate = "invalid"
        with self.assertRaises(BaseException):
            self.gradRate.convertRate(badRate)

if __name__ == "__main__":
    unittest.main()