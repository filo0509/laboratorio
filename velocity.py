import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/def/data_7.csv")

velocity = [0.0]
# df["position"] = round(df["position"] / 100, 3)

i = 1

while i < len(df):
    vel = (df.loc[i, "position"] - df.loc[i - 1, "position"]) / (df.loc[i, "time"] - df.loc[i - 1, "time"])
    velocity.append(round(vel, 3))
    i = i + 1
    
df["velocity"] = velocity

df.to_csv("data/def/data_7.csv", index = False)

plt.scatter(df[["time"]], velocity)
plt.show()