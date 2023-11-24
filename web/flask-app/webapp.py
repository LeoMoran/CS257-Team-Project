import flask
from flask import render_template, request
import json
import sys
from listDistricts import *
from gradRateAPI import *
from listStates import *

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def Home():
    '''
    Loads the home page for GradRate3000, inviting a user query.
    '''
    query="none"
    return render_template('home.html', query=query)

@app.route('/form', methods=['POST'])
def formProgress():
    '''
    Displays the set of input questions for user parameters
    '''
    if request.method == 'POST':
        query = request.form['queries']

    districts = loadDistricts()
    states = loadStates()

    return render_template('home.html', query=query, districts=districts, states=states, error=False)

@app.route('/results', methods=['POST'])
def formComplete():
    '''
    Displays the results of a query
    '''
    districts = loadDistricts()
    states = loadStates()
    
    if request.method == 'POST':
        query = request.form['queryType']

    ''' 
    Try/Except handles bad input from the user, 
    including those that could be used to perform an SQL injection.
    '''
    try:
        api = gradRateAPI()

        if query == 'findGradRate':
            cohort = request.form['cohort']
            district = request.form['myDistrict']
            results = api.findGradRate(district, cohort, api.connection)
            if results == None:
                raise Exception
            rate = results[0]
            state = formatName(results[1])
            return render_template('results.html', rate=rate, state=state, district=formatName(district), cohort=fixCohortName(cohort), query=query)
        elif query == 'findAllGradRates':
            district = request.form['myDistrict']
            results = api.findAllGradRates(district, api.connection)
            if len(results) == 0:
                raise Exception

            # Re-formats some of the results, turning the cohort name from abbreviation to full,
            # displays PS grad rates, and properly formats the state name. 
            fixedResults = []
            for result in results:
                newResult = list(result)
                newResult[0] = fixCohortName(newResult[0])

                if newResult[1] == 0.0:
                    newResult[1] = "Privacy Suppressed"

                fixedResults.append(newResult)
            state = formatName(results[0][2])

            return render_template('results.html', results=fixedResults, state=state, district=formatName(district), query=query)
        elif query == 'findStateAverage':
            state = request.form['myState']
            cohort = request.form['cohort']
            results = api.findStateAverage(state, cohort, api.connection)
            results = round(results, 1)
            return render_template('results.html', results=results, state=formatName(state), cohort=fixCohortName(cohort), query=query)
        elif query == 'orderDistricts':
            cohort = request.form['cohort']
            order = request.form['order']
            cutoff = float(request.form['cutoff'])
            listSize = int(request.form['listSize'])
            if order == "up":
                results = api.listHigherDistricts(cutoff, cohort, listSize, api.connection)
            elif order == "down":
                results = api.listLowerDistricts(cutoff, cohort, listSize, api.connection)

            formattedResults = []
            for result in results:
                newResult = list(result)
                newResult[0] = formatName(newResult[0])
                newResult[2] = formatName(newResult[2])
                formattedResults.append(newResult)

            
            return render_template('results.html', results=formattedResults, cohort=fixCohortName(cohort), query=query, cutoff=cutoff, listSize=listSize)
        elif query == 'orderStates':
            cohort = request.form['cohort']
            order = request.form['order']
            cutoff = float(request.form['cutoff'])
            listSize = int(request.form['listSize'])
            if order == "up":
                results = api.listHigherStates(cutoff, cohort, listSize, api.connection)
            elif order == "down":
                results = api.listLowerStates(cutoff, cohort, listSize, api.connection)

            formattedResults = []
            for result in results:
                newResult = list(result)
                newResult[0] = formatName(newResult[0])
                newResult[1] = round(newResult[1], 1)
                formattedResults.append(newResult)
            
            return render_template('results.html', results=formattedResults, cohort=fixCohortName(cohort), query=query, cutoff=cutoff, listSize=listSize)
    except:
        error = True
        return render_template('home.html', query=query, districts=districts, states=states, error=error)


def fixCohortName(abbreviation):
    '''
    Helper function for converting a cohort abbreviation into its full name. 
    '''
    if abbreviation == "ALL":
        return "All Students"
    elif abbreviation == "CWD":
        return "Children with Disabilities"
    elif abbreviation == "ECD":
        return "Economically Disadvantaged"
    elif abbreviation == "FCS":
        return "Foster Care Students"
    elif abbreviation == "HOM":
        return "Homeless Students"
    elif abbreviation == "LEP":
        return "English Language Learners"
    elif abbreviation == "MAM":
        return "Native American Students"
    elif abbreviation == "MAS":
        return "AAPI Students"
    elif abbreviation == "MBL":
        return "Black Students"
    elif abbreviation == "MHI":
        return "Hispanic/Latine Students"
    elif abbreviation == "MTR":
        return "Multiracial Students"
    elif abbreviation == "MWH":
        return "White Students"

def formatName(name):
    '''
    A helper function for reformatting data that is in all-caps.
    '''
    words = name.split(' ')
    fixedWord = ""
    for word in words:
        if len(word) > 1:
            word = word[0] + word[1:].lower()
        fixedWord = fixedWord + " " + word
    return fixedWord[1:]


@app.route('/about')
def about():
    '''
    Redirects to the 'About the Data' page.
    '''

    return render_template('about.html')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)