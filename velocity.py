import pandas as pd
import matplotlib.pyplot as plt
from math import *

# devo semplicemente trovare la velocità, poi magari calcolo anche l'energia

plt.style.use("seaborn")

m1 = 0.1994
m2 = 1.53916
h = 0.26
v1 = sqrt(2 * 9.81 * h)

df = pd.read_csv('data/data_6.csv')

# invert all the column 'position', the last value goes first and the first value goes last
df['position'] = df['position'].values[::-1]
df["velocity"] = round(df["position"].diff() / df["time"].diff(), 4)
df.dropna(inplace=True)

df_20 = df.head(20)

avg_velocity = round(df_20["velocity"].mean(), 5)
v2 = round(v1 * (m1 + m1) / (m1 + m2), 5)
print(avg_velocity)
print(v2)

plt.plot(df_20["time"], df_20["position"])
plt.show()