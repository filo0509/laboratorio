import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/def/data_10.csv")

velocity = [0]

df["position"] = round(df["position"] / 100, 4)

i = 1

while i < len(df):
    velocity.append(round((df.loc[i - 1, "position"] - df.loc[i, "position"]) / (df.loc[i, "time"] - df.loc[i - 1, "time"]), 5))
    i = i + 1
    
df["velocity"] = velocity

df.to_csv("data/def/data_10.csv")