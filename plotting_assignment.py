import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_df = pd.read_csv(r"C:\Users\EDWARD\machine_problems_solved\myVenv\automobile.csv")

# Car List Represents X-Axis.
cars = my_df.loc[: , 'company'].unique()

# Y-Axis Is Represented Of A List Of Mean For Each Car.
each_avrg_mean = []
for el in cars:
    df_filtered = my_df.loc[lambda my_df: my_df['company'] == el]
    mean = round(df_filtered['price'].dropna().mean(), 2)
    each_avrg_mean.append(mean)

# Start Plotting.
plt.plot(cars, each_avrg_mean, 'r', marker = 'o')
plt.title("Average Price Of Each Car Maker")
plt.xlabel("Car Brand")
plt.ylabel("Average Price In GBP")
plt.grid(True)
plt.legend(("Average Price"))
plt.show()

