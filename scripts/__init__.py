import streamlit as st
import pandas as pd

st.write("""
# Hey ☜(ﾟヮﾟ☜)
Hello world by Saida
""")

df = pd.read_csv("./scripts/temperature.csv")
df.dropna(inplace=True)
df.reset_index(drop=True)

df1 = pd.DataFrame(columns=['year'], data=df["year"])
df2 = pd.DataFrame(columns=['temperature'], data=df["AverageTemperatureUncertaintyFahr"])
df3 = pd.concat(objs=[df1, df2], axis=1)

st.line_chart(df3)

st.write("""
What is your level in Baldur's Gate III?
""")
number = st.slider("Pick a number", 1, 20)
