import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import *

data = pd.read_csv("activity.csv")

number_of_days = [d for d in data["date"].unique()]
number_of_steps = []

for i in number_of_days:
    number_of_steps.append(data.loc[data["date"], "steps"].dropna().sum())

# Create second dataframe for py-plotting
frame = pd.DataFrame({"DaysAxis": number_of_days, "StepsAxis": number_of_steps})

# Start plotting
graph = frame.plot.bar(x="DaysAxis", y="StepsAxis")
plt.title("Total Calculation of The Number of Steps Taken per Day")
plt.xlabel("DaysAxis")
plt.ylabel("StepsAxis")
plt.show()

print("Mean = {frame.mean().item()}")
print("Median = {frame.median().item()}")
