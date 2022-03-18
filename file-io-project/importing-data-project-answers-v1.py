# Transpose Table Function Assignment

# Name: 
# BTECH #: 

# INSTRUCTIONS
# Create a function that takes in a regular csv file as a parameter and transposes it (ie. flip it on its side)
# This means that rows will become columns, and columns will become rows.
# The function will read the old file in and save a new file, with the name indicated in the function parameters
# Make sure to add the parameter encoding='utf-8-sig' to the open() function!

import csv

def transpose_csv(path, new_file_name):
    # Read in the file
    with open(path, newline='', encoding='utf-8-sig') as csvfile:
        r = csv.reader(csvfile)

        # Go through rows, add them to a new "table" (ie. list of lists)
        transposedTable = []

        # The number of columns is the number of lists (rows) to go inside the transposed table
        numberOfColumns = len(next(r))
        newRows = [[] for i in range(numberOfColumns)]

        # Add what once were columns to the transposedTable as rows. Nothing in them yet, though.
        transposedTable.extend(newRows)

        # Go back to the first row with seek
        csvfile.seek(0)
        r = csv.reader(csvfile)

        # Add the rows to a list for iterating
        table = [row for row in r]

        # Loop through each column of the new table, using the column index to determine which values from
        # each row to add to the new column.
        for col in range(len(transposedTable)):
            for row in table:
                transposedTable[col].append(row[col])

        # Save the new table
        with open(new_file_name, 'w', newline='') as newCsv:
            writer = csv.writer(newCsv)
            writer.writerows(transposedTable)
        
    return

# This function will take in the Apple Unit Sales data and output the same, transposed (flipped) data as a new CSV.
transpose_csv("apple_unit_sales_data.csv", "newFile.csv")
