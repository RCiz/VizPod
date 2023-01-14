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

with st.expander('Odabir filtera:'):
    tip = st.multiselect('Odabir tipa:', set(df['type']))
    if (len(tip) != 0):
        df = updateTeble(df, 'type', tip)
    actors = st.multiselect('Odabir glumca:', set(df['cast']))
    if (len(actors) != 0):
        df = updateTeble(df, 'cast', actors)
    directors = st.multiselect('Odabir režisera:', set(df['director']))
    if (len(directors) != 0):
        df = updateTeble(df, 'cast', directors)

df = df.drop_duplicates(subset=['show_id'])
data_frame = df['release_year'].value_counts().reset_index()
data_frame['index'] = data_frame['index'].astype(str)

with st.expander('Prikaz tablice'):
    st.write(df)

st.line_chart(data_frame, x='index', y='release_year')
