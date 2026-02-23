import streamlit as st
import time
import random

# 1. KONFIGURACIJA
st.set_page_config(page_title="Mudrosti - Dominic Chant", page_icon="🦉")

# 2. STIL - FIKSNI ZELENI SJAJ ZA SOVU I BIJELA SLOVA
st.markdown("""
<style>
    .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Courier New', monospace; }
    
    /* SOVA - FIKSNI ZELENI SJAJ (Bez treperenja) */
    .sova {
        font-size: 80px;
        text-align: center;
        color: #FFFFFF;
        text-shadow: 0 0 20px #00FF41, 0 0 40px #00FF41;
        margin-bottom: 20px;
    }

    /* TEKST 25 GODINA - VELIKA ZELENA SLOVA */
    .godine-25 {
        color: #00FF41 !important;
        font-size: 50px !important;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 15px #00FF41;
    }

    /* PERO - STALNI SJAJ */
    .pero {
        font-size: 80px;
        text-align: center;
        text-shadow: 0 0 15px white;
    }

    /* EFEKT SVIJEĆE ZA MUDROST */
    .typing-text { 
        color: #FFFFFF; 
        font-size: 1.5rem; 
        text-align: center; 
        padding: 20px; 
        line-height: 1.6;
        animation: flicker 3s infinite;
    }
    @keyframes flicker {
        0% { opacity: 0.98; } 50% { opacity: 0.92; } 100% { opacity: 1; }
    }

    .zeleni-naslov { color: #00FF41 !important; text-align: center; text-shadow: 0 0 10px #00FF41; }
    .copyright { color: #444; font-size: 0.8rem; text-align: center; margin-top: 50px; }
    
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
        time.sleep(0.05)

# 3. DRAMATIČNI UVOD (S duljim trajanjem)
if 'intro_v3' not in st.session_state:
    placeholder = st.empty()
    
    # Faza A: Leteće riječi (Kratko)
    letece_rijeci = ["Sjene...", "Istina...", "Mastilo...", "Tišina..."]
    for rijec in letece_rijeci:
        placeholder.markdown(f"<h2 style='text-align: center; color: white;'>{rijec}</h2>", unsafe_allow_html=True)
        time.sleep(0.8)
    
    # Faza B: Pero (Trajanje: 4.5 sekunde)
    placeholder.markdown("<div class='pero'>🪶</div>", unsafe_allow_html=True)
    time.sleep(4.5)
    
    # Faza C: Skupljano preko 25 godina (Trajanje: 3.5 sekunde)
    placeholder.markdown("<div class='godine-25'>SKUPLJANO PREKO 25 GODINA</div>", unsafe_allow_html=True)
    time.sleep(3.5)
    
    placeholder.empty()
    st.session_state.intro_v3 = True

# 4. GLAVNI SADRŽAJ
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

# 5. LICENCA
st.markdown(f"""
<div class='copyright'>
    Iz arhive Dominic Chant mudrosti skupljane preko 25 godina kemijskom u bilježnice.<br>
    <strong>Labave istine i čvrste sjene by Dominic Chant</strong><br>
    all rights reserved © 2026
</div>
""", unsafe_allow_html=True)
