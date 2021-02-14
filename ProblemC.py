import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\EDWARD\machine_problems_solved\myVenv\Dataframe.csv")

# Calculate and report the total number of missing values in the dataset (i.e. the total number of rows with NAs).
# Using Method : "df.isnull().sum().sum()"
print(f"Found {df.isnull().sum().sum()} Missing Values In Original Dataframe(Before Cleaning Process).")

# Devise a strategy for filling in all of the missing values in the dataset.
# NaN's in df['steps'] will be replaced with random integer values, permanently.
def fill_missing_nans(column):
    if np.isnan(column) == True: 
        column = np.random.randint(0, 200)
    else:
         column = column
    return column

# use the "df['col].apply(func)" method to map each column value onto a function. 
df['steps'] = df['steps'].apply(fill_missing_nans)

# Create a new dataset that is equal to the original dataset but with the missing data filled in.
data = {
            'Steps': df['steps'],
            'Date': df['date'],
            'Interval': df['interval']
       }

new_df = pd.DataFrame(data, dtype = None)

# Make a histogram of the total number of steps taken each day.
each_day = []
steps_each_day = []

for day in new_df['Date'].unique():
    each_day.append(day)

for each in each_day:
    each_one = new_df[new_df['Date'] == each]
    steps_each_day.append(each_one['Steps'].astype(float).sum())

hist_df = pd.DataFrame({"Days": each_day, "Total Steps": steps_each_day})
hist = hist_df.plot.bar(x = "Days", y = "Total Steps")
plt.title("Sum Of Taken Steps For Each Timeline(Measured In Days)")
plt.xlabel("Days")
plt.ylabel("Steps Taken")
plt.show()

# Calculate and report the mean and median total number of steps taken per day.
print(f"Average Of Steps Taken = {np.mean(steps_each_day)}")
print(f"Median Of Steps Taken = {np.median(steps_each_day)}")