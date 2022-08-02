import pandas as pd
import matplotlib.pyplot as plt
from math import *

plt.style.use("seaborn")

m1 = 0.14904
m2 = 1.36916

h = 0.35

v1 = sqrt(2 * 9.81 * h)

df = pd.read_csv('data/data_5.csv')

# invert all the column 'position', the last value goes first and the first value goes last
df['position'] = df['position'].values[::-1]

df_20 = df.head(20)
print(df_20)
# calculate the mean of the velocity column of df_20
avg_velocity = round(df_20["velocity"].mean(), 5)
v2 = round(v1 * (m1 + m1) / (m1 + m2), 5)
print(avg_velocity)
print(v2)

plt.plot(df_20["time"], df_20["position"])
plt.show()