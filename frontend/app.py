import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 RAG Chatbot")
st.markdown("Welcome! Ask any question related to our knowledge base and get an AI-generated answer using Retrieval-Augmented Generation.")

st.markdown("---")

with st.form("question_form"):
    question = st.text_input("📥 Enter your question:")
    submitted = st.form_submit_button("Ask")

    if submitted and question:
        with st.spinner("Thinking..."):
            try:
                response = requests.post("http://backend:8000/ask", json={"question": question})
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer returned.")
                    st.success("✅ Here's what I found:")
                    st.markdown(f"> {answer}")
                else:
                    st.error("Hmm... I couldn't understand the request. Please try again.")
            except requests.exceptions.ConnectionError:
                st.error("🚧 The service is temporarily unavailable. Please make sure the backend is running.")
            except Exception as e:
                st.error("❌ Oops! Something went wrong. Please try again later.")
