import streamlit as st
from groq import Groq
import os

st.title("🔑 Test de conexión con Groq")

# Cargar API Key desde Secrets
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))
if not GROQ_API_KEY:
    st.error("No se encontró GROQ_API_KEY en Secrets.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

if st.button("Probar conexión"):
    try:
        resp = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": "Hola, ¿me escuchas?"}],
            max_tokens=100,
        )
        st.success("✅ Conexión exitosa")
        st.write(resp.choices[0].message.content)
    except Exception as e:
        st.error(f"❌ Error: {e}")
