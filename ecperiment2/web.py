import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
content1 = """
This just for practice but i do enjoy typing random words. 
Don't mind my english but if you wanna then you can. 
How can i stop someone from judging something like hahaha funny. 
Anyway enjoy your day beautiful. Love you emu muwahhh...
"""
st.write(content1)

st.subheader("Our Team")
col1,empty_column1, col2,empty_column2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

uk = pandas.read_csv("data2.csv", sep=",")
with col1:
    for index, row in uk[:4].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images2/" + row["image"])

with col2:
    for index, row in uk[4:8].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images2/" + row["image"])

with col3:
    for index, row in uk[8:].iterrows():
        st.subheader(f"{row["first name"].title()} {row["last name"].title()}")
        st.write(row["role"])
        st.image("images2/" + row["image"])


