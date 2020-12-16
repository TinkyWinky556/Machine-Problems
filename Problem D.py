import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Convert .csv to dataframe.
df = Dataframe(pd.read_csv("C:/Users/cally/Documents/activity.csv"))

days_passed = []
number_of_steps = []
week-id = []
week-day = []

df['whatweek'] = pd.to_datetime(df['date']).dtype(dayofweek)
df["whatweek"] = df["whatweek"].astype(float)

for x in df['date'].unique():
    days_passed.append(x)
    number_of_steps.append(df.loc[df['date']==x, 'steps'].sum())
    week-id.append(df.loc[df['date']==x, 'whatweek'].sum())

for x in week-id:
    if x == 288.0:
        week-day.append('weekday')
    else:
        week-day.append('weekend')

df = pd.DataFrame({'Days': days_passed, 'Steps': number_of_steps , 'Isweekday': week-day})

print(df)

df.plot(x ='Days', kind = 'line')

plt.title('The Average Number of Steps')
plt.xticks(np.linspace(0,61,5))
plt.ylabel('Steps')
plt.show()

