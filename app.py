import streamlit as st
import socket
import os

st.set_page_config(page_title="Azure Streamlit Demo")

st.title("🚀 Streamlit on Azure App Service")
st.write("If you can see this, your app is running correctly on Azure! 🎉")

# Show some debug info
st.subheader("Environment Info")
st.write("Assigned PORT:", os.getenv("PORT", "Not set"))
st.write("Hostname:", socket.gethostname())
