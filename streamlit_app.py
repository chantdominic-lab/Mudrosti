import streamlit as st
import time
import random

# 1. KONFIGURACIJA I FAVICON (Sova)
st.set_page_config(page_title="Mudrosti - Dominic Chant", page_icon="🦉")

# 2. PROŠIRENI CSS (Leteće riječi, Pero, Pulsiranje, Svijeća)
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
    
    /* ANIMACIJA SOVE I PERA */
    .sova, .pero {
        font-size: 80px;
        text-align: center;
        animation: pulse 4s infinite ease-in-out;
    }
    @keyframes pulse {
        0% { opacity: 0.2; text-shadow: 0 0 5px #00FF41; }
        50% { opacity: 1; text-shadow: 0 0 30px #00FF41; }
        100% { opacity: 0.2; text-shadow: 0 0 5px #00FF41; }
    }

    /* VELIKA ZELENA BROJKA */
    .godine-25 {
        color: #00FF41 !important;
        font-size: 80px !important;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 20px #00FF41;
    }

    /* EFEKT SVIJEĆE ZA TEKST MUDROSTI */
    .typing-text { 
        color: #FFFFFF; 
        font-size: 1.5rem; 
        text-align: center; 
        padding: 20px; 
        line-height: 1.6;
        animation: flicker 2s infinite;
    }
    @keyframes flicker {
        0% { opacity: 0.95; } 25% { opacity: 0.85; } 50% { opacity: 1; } 75% { opacity: 0.9; } 100% { opacity: 1; }
    }

    .zeleni-naslov { color: #00FF41 !important; text-align: center; text-shadow: 0 0 10px #00FF41; }
    .copyright { color: #444; font-size: 0.8rem; text-align: center; margin-top: 50px; }
    
    /* GUMB */
    .stButton>button { 
        background-color: #000; color: #00FF41; border: 1px solid #00FF41; 
        width: 100%; border-radius: 0; transition: 0.5s;
    }
    .stButton>button:hover { background-color: #00FF41; color: #000; box-shadow: 0 0 20px #00FF41; }

    /* KURSOR */
    @keyframes blink { 0% {opacity: 1;} 50% {opacity: 0;} 100% {opacity: 1;} }
    .cursor { animation: blink 1s infinite; color: #00FF41; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Funkcija za tipkanje
def pisaci_stroj(tekst):
    placeholder = st.empty()
    prikaz = ""
    for slovo in tekst:
        prikaz += slovo
        placeholder.markdown(f"<div class='typing-text'>{prikaz}<span class='cursor'>|</span></div>", unsafe_allow_html=True)
        time.sleep(0.04)

# 3. MISTIČNI UVOD (Leteće riječi -> Pero -> 25 Godina)
if 'intro_v3' not in st.session_state:
    placeholder = st.empty()
    
    # Faza A: Leteće riječi
    letece_rijeci = ["Sjene...", "Istina...", "Mastilo...", "Tišina...", "Bilježnice..."]
    for rijec in letece_rijeci:
        placeholder.markdown(f"<h2 style='text-align: center; color: white;'>{rijec}</h2>", unsafe_allow_html=True)
        time.sleep(0.8)
    
    # Faza B: Pero
    placeholder.markdown("<div class='pero'>🪶</div>", unsafe_allow_html=True)
    time.sleep(1.5)
    
    # Faza C: 25 Godina
    placeholder.markdown("<div class='godine-25'>25 GODINA</div>", unsafe_allow_html=True)
    time.sleep(2.0)
    
    placeholder.empty()
    st.session_state.intro_v3 = True

# 4. GLAVNI SADRŽAJ (Sova i Mudrosti)
st.markdown("<div class='sova'>🦉</div>", unsafe_allow_html=True)
st.markdown("<h1 class='zeleni-naslov'>MUDROSTI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00FF41;'>by Dominic Chant</p>", unsafe_allow_html=True)
st.markdown("---")

if "popis_mudrosti" in st.secrets:
    lista = st.secrets["popis_mudrosti"]
    if 'zadnja' not in st.session_state:
        st.session_state.zadnja = ""
    
    izabrana = random.choice(lista)
    while izabrana == st.session_state.zadnja and len(lista) > 1:
        izabrana = random.choice(lista)
    
    st.session_state.zadnja = izabrana
    pisaci_stroj(izabrana)
    
    st.markdown("---")
    if st.button("PROBUDI NOVU MUDROST"):
        st.rerun()
else:
    st.error("Arhiv je zaključan. Provjeri Secrets.")

# 5. LICENCA I INFO
st.markdown(f"""
<div class='copyright'>
    Iz arhive Dominic Chant mudrosti skupljane preko 25 godina kemijskom u bilježnice.<br>
    <strong>Labave istine i čvrste sjene by Dominic Chant</strong><br>
    all rights reserved © 2026
</div>
""", unsafe_allow_html=True)
