# ---------------------------------------------------------------
# Name: pyBoss.py
# Created by: Felipe Murillo
# Date Created: April 3, 2020
#
# Description: Inputs data employee data from ../Resources/employee_data.csv 
# to output a company preferred formatted CSV file
#
# Inputs: 
# employee_data.csv > employee personal data
#
# Outputs:
# ./Analysis/formatted_employee_data.csv
# ---------------------------------------------------------------

# Import modules to manipulate filesystems
import os
import csv

# Import state abbreviations dictionary:
from us_states import us_state_abbrev

# Specify path to input data
csvpath = os.path.join("..","Resources","employee_data.csv")

# Open input data file
with open(csvpath) as csvfile:

    # Read file as comma delimited
    csvreader = csv.reader(csvfile,delimiter = ',')

    # Skip data contained in header (i.e., 1st row)
    next(csvreader)

    # Initialize working lists
    entries = 0
    employee_entry = []

    for row in csvreader:
        # Employee ID
        emp_id = row[0]
        # Split employee name by first space into a first name and a last name(s) list
        full_name = row[1].split(" ",1)
        first_name = full_name[0]
        last_name = full_name[1]

        # Split DOB into year, day, month and rearrange
        dob = row[2].split("-")
        dob_f = (f'{dob[1]}/{dob[2]}/{dob[0]}')

        # Decode first two parts of SSN number
        ssn = row[3].split("-")
        ssn_f = (f'***-**-{ssn[2]}')

        # Looks for abbreviation of state name in input dictionary
        state_f = us_state_abbrev[row[4]]

        # Compile a full employee entry
        employee_entry.append([emp_id, first_name, last_name, dob_f, ssn_f, state_f])

        # Increment entry counter
        entries += 1


# Save formatted employee data to ../Analysis/formatted_employee_data.csv
output =  os.path.join("..","Analysis","formatted_employee_data.csv")

# If the Output folder does not exist, create it; if it does, use it!
os.makedirs(os.path.dirname(output), exist_ok=True)

# Write output to txt file and close it when done
with open(output,"w") as csvfile:
    csvwriter = csv.writer(csvfile,delimiter = ",")
    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB", "SSN","State"])
    csvwriter.writerows(employee_entry)