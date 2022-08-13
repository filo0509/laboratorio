import pandas as pd
import matplotlib.pyplot as plt
from math import *

# devo semplicemente trovare la velocità, poi magari calcolo anche l'energia

plt.style.use("seaborn")

m1 = 0.14904
m2 = 1.36916

h = 0.35

v1 = sqrt(2 * 9.81 * h)

df = pd.read_csv('data/data_5.csv')

# invert all the column 'position', the last value goes first and the first value goes last
df['position'] = df['position'].values[::-1]

# create a column called 'velocity', that is the difference of the position divided by the time
df['velocity'] = round(df['position'].diff() / df['time'].diff(), 4)

df_20 = df.head(20)

print(df_20)