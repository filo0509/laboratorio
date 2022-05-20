import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/def/data_1.csv")

acceleration = [0]

i = 1

while i < len(df):
    acceleration.append(round((df.loc[i - 1, "velocity"] - df.loc[i, "velocity"]) / (df.loc[i, "time"] - df.loc[i - 1, "time"]), 5))
    i = i + 1
    
df["acceleration"] = acceleration

df.to_csv("data/def/data_1.csv")