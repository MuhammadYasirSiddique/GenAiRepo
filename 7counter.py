
''' 
Counter with Session State
No matter how many times we press the Increment button in 
the above app, the count remains at 1. Let's understand why:

Each time we press the Increment button, Streamlit reruns 
counter_without_session.py from top to bottom, and with every run, count 
gets initialized to 0 .

Pressing Increment subsequently adds 1 to 0, thus count=1
no matter how many times we press Increment.

'''

import streamlit as st

st.title('Counter Example')
count = 0

incre = st.button('Addition')
if incre:
    count += 1

st.write('Count = ', count)

#################
###SESSION#######
#################

import streamlit as st

st.title('Counter Example')

st.write(st.session_state) 

if 'count' not in st.session_state:
    st.session_state.count = 0



increment = st.button('Increment')
if increment:
    st.session_state.count += 1

clear = st.button('clear')
if clear:
    st.session_state.count = 0

st.write('Count = ', st.session_state.count)
# del st.session_state.count
"Text" , st.session_state.count



#############################
## Call back Function #######
#############################

import streamlit as st

st.title('Counter Example using Callbacks')
if 'counter' not in st.session_state:
    st.session_state.counter = 0

def increment_counter():
    st.session_state.counter += 1

st.button('Increment1', on_click=increment_counter)

# st.button('Increment logic1', on_click=increment_counter)

# st.button('Increment logic2', on_click=increment_counter)

st.write('Count = ', st.session_state.counter)



##############################
### Call back Function #######
#### with Argumemnts #########

import streamlit as st

st.title('Counter Example using Callbacks with args')
if 'counting' not in st.session_state:
    st.session_state.counting = 0

increment_value = st.number_input('Enter a value', value=1, step=5)

def increment_counter(increment_value):
    st.session_state.counting += increment_value

increment = st.button('Incremental', on_click=increment_counter,
    args=(increment_value, ))

st.write('Count = ', st.session_state.counting)