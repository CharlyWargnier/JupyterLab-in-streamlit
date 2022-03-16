import streamlit as st
import streamlit.components.v1 as components

st.title("Jupyterlite in Streamlit")
st.sidebar.header("Configuration")
components.iframe(
    "https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1",
    height=500
)