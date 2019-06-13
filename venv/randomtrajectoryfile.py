#!/usr/bin/python

# This program is designed to generate a random calendar for launch periods.\n
# It will generate a one year calendar with a launch period each month that contains 5 days with times.
# Random times will be invalid launches to test tableau barcode chart. Time periods will be ~120 mins.

# Generate one year of dates with times. Mark days/times as valid launches.

# Remove random times and make them invalid launches

# Write to excel sheet.

import pandas as pd
import time
import random

class launch_date_generator():

    def __init__(self,start_date,end_date):
        self.start_date = start_date
        self.end_date = end_date



    def date_generator(self):
        datelist = pd.date_range('2021-01-01', periods=12, freq='MS').to_list()  # Generate Dates
        datedhours1 = pd.DataFrame()

        for months in datelist:

            datedhours1 = pd.DataFrame(pd.date_range(start=months, periods=24, freq='H'), columns=['Hours']).append(datedhours1,ignore_index=True)



        datedf = pd.DataFrame(datelist,columns=["Dates"])  # Convert to Dataframe
        datedf["Dates"] = datedf["Dates"].astype('datetime64[m]')  # Get Rid of Nano-seconds

        return datedf, datedhours1


run1=launch_date_generator(1-1-2021, 12-31-2021)

datelist1,datelist2=run1.date_generator()
datelist2.to_csv(r'/users/dbaros/documents/test1.csv')
print(datelist1)
print(datelist2)
##################################





