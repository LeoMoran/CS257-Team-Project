from api import *

def query():
    print("The following are the functions that you may use:")

    print("""findGradRates
    findAllGradRates
    findStateAverage
    listLowerDistricts
    listHigherDistricts
    listLowerStates
    listHigherStates\n""")

    func = input("Please pick which function you'd like to run:\n")

    if func == "findGradRate":
        district = input("Please enter a school district: ")
        cohort = input("Please enter a cohort: ")
        print(findGradRate(district, cohort))
    elif func == "findAllGradRates":
        district = input("Please enter a school district: ")
        print(findAllGradRates(district))
    elif func == "findStateAverage":
        state = input("Please enter a school district: ")
        cohort = input("Please enter a cohort: ")
        print(findStateAverage(state, cohort))
    elif func == "listHigherStates":
        minGradRate = input("Please enter a minimum graduation rate: ")
        cohort = input("Please enter a cohort: ")
        print(listHigherStates(minGradRate, cohort))
    elif func == "listLowerStates":
        maxGradRate = input("Please enter a maximum graduation rate: ")
        cohort = input("Please enter a cohort: ")
        print(listLowerStates(maxGradRate, cohort))
    elif func == "listHigherDistricts":
        minGradRate = input("Please enter a minimum graduation rate: ")
        cohort = input("Please enter a cohort: ")
        print(listHigherDistricts(minGradRate, cohort))
    elif func == "listLowerDistricts":
        maxGradRate = input("Please enter a maximum graduation rate: ")
        cohort = input("Please enter a cohort: ")
        print(listLowerDistricts(maxGradRate, cohort))
    else:
        print("That is not a valid function name. Please try again.")
        

def main():
    shouldRun = True
    while(shouldRun):
        query()
        response = input("Would you like to exit? [Y/n]")
        if response == "Y" or response == "y":
            shouldRun = False

if __name__ == "__main__":
    main()

