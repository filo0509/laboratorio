# import numpy as np
# import pandas as pd
# import csv
# import random
# import matplotlib.pyplot as plt

# time = []
# positions = [70]
# i = 0

# position = 70

# while i <= 3.21:
#     time.append(i)
#     i = round(i + 0.01, 4)

# i = 0

# fattore_di_scala_1 = 0
# fattore_di_scala_2 = 0

# while i <= 3.21:

#     fattore_di_scala_1 = 0.6 / (i + 1.8)
#     fattore_di_scala_2 = 0.6 / (i + 1)
#     subtractor = random.uniform(fattore_di_scala_1, fattore_di_scala_2)
#     position = round(position - subtractor, 1)
#     positions.append(position)
#     i = i + 0.01

# print(time)
# print(positions)

# df = pd.DataFrame({"time": time, "position": positions})

# df.to_csv("data/def/data_1.csv")

# plt.plot(time, positions)
# plt.show()