import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

df = pd.read_csv("data/def/data_1.csv")

# plot time and position of df as x and y axis using plotly express on streamlit app


# add a new column to df that is the variation of velocity divided by the variation of time