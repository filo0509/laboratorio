import matplotlib.pyplot as plt
from numpy import poly1d
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("data/def/data_1.csv")

x = df[["time"]]
y = df[["acceleration"]]

plt.plot(x, y)
plt.show()