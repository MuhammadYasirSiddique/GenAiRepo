# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''
import streamlit as st

import pandas as pd
df : pd.DataFrame = pd.DataFrame({'col1': [1,2,3],'col2':list('abc')})
# df : pd.DataFrame = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe


x : int = 20

'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=20)
fig, ax = plt.subplots(1,1)
ax.hist(arr, bins=30)

fig  # 👈 Draw a Matplotlib chart

'# Pakistan zinda bad'

# hello world
'''
# This is the document title

This is some _markdown_.
'''