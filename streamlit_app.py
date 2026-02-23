import streamlit as st
import time
import random

# 1. KONFIGURACIJA I FAVICON (SOVA 🦉)
st.set_page_config(page_title="Mudrosti - Dominic Chant", page_icon="🦉")

# 2. MRAČNI MISTERIOZNI STIL
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
    .typing-text { color: #FFFFFF; font-size: 1.4rem; text-align: center; padding: 20px; line-height: 1.6; }
    .zeleni-naslov { color: #00FF41 !important; text-align: center; text-shadow: 0 0 10px #00FF41; }
    .copyright { color: #444; font-size: 0.8rem; text-align: center; margin-top: 50px; }
    .stButton>button { background-color: #111; color: #00FF41; border: 1px solid #00FF41; width: 100%; border-radius: 0; }
    .stButton>button:hover { background-color: #00FF41; color: #000; }
    /* Efekt treperenja kursora */
    @keyframes blink { 0% {opacity: 1;} 50% {opacity: 0;} 100% {opacity: 1;} }
    .cursor { animation: blink 1s infinite; color: #00FF41; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Funkcija za efekt pisaćeg stroja
def pisaci_stroj(tekst):
    placeholder = st.empty()
    prikaz = ""
    for slovo in tekst:
        prikaz += slovo
        placeholder.markdown(f"<div class='typing-text'>{prikaz}<span class='cursor'>|</span></div>", unsafe_allow_html=True)
        time.sleep(0.04)

# 3. UVODNA ANIMACIJA (SAMO PRVI PUT)
if 'uvod_mudrosti' not in st.session_state:
    priprava = st.empty()
    faze = ["Otvaranje arhiva...", "25 godina mastila na papiru...", "Labave istine...", "Čvrste sjene."]
    for f in faze:
        priprava.markdown(f"<h2 style='text-align:center; color:#00FF41;'>{f}</h2>", unsafe_allow_html=True)
        time.sleep(1.2)
    priprava.empty()
    st.session_state.uvod_mudrosti = True

# 4. NASLOV
st.markdown("<h1 class='zeleni-naslov'>MUDROSTI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00FF41;'>by Dominic Chant</p>", unsafe_allow_html=True)
st.markdown("---")

# 5. DOHVAĆANJE MUDROSTI IZ TAJNOG SEFA (SECRETS)
if "popis_mudrosti" in st.secrets:
    lista = st.secrets["popis_mudrosti"]
    
    # Osiguravamo da se ne ponavlja ista mudrost odmah
    if 'zadnja' not in st.session_state:
        st.session_state.zadnja = ""
    
    # Biranje nove koja nije ista kao zadnja
    izabrana = random.choice(lista)
    while izabrana == st.session_state.zadnja and len(lista) > 1:
        izabrana = random.choice(lista)
    
    st.session_state.zadnja = izabrana
    
    # PRIKAZ EFEKTOM PISAĆEG STROJA
    pisaci_stroj(izabrana)
    
    st.markdown("---")
    if st.button("TRAŽI NOVU MUDROST"):
        st.rerun()
else:
    st.error("Arhiv je zaključan. (Secrets nisu postavljeni)")

# 6. INFO O AUTORU I LICENCA
st.markdown(f"""
<div class='copyright'>
    Iz arhive Dominic Chant mudrosti skupljane preko 25 godina kemijskom u bilježnice. 
    Ovdje je samo kap mudrosti iz oceana bilježnica. Mudrosti potraži u knjizi:<br>
    <strong>Labave istine i čvrste sjene by Dominic Chant</strong><br>
    all rights reserved © 2026
</div>
""", unsafe_allow_html=True)
