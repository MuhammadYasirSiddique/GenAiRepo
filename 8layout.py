# https://docs.streamlit.io/library/api-reference/layout/st.columns


#########################
#### Columns ###########
#######################

import streamlit as st

col1, col2, col3 = st.columns([3, 2, 1])

# col1.header("aaaaa")

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")


   


import numpy as np

col1, col2 = st.columns([3, 2])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)