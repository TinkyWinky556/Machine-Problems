import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from statistics import *

data = pd.read_csv("C:/Users/cally/Documents/activity.csv")
df = pd.DataFrame(data)

# Detect the number of missing values using .isna() function.
print(data["steps"].isna())

# Create new lists and fill them with those NaN's
number_of_days = [day for day in newData["date"].unique()]
number_of_steps = []

for i in number_of_days:
    number_of_steps.append(newData.loc[newData["date"] == i, "steps"].sum())

frame = pd.DataFrame({"DaysAxis": number_of_days, "StepsAxis": number_of_steps})

# Plot the dataframe
graph = frame.plot.bar(x="DaysAxis", y="StepsAxis")
plt.title("Total Number of Steps Taken per Day")
plt.xlabel("DaysAxis")
plt.ylabel("StepsAxis")
plt.show()

# Print out the mean and median
print("Report:\n")
print("Mean = {frame.mean().item()}")
print("Median = {frame.median().item()}")
