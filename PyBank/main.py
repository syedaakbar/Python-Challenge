# importing necessary modules
import csv
import os
from datetime import datetime, date
import pdb       #for debugging

# defining lists and variables 

#list to store Date column in datetime format
month_year=[] 

#list to store Profit/losses column
revenue = []

#list to store the change in revenue from month to month
change_revenue=[]

# variables that will be evaluated in this script
total=0
total_months=0
average_change = 0
greatest_increase = 0
greatest_decrease = 0

#creating the csv file path 
path_csv = os.path.join('budget_data.csv')

#reading the csv using csv module and creating a file object
with open (path_csv,'r',newline = '') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    
    #skipping the header row 
    next(csv_reader)
    
    #creating a list of rows
    rows = list(csv_reader)

    #looping through rows to create month_year and revenue lists
    for row in rows:
        
        # convert the date from str type to datetime object using strptime() of datetime module 
        month_year_extraction=datetime.strptime(row[0],'%b-%y')
        
        #appending the month_year array to store all datetime values 
        month_year.append(month_year_extraction)

        #making a list of the Profit/loss column
        revenue.append(int(row[1]))

    #pdb.set_trace() - used for debugging

    #looping through (length of revenue list - 1) to generate change_revenue list. 
    for i in range(len(revenue)-1):

        #change in profit/loss is the difference between this month's and previous months's value
        change = revenue[i+1] - revenue[i]
        
        # change_revenue list will hold the change in profit/loss from month to month
        change_revenue.append(change)

    # calculating the variables required for financial analysis 
    
    #total revenue from all months
    total=sum(revenue)
    
    #total months in the dataset
    total_months = len(month_year)

    #average change between months
    average_change = sum(change_revenue)/len(change_revenue)

    #greatest increase in profits
    greatest_increase = max(change_revenue)

    #greatest decrease in profits
    greatest_decrease = min(change_revenue)

#loop through length of change_revenue to get index of the greatest increase/decrese in profit months 
for i in range(len(change_revenue)):

    #for greatest increase in profit
    if change_revenue[i] == greatest_increase:

        #extracting month in the %b(eg 'Dec') format
        month_greatest_increse = month_year[i+1].strftime('%b')  

        #extracting year in the %Y(eg 2012) format
        year_greatest_increase = month_year[i+1].strftime('%Y')
    
    #for greatest decrease in profit 
    if change_revenue[i] == greatest_decrease:
        month_greatest_decrease=month_year[i+1].strftime('%b')
        year_greatest_decrease = month_year[i+1].strftime('%Y')

# printing total months, total profit/loss, average change in profit/loss between months and 
# printing greatest increase in profit and greatest decrease in profit to the terminal 
print("Financial Analysis")
print("---------------------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total))
print("Average change: $" + str(average_change) )
print("Greatest Increase in Profits: " + str(month_greatest_increse) + " " + str(year_greatest_increase) 
        + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(month_greatest_decrease) + " " + str(year_greatest_decrease) 
        + " ($" + str(greatest_decrease) + ")")

# saving the Financial analysis in a text file
fa = open('Financial Analysis.txt','w') 
lines_of_text = ['Financial Analysis \n', 
'-------------------------------------- \n', 
'Total Months: ' + str(total_months) + '\n', 
'Total: $' + str(total) + '\n',
'Greatest Increase in Profits: ' + str(month_greatest_increse) + ' ' + str(year_greatest_increase) + ' ($' + str(greatest_increase) + ') \n',
'Greatest Decrease in Profits: ' + str(month_greatest_decrease) + ' ' + str(year_greatest_decrease) + ' ($' + str(greatest_decrease) + ') \n']
fa.writelines(lines_of_text) 
fa.close() 