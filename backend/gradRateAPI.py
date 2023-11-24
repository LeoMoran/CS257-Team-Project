### GradRateAPI.py, CS257 S23, Prof. Amy Czismar Dalal @ Carleton College
### Implemented API for the backend of our website.
### Written by Graham Gordon, Leo Moran, and Ian Mortensen. 

### ListHigherStates: calls a function that returns a list of tuples with state averages.
### FindStateAverage: calls this same function and searches through this list to get state.
### Also we will get a index out of range error for the listLowerDistrict function right not if we don't check maxSizeList.

import csv
from cli import *
import psycopg2
# import psqlConfig as config

class gradRateAPI:

    def __init__(self):
        
        '''
        Reads in and stores the data from the specified file as a list of dictionaries, for use by the rest of the functions in the class.
        '''

        try:
            self.connection = psycopg2.connect(database="gordong", user="gordong", password="towel962table", host="localhost")
        except Exception as e:
            print("Connection error", e)
            exit()

    def isValidCohort(self, cohort):
        validCohortList = ["ALL", "CWD", "ECD", "FCS", "HOM", "HOM", "LEP", "MAM", "MAS", "MBL", "MHI", "MTR", "MWH"]
        if cohort not in validCohortList:
            return False
        return True

    def findGradRate(self, schoolDistrict, cohort, connection):
        """Returns the graduation rate for a particular district and cohort"""
        ### Function to check if valid schoolDistrict
        ### Call isValid cohort
        ### 
        if self.isValidCohort(cohort):
            
            # need to handle exception with no valid school district
            try:
                cursor = connection.cursor()
                query = "SELECT convertedRate from gradratetable WHERE districtName=%s AND category=%s"
                cursor.execute(query, (schoolDistrict, cohort))
                return cursor.fetchall()[0][0]
            except Exception as e:
                print("Query error: ", e)
                return None

        raise Exception("The cohort ", cohort, " is invalid.")

        
    def findAllGradRates(self, schoolDistrict, connection):
        """Returns a list with graduation rates from all cohorts in a school district."""
        try:
            cursor = connection.cursor()
            query = "SELECT category,convertedRate from gradratetable WHERE districtName=%s"
            cursor.execute(query, (schoolDistrict,))
            return cursor.fetchall()
        except Exception as e:
            print("Query error: ", e)
            return None

    def findStateAverage(self, state, cohort, connection):
        """Returns the average graduation rate for a particular state and cohort"""

        try:
            cursor = connection.cursor()
            query = """SELECT SUM(convertedRate * cohortSize)/SUM(cohortSize) FROM gradratetable 
                WHERE stateName=%s AND category=%s"""
            cursor.execute(query, (state, cohort))
            return cursor.fetchall()[0][0]
        except Exception as e:
            print("Query error: ", e)
            return None

    def trimTuple(self, tuplesList, maxListSize):
        """Returns a list of tuples, trimmed according to user input."""
        if maxListSize > len(tuplesList):
            maxListSize = len(tuplesList)
        return tuplesList[0:maxListSize]

    def listLowerDistricts(self, maxGradRate, cohort, maxListSize, connection):
        """Returns an ordered list of all tuples formatted (district, graduation rate) 
        where the graduation rate is lower than given for a cohort"""

        try:
            cursor = connection.cursor()
            query = "SELECT districtName,convertedRate from gradratetable WHERE category=%s AND convertedRate<%s ORDER BY convertedRate DESC LIMIT %s"
            cursor.execute(query, (cohort,maxGradRate, maxListSize))
            return cursor.fetchall()
        except Exception as e:
            print("Query error: ", e)
            return None

    def listHigherDistricts(self, minGradRate, cohort, maxListSize, connection):
        """Returns an ordered list of all tuples formatted (district, graduation rate) 
        where the graduation rate is higher than given for a cohort"""
        
        try:
            cursor = connection.cursor()
            query = "SELECT districtName,convertedRate from gradratetable WHERE category=%s AND convertedRate>%s ORDER BY convertedRate ASC LIMIT %s"
            cursor.execute(query, (cohort,minGradRate, maxListSize))
            return cursor.fetchall()
        except Exception as e:
            print("Query error: ", e)
            return None

    def findAllAverages(self, cohort, connection):
        """Returns a dictionary of all state averages.""" 

        allStatesList = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", 
                         "CONNECTICUT","DELAWARE", "FLORIDA", "GEORGIA", "HAWAII", "IDAHO", 
                         "INDIANA", "IOWA", "KANSAS", "KENTUCKY", "LOUISIANA", 
                         "MAINE", "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI",
                         "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA", "NEW HAMPSHIRE", 
                         "NEW JERSEY","NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA", 
                         "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA", "RHODE ISLAND", 
                         "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "UTAH", 
                         "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", 
                         "WYOMING", "BUREAU OF INDIAN EDUCATION", "PUERTO RICO"] 
        
        allAverages = []
        for state in allStatesList:
            avg = self.findStateAverage(state, cohort, connection)
            allAverages.append((state, avg))
        return allAverages


    def listLowerStates(self, maxGradRate, cohort, maxListSize, connection):
        """Returns an ordered list of tuples formatted (state, cohortRate) 
        with a graduation rate lower than given for a cohort"""

        if self.isValidCohort(cohort):
            stateAvgTuples = self.findAllAverages(cohort, connection)
            stateAvgTuples.sort(reverse=True, key=lambda x:x[1])
            sortedStatesDescending = stateAvgTuples

            index = 0
            for stateTuple in sortedStatesDescending:
                if stateTuple[1] <= maxGradRate:
                    return self.trimTuple(sortedStatesDescending[index:], maxListSize)
                index += 1
        else:
            raise Exception("The cohort ", cohort, " is invalid.")


    def listHigherStates(self, minGradRate, cohort, maxListSize, connection):
        """Returns an ordered list of tuples formatted (state, cohortRate) 
        with a rate higher than given for a cohort"""

        if self.isValidCohort(cohort):
            stateAvgTuples = self.findAllAverages(cohort, connection)
            stateAvgTuples.sort(reverse=False, key=lambda x:x[1])
            sortedStatesAscending = stateAvgTuples

            index = 0
            for stateTuple in sortedStatesAscending:
                if stateTuple[1] >= minGradRate:
                    return self.trimTuple(sortedStatesAscending[index:], maxListSize)
                index += 1
        else:
            raise Exception("The cohort ", cohort, " is invalid.")




