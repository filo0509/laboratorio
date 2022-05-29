import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression
from math import *

m1 = 0.07804
m2 = 1.36916

h = 0.35

v1 = sqrt(2 * 9.81 * h)

st.title("Laboratorio di fisica: urto con pendolo")

# in the sidebar of streamlit app put a radio to decide the file to open
# st.sidebar.radio("Select the file to open", ["data_1", "data_2", "data_3"])

file = st.sidebar.radio("Select the file to open", [
                        "data_1.csv", "data_2.csv", "data_3.csv", "data_4.csv", "data_5.csv", "data_6.csv"])

df = pd.read_csv("data/def/" + file)
df = df.dropna()

st.write("L'obbiettivo del nostro esperimento era di determinare la velocità con cui la massa urtata si muoveva dopo l'urto.")

# plot time and position of df as x and y axis using plotly express on streamlit app
position_graph = px.scatter(
    df, x="time", y="position", color="position", trendline="ols")
st.plotly_chart(position_graph)

# linear regression of time and position of df as x and y axis using sklearn on streamlit app
model_position = LinearRegression()
model_position.fit(df[["time"]], df[["position"]])
# write the accuracy of the model
st.write("accuracy of the model:", model_position.score(
    df[["time"]], df[["position"]]))

# latex formula for the model on streamlit app
st.latex("y = " + str(model_position.coef_[0]) +
         "x + " + str(model_position.intercept_))

# add a new column named velocity to df that is the variation of position divided by the variation of time
df["velocity"] = round(df["position"].diff() / df["time"].diff(), 4)
df = df.iloc[1:]

velocity_graph = px.scatter(
    df, x="time", y="velocity", color="velocity", trendline="ols")
st.plotly_chart(velocity_graph)

# linear regression of time and velocity of df as x and y axis using sklearn on streamlit app
model_velocity = LinearRegression()
model_velocity.fit(df[["time"]], df[["velocity"]])
# write the accuracy of the model
st.write("accuracy of the model:", model_velocity.score(
    df[["time"]], df[["velocity"]]))

# latex formula for the model on streamlit app
st.latex("y = " + str(model_velocity.coef_[0]) +
         "x + " + str(model_velocity.intercept_))

# find the average of velocity in df
st.write("average of velocity:", round(df["velocity"].mean(), 4))

# velocity of m2 in elastic collision between m1 and m2, m1 has velocity v1, m2 has velocity v2
v2 = v1 * (m1 + m1) / (m1 + m2)

st.write("La velocità che ci aspettavamo è: ", round(-v2, 4))

# add a new column named acceleration to df that is the variation of velocity divided by the variation of time
df["acceleration"] = round(df["velocity"].diff() / df["time"].diff(), 4)
# delete first two rows of df
df = df.iloc[1:]

acceleration_graph = px.scatter(
    df, x="time", y="acceleration", color="acceleration", trendline="ols")
st.plotly_chart(acceleration_graph)

# find the average of acceleration column
avg_acceleration = df["acceleration"].mean()
st.write("Accelerazione media", avg_acceleration)
