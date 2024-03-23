import streamlit as st


st.text("yasir")
st.write("World")
st.title("Yasir")
st.write(['st', 'is <', 3]) # see *
st.markdown('# Latex') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')

st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

st.dataframe(my_dataframe)
