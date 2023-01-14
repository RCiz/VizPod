import streamlit as st
import pandas as pd
import numpy as np

@st.cache
def read_csv(filename):
    return pd.read_csv(filename,index_col=0, error_bad_lines=False)

df = read_csv('https://github.com/renato37/VizPod/releases/download/Test/data.csv')

st.title("Analiza Netfliksovih podataka")
st.subheader("Cilj projekta")
st.write("Razumijevanje sadržaja dostupnog u različitim zemljama")
st.write("Otkrivanje sličnog sadržaja uspoređivanjem tekstualnih značajki")
col1, col2 = st.columns(2)
with col1:
    st.subheader("O ovom skupu podataka")
    st.write("Netflix je jedna od najpopularnijih medijskih i video streaming platformi. Imaju više od 8000 filmova ili TV emisija dostupnih na njihovoj platformi, a sredinom 2021., imaju više od 200 milijuna pretplatnika diljem svijeta. Ovaj tablični skup podataka sastoji se od popisa svih filmova i TV emisija dostupnih na Netflixu, zajedno s detaljima poput - glumaca, redatelja, ocjena, godine izdavanja, trajanja itd.")


with col2:
    st.subheader("O podacima")
    st.markdown("**show_id** - Jedinstveni ID za svaki film/TV emisiju")
    st.markdown("**type** - Identifikator - film ili TV emisija")
    st.markdown("**title** - Naslov filma/TV emisije")
    st.markdown("**director** - Redatelj filma")
    st.markdown("**cast** - Glumci uključeni u film / emisiju")
    st.markdown("**country** - Država u kojoj je film/serija proizveden")
    st.markdown("**date_added** - Datum dodavanja na Netflix")
    st.markdown("**release_year** - Stvarna godina izlaska preseljenja/prikazivanja")
    st.markdown("**rating** - TV ocjena filma/emisije")
    st.markdown("**duration** - Ukupno trajanje - u minutama ili broju sezona")