import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

@st.cache
def read_csv(filename):
    return pd.read_csv(filename)

def updateTeble(df, key, arr):
    return df[df[key].isin(arr)]

df = read_csv('https://github.com/renato37/VizPod/releases/download/Test/data.csv')
with st.sidebar:
    prikazDirector = st.checkbox('Filter režisera')
    prikazGlumaca = st.checkbox('Filter glumaca')
    prikazTipa = st.checkbox('Filter tipa')
    prikazGodina = st.checkbox('Filter godina')
    prikazTrajanja = st.checkbox('Filter trajanja')
    prikazZanra = st.checkbox('Filter žanra')

    if prikazDirector:
        director = st.multiselect('Režiseri: ', options=set(df['director']))
        df = updateTeble(df, 'director', director)

    if prikazGlumaca:
        cast = st.multiselect('Glumci: ', options=set(df['cast']))
        df = updateTeble(df, 'cast', cast)

    if prikazTipa:
        type = st.multiselect('Film/serija: ', options=set(df['type']))
        df = updateTeble(df, 'type', type)

    if prikazGodina:
        release_year = st.multiselect('Godina kada je izašao film: ', options=set(df['release_year']))
        df = updateTeble(df, 'release_year', release_year)

    if prikazTrajanja:
        duration = st.multiselect('Vrijeme trajanja: ', options=set(df['duration']))
        df = updateTeble(df, 'duration', duration)

    if prikazGlumaca:
        listed_in = st.multiselect('Žanr: ', options=set(df['listed_in']))
        df = updateTeble(df, 'listed_in', listed_in)



df = df.drop_duplicates(subset=['show_id'])
chart_data = df[['longitude', 'latitude', 'country']]
chart_data = chart_data.dropna()

with st.expander("Tablica: "):
    st.write(df.value_counts('country'))

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=45,
        longitude=0,
        zoom=4,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[longitude, latitude]',
           radius=20000,
           elevation_scale=1,
           elevation_range=[0, 1000000],
           pickable=True,
           extruded=True,
        ),
    ],
), use_container_width=True)