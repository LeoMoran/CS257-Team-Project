import csv

class gradRateAPI:

    def __init__ (self, fileName):
       with open(fileName, newline='') as file:
            self.fileLines = list(csv.DictReader(file))
    


    def findGradRate(self, schoolDistrict, cohort):
        """Returns the graduation rate for a particular district and cohort"""

        for line in self.fileLines:
            if line['LEANM'] == schoolDistrict and line['CATEGORY'] == cohort:
                return line['RATE']
            
        raise Exception("The school district ", schoolDistrict, " is invalid.")


    def findAllGradRates(self, schoolDistrict):
        """Returns a table with graduation rates from all cohorts in a school district"""

        for line in self.fileLines:
            if line['LEANM'] == schoolDistrict:
                print(line['CATEGORY'], ": ", line['RATE'])

        return 0

    def findStateAverage(state, cohort):
        """Returns the average graduation rate for a particular state and cohort"""
        return 3

    def listLowerDistricts(maxGradRate, cohort):
        """Returns an ordered list of all districts with a graduation rate lower than given for a cohort"""
        return 4

    def listHigherDistricts(minGradRate, cohort):
        """Returns an ordered list of all districts with a graduation rate lower than given for a cohort"""
        return 5

    def listLowerStates(maxGradRate, cohort):
        """Returns an ordered list of all states with a graduation rate higher than given for a cohort"""
        return 6

    def listHigherStates(minGradRate, cohort):
        """Returns an ordered list of all states with a graduation rate lower than given for a cohort"""
        return 7
