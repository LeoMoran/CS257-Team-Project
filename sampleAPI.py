'''
sampleAPI.py

An example of an API written as a Python class.
The constructor demonstrates how to read a CSV file in as a list of dictionaries, where the keys are the column headings.

CS 257, Winter 2023
'''
import csv

class EarthquakeAPI:

    def __init__(self, filename):
        '''
        Reads in and stores the data from the specified file as a list of dictionaries, for use by the rest of the functions in the class.
        
        PARAMETER
            filename - the name (and path, if not in the current working directory) of the data file
        '''
        with open(filename, newline='') as quakefile:
            self.earthquakes = list(csv.DictReader(quakefile))
            
    def getCountriesWithQuakesBetween(self, low, high):
        '''
        Returns a list of countries that have earthquakes with magnitudes in the specified range.

        PARAMETERS:
        low - the start of the magnitude range (inclusive), as a float
        high - the end of the magnitude range (inclusive), as a float
        '''
        countries = []
        
        for quake in self.earthquakes:
            magnitude = float(quake['mag'])
            if magnitude >= low and magnitude <= high:
                '''
                Note that for brevity, I am not extracting the country name from the location string here. Normally, I would call a function to extract the country name from the location string here.
                '''
                countries.append(quake['place'])
                
        return countries

    def getAverageQuakeMagnitudeByLocation(self, country=""):
        '''
        Returns the average magnitude of all the earthquakes in a specified country

        PARAMETER:
        country - the name of the country of interest. If not specified, the average magnitude of _all_ earthquakes will be returned.
        '''
        if country != "":
            quakeList = getQuakesInCountry(country)
        else:
            quakeList = self.earthquakes
            
        totalMagnitude = 0.0
        
        for quake in quakeList:
            totalMagnitude = totalMagnitude + float(quake['mag'])
            
        return totalMagnitude / len(quakeList)
            
            
    def getQuakesInCountry(country):
        '''
        Returns a DictReader object containing all earthquake data associated with a specified country.
        '''
        # note: I am leaving this unimplemented for now; it will just return all of the earthquakes
        return self.earthquakes
        
        
if __name__ == "__main__":
    quakes = EarthquakeAPI('2.5_month.csv')
    
    places = quakes.getCountriesWithQuakesBetween(5.0, 6.0)
    print("Places with earthquakes between 5.0 and 6.0 magnitude: ")
    for place in places:
        print(place)
    
    avgMagnitudeOfAllEarthquakes = quakes.getAverageQuakeMagnitudeByLocation()
    print("The average magnitude of all earthquakes over 2.5 magnitude this past month is %.1f" % avgMagnitudeOfAllEarthquakes)
