# Dependencies 
import os 
import csv
import pdb
from datetime import datetime, date

# dictionary of US state abbreviaitons 
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

#declarations
emp_id=[]
first_name=[]
last_name=[]
dob=[]
ssn=[]
state=[]

#creating the csv file path 
path_csv = os.path.join('employee_data.csv')

#reading the csv using csv module and creating a file object
with open (path_csv,'r',newline = '') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    
    #skipping the header row 
    next(csv_reader)
    
    #creating a list of rows
    rows = list(csv_reader)

    for row in rows:

        emp_id.append(row[0])
        name_split = row[1].split(' ')
        first_name.append(name_split[0])
        last_name.append(name_split[1])
        
        #used strptime to convert a string to datetime format 
        #used strftime to write it in the desired format
        dob.append(datetime.strptime(row[2],'%Y-%m-%d').strftime('%m/%d/%y'))
        
        ssn_split = row[3].split('-')
        ssn.append('***-**-' + ssn_split[2])
        state.append(us_state_abbrev[(row[4])])
    
    #zip the modified data
    entire_data = zip(emp_id,first_name,last_name,dob,ssn,state)

    print(entire_data)

#file path of the outputfile
output_file = os.path.join("employee_data_new.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as csvfile:
    
    writer = csv.writer(csvfile)

    writer.writerow(["Emp ID", "First Name", "Last Name", "DOV", "SSN","State"])

    writer.writerows(entire_data)