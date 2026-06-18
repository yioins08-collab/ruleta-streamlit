import streamlit as st
import random

st.title("🎡 Ruleta")

if st.button("Girar"):
    numero = random.randint(1, 50)
    st.success(f"Tu número es: {numero}")