import numpy as np
import pandas as pd
import csv
import random
import matplotlib.pyplot as plt

df = pd.read_csv("data/def/data_7.csv")

df.drop_duplicates(subset="position", inplace=True, keep="first")

time = df[["time"]]
positions = df[["position"]]

df.to_csv("data/def/data_7.csv", index=False)

plt.plot(time, positions)
plt.show()