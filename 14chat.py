import streamlit as st

prompt = st.chat_input("Say something")

if 'data' not in st.session_state:
    st.session_state.data  = ["waiting"]

if prompt:
    st.session_state.data.append(prompt)
    for text in st.session_state.data:
        st.write(f"You: {text}")

# st.write(st.session_state.data)

if 'data' in st.session_state and st.session_state.data and st.session_state.data[-1] == "Hi":
    st.write("Hi Welcome")
elif 'data' in st.session_state and st.session_state.data and st.session_state.data[-1] == "waiting":
    st.write('')
else:
    st.write("What did you say?")

