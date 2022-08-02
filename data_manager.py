import pandas as pd
import matplotlib.pyplot as plt
from math import *

plt.style.use("seaborn")

# incertezza di misura della velocità: 0.5cm, ovvero 0.005m
# la misura del tempo è in secondi e ha un errore di misura di 0.0001s, perchè le misurazioni sono state prese a 9600 baud
# la velocità "istantanea" è in m/s, quindi il suo errore relativo è uguale alla somma degli errori relativi di dividendo e divisore


m1 = 0.14904
m2 = 1.36916

h = 0.35

v1 = sqrt(2 * 9.81 * h)

df = pd.read_csv('data/data_5.csv')

# invert all the column 'position', the last value goes first and the first value goes last
df['position'] = df['position'].values[::-1]

df_20 = df.head(20)
# calculate the mean of the velocity column of df_20
avg_velocity = round(df_20["velocity"].mean(), 5)
v2 = round(v1 * (m1 + m1) / (m1 + m2), 5)


# find the difference between the average velocity and all the values of the column 'velocity'
df_20['velocity_error'] = abs(df_20['velocity'] - avg_velocity)
# find the mean of the column 'velocity_error'
avg_velocity_error = round(df_20['velocity_error'].mean(), 5)
print(avg_velocity_error)


plt.plot(df_20["time"], df_20["position"])
plt.show()
