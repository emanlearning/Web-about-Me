import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Eman")
    content = """
    Hi, I am Eman.I am new python programmmer. It's my frist programming language. I want to make apps, webs, Ai and many more things.
    I do have big scopes. 
    See you there!
    """
    st.info(content)

content2 = "Below you can find some of the app i built in python. Feel free to Contact me."

st.write(content2)

