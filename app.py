import streamlit as st
from QA_System.ingestion import load_and_split_pdfs
from QA_System.ingestion import create_faiss_index
import os
from QA_System.retrievalandgeneration import get_response_llm


st.title("RAG APP Using Bedrock")

with st.sidebar:
    if st.button("Update FAISS Index"):
        st.write("Processing PDF files...")
        chunks = load_and_split_pdfs()
        st.write(f"Total chunks created: {len(chunks)}")
        st.write("Creating and saving FAISS index...")
        create_faiss_index(chunks)
        st.write("FAISS index has been updated!")

    

st.header("LLaMA Query")
query = st.text_input("Enter your query:")
if st.button("Send to Model"):
    if query:
        st.write("Processing your query...")
        response = get_response_llm(query)
        st.write("Response:")
        st.write(response)
    else:
        st.write("Please enter a query.")