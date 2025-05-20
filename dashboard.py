import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("📊 Bot Absence Log")

df = pd.read_csv("station_bot_absence_log.csv")
st.dataframe(df)

stations = df['Station'].unique().tolist()
station_filter = st.selectbox("Filter by station", ["All"] + stations)
if station_filter != "All":
    df = df[df["Station"] == station_filter]

st.write(f"Showing {len(df)} records")
