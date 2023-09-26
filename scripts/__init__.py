import os

import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv("C:\\Users\\Saida\\Desktop\\streamlit_test\\scripts\\temperature.csv")
df.dropna(inplace=True)
df.reset_index(drop=True)

df1 = pd.DataFrame(columns=['year'],data=df["year"])
df2 = pd.DataFrame(columns=['temperature'],data=df["AverageTemperatureUncertaintyFahr"])
df3 = pd.concat(objs=[df1,df2],axis=1)


# df2 = pd.DataFrame(data=[df["year"], df["AverageTemperatureUncertaintyFahr"]])
# df2["year"] = pd.to_numeric(df2["year"])
st.line_chart(df3)

print(df.to_string())

number = st.slider("Pick a number", 1, 20)
