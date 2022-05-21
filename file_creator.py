import numpy as np
import pandas as pd
import csv
import random
import matplotlib.pyplot as plt

time = [0]
positions = [70]
i = 0

position = 70

while i <= 3.11:
    time.append(round(i, 4))
    i = i + 0.001

i = 0

fattore_di_scala_1 = 0
fattore_di_scala_2 = 0

while i <= 3.11:
    fattore_di_scala_1 = 0.06 / (i + 1.8)
    fattore_di_scala_2 = 0.06 / (i + 1)
    subtractor = random.uniform(fattore_di_scala_1, fattore_di_scala_2)
    position = round(position - subtractor, 2)
    positions.append(position)
    i = i + 0.001

print(time)
print(positions)

df = pd.DataFrame({"time": time, "position": positions})

df.to_csv("data/def/data_4.csv", index=False)

plt.plot(time, positions)
plt.show()