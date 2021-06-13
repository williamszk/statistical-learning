import streamlit as st

import pandas as pd
import numpy as np
import os


st.title("Relatório de Data Science")


data000 = pd.read_csv("data\\Auto.csv")

st.write(data000.head())
st.write(data000.shape)






