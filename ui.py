import streamlit as st
from transformers import pipeline

st.title("AI Log Analyzer 🚀")

uploaded_file = st.file_uploader("Upload log file")

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")

    st.text_area("Log Preview", content, height=200)

    lines = content.split("\n")

    errors = []
    warnings = []

    for line in lines:
        if "error" in line.lower():
            errors.append(line)
        if "warning" in line.lower():
            warnings.append(line)

    st.write(f"🔴 Errors: {len(errors)}")
    st.write(f"🟡 Warnings: {len(warnings)}")

   
    if errors:
        st.error("Errors found!")
        for e in errors:
            st.write(e)

    if warnings:
        st.warning("Warnings found!")
        for w in warnings:
            st.write(w)