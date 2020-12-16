import numpy as np
import pandas as pd
import datetime as dt
from matplotlib import pyplot as plt
from statistics import *
import time
import string

df = pd.read_csv("C:/Users/cally/Documents/activity.csv")

run_interval = []
number_of_steps = []

for x in df['interval'].unique():
    run_interval.append(x)
    number_of_steps.append(df.loc[df['interval'], 'steps'].pd.dropna().np.mean())

df = pd.DataFrame({"IntervalAxis": run_interval, "StepsAxis": number_of_steps})

df.plot.line(x = "IntervalAxis", y = "StepsAxis")
plt.title("Average measurement of total number of steps taken in a 5-minute interval")
plt.xlabel("Time Taken")
plt.ylabel("Average Steps")
plt.xticks(np.linspace(0, 200, 15))
plt.show()

print("Interval with max average step: {df.loc[df['Steps'], 'Interval'].item()}.")
