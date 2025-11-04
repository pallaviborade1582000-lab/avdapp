import streamlit as st
import pandas as pd

data = {
    "Task": [ "Extract", "Transform", "Load"],
    "Satus": ["Completed", "Processing","pending"]
}
df =pd.DataFrame(data)

st.title("Streamlit App-3")
st.write(df)