### A command line interface implementing functions from api.py.
### Written by Graham Gordon, Leo Moran, and Ian Mortensen.

from gradRateAPI import *

validCohortList = ["ALL", "CWD", "ECD", "FCS", "HOM", "LEP", "MAM", "MAS", "MBL", "MHI", "MTR", "MWH"]
cohortDescriptions = ["ALL: All Students", "CWD: Students with Disabilities", 
                      "ECD: Economically Disadvantaged Students", "FCS: Foster Care Students",
                      "HOM: Homeless Students", "LEP: English Language Learners", 
                      "MAM: American Indian/Native Alaskan Students", "MAS: Asian American/Pacific Islander Students",
                      "MBL: Black Students", "MHI, Hispanic/Latine Students", "MTR: Multiracial Students",
                      "MWH: White Students"]


def getUserInput():
    print("The following are the functions that you may use:")

    print("""
    findGradRate: Returns the graduation rate of a given school district and cohort.
    findAllGradRates: For a given district, returns the graduation rates for all cohorts. 
    findStateAverage: Returns the average graduation rate for a given state and particular cohort. 
    listLowerDistricts: Given a cohort and maximum graduation rate, returns a size-capped list of the immediate districts with lower graduation rates
    in descending order.
    listHigherDistricts: Given a cohort and minimum graduation rate, returns a size-capped list of the immediate districts with higher graduation rates
    in ascending order. 
    listLowerStates: Given a cohort and maximum graduation rate, returns a size-capped list of the immediate states with lower graduation rates
    in descending order.
    listHigherStates: Given a cohort and minimum graduation rate, returns a size-capped list of the immediate states with higher graduation rates
    in ascending order. 
    \n""")

    userInput = input("Please pick which function you'd like to run:\n")
    return userInput

def query():
    
    func = getUserInput()

    if func == "findGradRate":
        run_findGradRate()
    elif func == "findAllGradRates":
        run_findAllGradRates()
    elif func == "findStateAverage":
        run_findStateAverage()
    elif func == "listHigherStates":
        run_listHigherStates()
    elif func == "listLowerStates":
        run_listLowerStates()
    elif func == "listHigherDistricts":
        run_listHigherDistricts()
    elif func == "listLowerDistricts":
        run_listLowerDistricts()
    else:
        print("That is not a valid function name. Please try again.")

def inputCohort():
    print("Here are a list of cohorts:")
    for item in cohortDescriptions:
        print(item)
    cohort = input("Please enter a cohort: ")
    if isValidCohort(cohort):
        return cohort
    else:
        print("Not a valid cohort.")
        return False
    
def isValidGraduationRate(graduationRate):

    try:
        graduationRate = float(graduationRate)
        if isBetweenZeroAndOneHundred(graduationRate):
            return True
    except:
        print("Invalid Input: Must be a number between 0 and 100")
    return False

def isBetweenZeroAndOneHundred(graduationRate):
    if graduationRate <= 100 and graduationRate >= 0:
        return True
    else:
        print("Invalid Input: Graduation rate must be between 0 and 100.")
        return False

def isValidCohort(cohort):
    if cohort not in validCohortList:
        return False
    return True

<<<<<<< HEAD
=======
def tupleListFormatter(tupleList):
    for curTuple in tupleList:
        print(str(curTuple[0])+ ": "+ str(curTuple[1]))

def isValidState(stateName):

    allStatesList = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", 
                         "CONNECTICUT","DELAWARE", "FLORIDA", "GEORGIA", "HAWAII", "IDAHO", 
                         "INDIANA", "IOWA", "KANSAS", "KENTUCKY", "LOUISIANA", 
                         "MAINE", "MARYLAND", "MASSACHUSETTS", "MINNESOTA", "MISSISSIPPI",
                         "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA", "NEW HAMPSHIRE", 
                         "NEW JERSEY","NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA", 
                         "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA", "RHODE ISLAND", 
                         "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "UTAH", 
                         "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", 
                         "WYOMING", "BUREAU OF INDIAN EDUCATION", "PUERTO RICO"] 
    
    if stateName not in allStatesList:
        return False
    else:
        return True
    

>>>>>>> f32262ac25d80f79fea4f7a17bccc095fda93452
def run_findGradRate():
    district = input("Please enter a school district: ")
    cohort = inputCohort()
    api = gradRateAPI()
    if cohort:
        print(cohort + " graduation rate for district " + district + ": " + str(api.findGradRate(district, cohort, api.connection)))

def run_findAllGradRates():
    district = input("Please enter a school district: ")
    api = gradRateAPI()
    ratesList = api.findAllGradRates(district, api.connection)
    print("All cohort rates for district " + district + ": ")
    for tuple in ratesList:
<<<<<<< HEAD
        print(tuple[0]+ ": " + tuple[1])
    
=======
	    print(str(tuple[0]) + ": " + str(tuple[1]))
>>>>>>> f32262ac25d80f79fea4f7a17bccc095fda93452

def run_findStateAverage():
    state = "FAKE_NAME"
    while not isValidState(state):
        state = input("Please enter a valid state: ")
    cohort = inputCohort()
    api = gradRateAPI()
    if cohort:
        print(cohort + " graduation rate for state " + state + ": " + str(api.findStateAverage(state, cohort, api.connection)))

def run_listHigherStates():
    minGradRate = float(input("Please enter a minimum graduation rate: "))
    cohort = inputCohort()
    maxListSize = int(input("Please enter the maximum number of states you'd like to display: "))
    if maxListSize < 1:
        maxListSize = 10
        print("Negative list length entered. Automatically set to 10. ")
    api = gradRateAPI()
    if isValidGraduationRate(minGradRate) and cohort:
        print("States with a higher average graduation rate than", minGradRate, "for the", cohort, "cohort:")
        tupleListFormatter(api.listHigherStates(minGradRate, cohort, maxListSize, api.connection))

def run_listLowerStates():
    maxGradRate = float(input("Please enter a maximum graduation rate: "))
    cohort = inputCohort()
    maxListSize = int(input("Please enter the maximum number of states you'd like to display: "))
    if maxListSize < 1:
        maxListSize = 10
        print("Negative list length entered. Automatically set to 10. ")
    api = gradRateAPI()
    if isValidGraduationRate(maxGradRate) and cohort:
        print("States with a lower average graduation rate than", maxGradRate, "for the", cohort, "cohort:")
        tupleListFormatter(api.listLowerStates(maxGradRate, cohort, maxListSize, api.connection))

def run_listHigherDistricts():
    minGradRate = float(input("Please enter a minimum graduation rate: "))
    cohort = inputCohort()
    maxListSize = int(input("Please enter the maximum number of states you'd like to display: "))
    if maxListSize < 1:
        maxListSize = 10
        print("Negative list length entered. Automatically set to 10.")
    api = gradRateAPI()
    if isValidGraduationRate(minGradRate) and cohort:
        print("Districts with a higher graduation rate than", minGradRate, "for the", cohort, "cohort:")
        tupleListFormatter(api.listHigherDistricts(minGradRate, cohort, maxListSize, api.connection))

def run_listLowerDistricts():
    maxGradRate = float(input("Please enter a maximum graduation rate: "))
    cohort = inputCohort()
    maxListSize = int(input("Please enter the maximum number of states you'd like to display: "))
    if maxListSize < 1:
        maxListSize = 10
        print("Negative list length entered. Automatically set to 10.")
    api = gradRateAPI()
    if isValidGraduationRate(maxGradRate) and cohort:
        print("Districts with a lower graduation rate than", maxGradRate, "for the", cohort, "cohort:")
        tupleListFormatter(api.listLowerDistricts(maxGradRate, cohort, maxListSize, api.connection))

def main():
    print("Welcome to our API! Here you can explore graduation rates all around the United States for the 2020 cohort!")
    shouldRun = True
    while(shouldRun):
        query()
        response = input("\nWould you like to exit? [Y/n]")
        if response == "Y" or response == "y":
            shouldRun = False

if __name__ == "__main__":
    main()

