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
        datelist = pd.date_range(pd.datetime.today(), periods=100).tolist()
        return datelist


run1=launch_date_generator(1-1-2021,12-31-2021)

datelist1=run1.date_generator()
print(datelist1)
##################################





