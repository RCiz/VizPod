import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import matplotlib.pyplot as plt

@st.cache
def read_csv(filename):
    return pd.read_csv(filename)

def updateTeble(df, key, arr):
    return df[df[key].isin(arr)]

df = read_csv('https://github.com/renato37/VizPod/releases/download/Test/data.csv')

tip = st.radio('Odabir tipa:', set(df['type']))

df = updateTeble(df, 'type', [tip])
duration = set(df['duration'])
listed_in = set(df['listed_in'])

with st.expander('Odabir filtera: '):
    col11, col21 = st.columns(2)
    with col11:
        duration = st.multiselect('Trajanje filma/serije: ', options=set(df['duration']), default=duration)

    with col21:
        listed_in = st.multiselect('Žanr filma/serije: ', options=set(df['listed_in']), default=listed_in)

df = updateTeble(df, 'duration', duration)
df = updateTeble(df, 'listed_in', listed_in)

group = pd.crosstab(df['duration'], df['listed_in'], normalize='index')
col12, col22 = st.columns(2)
with col12:
    st.write(group)

with col22:
    st.bar_chart(group)