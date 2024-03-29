# PyBoss

#![Boss](Images/boss.jpg)

#In this challenge, you get to be the _boss_. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

#Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

#* Import the `employee_data.csv` file, which currently holds employee records like the below:

#```csv
#Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
# ```

# * Then convert and export the data to use the following format instead:

# ```csv
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA
# ```

# * In summary, the required conversions are as follows:

#   * The `Name` column should be split into separate `First Name` and `Last Name` columns.

#   * The `DOB` data should be re-written into `MM/DD/YYYY` format.

#   * The `SSN` data should be re-written such that the first five numbers are hidden from view.

#   * The `State` data should be re-written as simple two-letter abbreviations.

# * Special Hint: You may find this link to be helpful—[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).

import os
import csv
import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

bossData = os.path.join("employee_data.csv")
newBossData = os.path.join("new_employee_data.csv")
# currentDirectory = os.getcwd()
# print(currentDirectory)
# print(bossData)

with open(bossData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    
# The total number of months included in the dataset (row count after the header)
    data = list(csvreader)
    newData = []
    row_count = len(data)

# Set new headers
    headers = ['Emp ID','Last Name','First Name','DOB','SSN','State']
    newData.append(headers)
# Manipulate the data
    for i in range(1,row_count):
        fullname = str(data[i][1])
        fullname = list(fullname.split())
        firstname = fullname[1]
        lastname = fullname[0]
        prefdate = str(data[i][2])
        DOB = datetime.datetime.strptime(prefdate, '%Y-%m-%d').strftime('%m/%d/%Y')
        ssn = data[i][3]
        hidssn = "***-**-"+ssn[-4:]
        state = str(data[i][4])
        stateabv = us_state_abbrev[state]
        templist = [data[i][0],firstname,lastname,DOB,hidssn,stateabv]
        newData.append(templist)
# Creates new file to output data while preserving original data
with open(newBossData, 'w+',newline="", encoding="utf-8") as csvfile2:
    csvwriter = csv.writer(csvfile2, delimiter=",")
    row_count2 = len(newData)
    for j in range(0,row_count2):
        csvwriter.writerow(newData[j])