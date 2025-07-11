import streamlit as st
import requests

st.set_page_config(page_title="AWS Titan LLM Demo", layout="centered")
st.title("🤖 Ask AWS Titan")

prompt = st.text_area("Enter your question:", height=150)
if st.button("Ask"):
    response = requests.post("https://your-api-id.execute-api.us-east-1.amazonaws.com", json={"prompt": prompt})
    if response.ok:
        st.success(response.json()["answer"])
    else:
        st.error("Error: " + response.text)
