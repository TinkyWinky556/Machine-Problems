import statistics as stt
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\EDWARD\machine_problems_solved\myVenv\Dataframe.csv")

# Separate Days And Each One's Total Of Taken Steps.
days = []
steps_per_day = []
for day in df['date'].unique():
    days.append(day)
# Filter The Dataframe For Each Day.
# Collect The Sum Of Each Filtered df['steps'] And Append Them Into List.
for d in days:
    each = df[df['date'] == d]
    steps_per_day.append(each['steps'].dropna().sum())

# Create A New Dataframe To Contain Each Day And Its Corresponding Sum Of Steps.
# Plot This New Dataframe Into A Histogram.
hist_df = pd.DataFrame({"Days": days, "Total Steps": steps_per_day})
hist = hist_df.plot.bar(x = "Days", y = "Total Steps")
plt.title("Sum Of Taken Steps For Each Timeline(Measured In Days)")
plt.xlabel("Days")
plt.ylabel("Steps Taken")
plt.show()

# Report For Mean And Median Of Steps Taken.
print(f"Average Of Steps Taken = {stt.mean(steps_per_day)}")
print(f"Median Of Steps Taken = {stt.median(steps_per_day)}")








