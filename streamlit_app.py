import streamlit as st
import pandas as pd
from utils.extract import load_data
from utils.visualizer import plot_visuals
from utils.llama_api import query_llama

st.set_page_config(page_title="📊 Data Analyst Agent", layout="wide")
st.title("📈 Data Analyst Agent with Together.ai")

uploaded_file = st.file_uploader("Upload a document", type=["csv", "xlsx", "pdf", "docx", "txt", "jpg", "png"])
user_question = st.text_input("Ask a question about the file:")

if uploaded_file:
    data = load_data(uploaded_file)
    if isinstance(data, pd.DataFrame):
        st.dataframe(data.head())
        plot_visuals(data)

        if user_question:
            prompt = f"Here is a dataset:\n{data.head(10).to_csv(index=False)}\n\nQuestion: {user_question}"
            answer = query_llama(prompt)
            st.markdown("### 🤖 Answer:")
            st.write(answer)

    elif isinstance(data, str):
        st.text_area("📝 Extracted Text", data, height=200)

        if user_question:
            prompt = f"Here is some extracted text:\n{data[:1000]}\n\nQuestion: {user_question}"
            answer = query_llama(prompt)
            st.markdown("### 🤖 Answer:")
            st.write(answer)
