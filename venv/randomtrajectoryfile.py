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

    def __init__(self):
        random.seed()

        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                       'November', 'December']

        self.months_numerical = range(1, 13)
        self.hours = range(7, 18)
        self.minutes = range(0, 60)
        self.ampm = ['AM', 'PM']

        # for n in self.months_numerical:
        #    print(n)

        self.monthsdays = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                           'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}



    def date_generator(self):

        date_list=[]
        launch_valid=[]
        count=0
        date_list_index=0

        for x in self.months_numerical:
            chosen_month_days= range(1, self.monthsdays[self.months[x-1]])
            # print('Chosen Month: ', x)
            # print('Chosen month day: ', chosen_month_days[x-1])
            starting_day = random.choice(chosen_month_days)

            # print('Initial Starting day: ', starting_day)

            if abs(starting_day-self.monthsdays[self.months[x-1]]) <= 5:
                starting_day=starting_day-5
            day_range = range(starting_day, starting_day+5)

            for y in day_range:
                starting_hour = random.choice(self.hours)


                hour_range = range(starting_hour, starting_hour+2)


                for z in hour_range:
                    for k in self.minutes:

                        date_list.append(str(x)+"-"+str(y)+"-2020"+"  "+str(z)+":"+str(k)+":00")


        for num_dates in date_list:
            launch_valid.append(True)

            if (count % random.randrange(1, 4)) == 1:
                launch_valid[count] = False

            count += 1



        df_contents={'Dates': date_list, 'Launch Valid': launch_valid}
        date_list_dataframe = pd.DataFrame(data=df_contents)

        return date_list_dataframe





run1=launch_date_generator()

datelist1 = run1.date_generator()


datelist1.to_csv(r'/users/dbaros/documents/test1.csv')


##################################





