# https://docs.streamlit.io/library/api-reference/layout/st.container


###################
### Bar Chart ####
##################

import streamlit as st
import numpy as np

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")





###################
### Pi Chart ####
##################

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

with st.container():
    st.write("This is inside the container")

    # Generate some example data
    labels = ['Category A', 'Category B', 'Category C']
    sizes = [30, 40, 30]

    # Create a pie chart using Matplotlib
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Display the pie chart using st.pyplot()
    st.pyplot(fig)

st.write("This is outside the container")
