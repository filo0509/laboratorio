import pandas as pd
import matplotlib.pyplot as plt
from math import *

# devo semplicemente trovare la velocità, poi magari calcolo anche l'energia

plt.style.use("seaborn")

m1 = 0.14904
m2 = 1.36916

h = 0.26

v1 = sqrt(2 * 9.81 * h)
v2 = round(v1 * (m1 + m1) / (m1 + m2), 5)

df = pd.read_csv('data/data_5.csv')

# invert all the column 'position', the last value goes first and the first value goes last
df["position"] = df["position"].values[::-1]

# create a column called 'velocity', that is the difference of the position divided by the time
df["velocity"] = round(df["position"].diff() / df["time"].diff(), 4)
df.dropna(inplace=True)

df["energy"] = round((m2 * (df["velocity"] ** 2) / 2), 4)

df_20 = df.head(20)

# ricordati che l'energia cinetica rimane anche nella massa proiettile, quindi è normale che non siano uguali

error = df_20["energy"].std()
mean_value = df_20["energy"].mean()
expected_kinetic_energy = m1 * 9.81 * h
loss_of_energy = 0.14 * 9.81 * m1

print(error)
print(mean_value)
print(expected_kinetic_energy - loss_of_energy)

plt.scatter(df_20["time"], df_20["energy"], label="energy")
plt.show()
