import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

df = pd.read_csv("data/def/data_1.csv")

st.title("Laboratorio di fisica")
st.subheader("Urto con pendolo")

st.dataframe(df)
st.line_chart(df[["time", "position"]])