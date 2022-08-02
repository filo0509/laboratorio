import matplotlib.pyplot as plt
import pandas as pd
from math import *

m1 = 0.11904
m2 = 1.36916

h = 0.35

v1 = sqrt(2 * 9.81 * h)

filename = "data_1.csv"

plt.style.use("seaborn")

df = pd.read_csv("data/" + filename)

# create a new column velocity that represents the division between variation of the x and the variation of y
df["velocity"] = round(df["position"].diff() / df["time"].diff(), 5)


# df is equal to df except the rows where the position is less than 0.5
df = df[df["position"] > 0.5]

x = df["time"]
y = df["position"]

# calculate the average velocity
avg_velocity = round(df["velocity"].mean(), 5)
v2 = round(v1 * (m1 + m1) / (m1 + m2), 5)

print("Velocità calcolata con il sistema di conservazione energia e momento: ", v2)
print("Velocità media del proiettile: ", abs(avg_velocity))

plt.title("Grafico tempo-posizione")
plt.xlabel("Time [s]")
plt.ylabel("Position [m]")
plt.scatter(x, y, s=3)
plt.savefig("data_1.png", format="png", dpi=1200)
