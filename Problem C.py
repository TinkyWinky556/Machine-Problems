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
    steps.append(newData.loc[newData["date"] == i, "steps"].sum())

frame = pd.DataFrame({"Days": number_of_days, "Steps": number_of_steps})

# Plot the dataframe
graph = frame.plot.bar(x="Days", y="Steps")
plt.title("Total Number of Steps Taken per Day")
plt.xlabel("Days")
plt.ylabel("Steps")
plt.show()

# Report for mean and median
print(f"\nReport:\nMean = {frame.mean().item()}\nMedian = {frame.median().item()}")