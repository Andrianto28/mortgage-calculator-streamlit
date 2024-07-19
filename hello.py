import streamlit as st
import pandas as pd
import numpy as np

st.write("# My Cool Chart")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a", "b", "c"]
)
st.write(chart_data)

st.bar_chart(chart_data)
st.line_chart(chart_data)



# ## Show the table on the streamlit
# data = pd.read_csv("movies.csv")
# st.write(data)


# st.write("Hello World")

# x = st.text_input("Favorite Food?")

# st.write(f"Your Favorite food is {x}")