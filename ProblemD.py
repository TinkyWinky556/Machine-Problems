import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv(r"C:\Users\EDWARD\machine_problems_solved\myVenv\Dataframe.csv")

# Create a new factor variable with two levels :
# "weekday" and "weekend" indicating whether a given date is a weekday or weekend day.
"""
There Are No Weekend Days Available In df['date'], thus Weekends List Is Empty.
"""
weekdays = []
weekends = []
for date in df['date'].unique():
    date_details = date.split("/")
    format = datetime.datetime(int(date_details[-1]), int(date_details[0]), int(date_details[1])).strftime("%A")
    if format == "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday":
        weekdays.append(format)
    elif format == "Saturday" or "Sunday":
        weekends.append(format)

# Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of steps taken, 
# averaged across all weekdays.
"""
Weekend Average Is None, Since There Is No Data Regarding Weekend Activity.
This Does Not Necessarily Require Plotting.
"""
interval = []
weekday_daily_avrg = []
"""
All Dates In df['date'] Are Weekdays.
"""
for i in df['interval'].unique():
    interval.append(i)

for el in interval:
    filtered_df = df[df['interval'] == el]
    mean_per_day = filtered_df['steps'].dropna().mean()
    if np.isnan(mean_per_day):
        weekday_daily_avrg.append(0)
    else:
        weekday_daily_avrg.append(mean_per_day)

plt.plot(interval, weekday_daily_avrg, 'r')
plt.title("Plot This")
plt.xlabel("Intervals")
plt.ylabel("Average Steps Taken For An Interval")
plt.grid(True)
plt.show()