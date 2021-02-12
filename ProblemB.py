import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\EDWARD\machine_problems_solved\myVenv\Dataframe.csv")

# The 'interval' List Will Be Used To Plot X-Axis Of The Graph.
interval = []
for i in df['interval'].unique():
    interval.append(i)

# the average number of steps taken, averaged across all days serves to plot the y-axis of the graph.
# loop through all step values in a single interval and take their average. 
each_mean = []
for each in interval:
    each_df = df[df['interval'] == each]
    each_mean.append(each_df['steps'].dropna().mean())

# create the line graph.
plt.plot(interval, each_mean)
plt.xlabel("Intervals")
plt.ylabel("Average Steps Taken For An Interval")
plt.grid(True)
plt.show()

# which 5-minute interval, on average across all the days in the dataset, contains the maximum number of steps?
# index of max mean = index of the corresponding interval, since both elements have the same index value in both lists.
print(f"Interval {interval[each_mean.index(max(each_mean))]} Has The Greatest Average Of Daily Steps Value.")



