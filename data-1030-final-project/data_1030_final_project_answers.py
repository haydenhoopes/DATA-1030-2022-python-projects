# Name: Hayden Hoopes
# Date: 12/29/2021

# Write code that takes in the data.csv file, organizes it into two contingency tables 
# (actual and expected) with gotCovid and didNotGetCovid as the rows, and days stayed 
# abroad as the columns. Place the days stayed abroad into bins of one week (1-7 days, 
# 8-14 days, 15-21, 22-28, 29-35, and 36+ days abroad)

# Import the required packages
import numpy as np
import csv
import datetime

def importCsv(path):
    with open(path, newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = []
        next(reader) # Skip the first row (headers)
        for row in reader:
            newRow = []
            arrival = datetime.datetime(int(row[3]), int(row[4]), int(row[5]))
            departure = datetime.datetime(int(row[6]), int(row[7]), int(row[8]))
            daysTravelling = getDaysBetween(arrival, departure)
            row.append(daysTravelling)
            data.append(row)
        return np.array(data)


def getDaysBetween(start, end):
    return int(abs((end - start).total_seconds() / 60 / 60 / 24))

def getContingencyTables(array):
    expected = np.zeros((2,6))
    actual = np.zeros((2, 6))

    for row in array:
        if int(row[10]) <= 7:
            actual[int(row[9]), 0] += 1
        elif int(row[10]) <= 14:
            actual[int(row[9]), 1] += 1
        elif int(row[10]) <= 21:
            actual[int(row[9]), 2] += 1
        elif int(row[10]) <= 28:
            actual[int(row[9]), 3] += 1
        elif int(row[10]) <= 35:
            actual[int(row[9]), 4] += 1
        else:
            actual[int(row[9]), 5] += 1

    total = np.sum(actual)
    numCovidCases = np.sum(actual[1,:])
    percentNotCovid = 1- numCovidCases / total

    for row in range(len(actual)):
        for col in range(len(actual[0])):
            expected[row, col] = abs(row-percentNotCovid) * np.sum(actual[:,col])

    return actual, expected

def getChiSquareStatistic(actual, expected):
    chi = 0
    for row in range(len(actual)):
        for col in range(len(actual[0])):
            chi += ( (float(actual[row,col]) - float(expected[row,col])) ** 2) / float(expected[row,col])
    return chi

def getDegreesOfFreedom(contingencyTable):
    return (contingencyTable.shape[0]-1) * (contingencyTable.shape[1]-1)

def chiSquareTest(path, alpha=0.05):
    data = importCsv(path)
    actual, expected = getContingencyTables(data)
    chi = getChiSquareStatistic(actual, expected)
    doff = getDegreesOfFreedom(actual)
    print(f"The chi square statistic is {chi} and the degrees of freedom are {doff}. The alpha value is {alpha}.")
    return

"""
    QUESTION 1: Based on the Chi square statistic and the degrees of freedom, is there a significant relationship 
    between time spent in Hawaii and becoming infected with COVID-19 at a significance level (alpha) of 0.05?

    ANSWER: At a significance level of 0.05, the Chi square test suggests that a relationship (does/does not) exist
    between time spent in Hawaii and becoming infected with COVID-19.


    QUESTION 2: If a significance level (alpha) of 0.1 had been used, would our interpretation of the Chi square 
    statistic change? How so?

    ANSWER: 
"""


