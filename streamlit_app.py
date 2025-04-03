import streamlit as st
import pymupdf
import fitz  # PyMuPDF for extracting text from PDF
import google.generativeai as genai
from langchain.prompts import PromptTemplate
import re
from deep_translator import GoogleTranslator
import time

GENAI_API_KEY = st.secrets["GENAI_API_KEY"]

# Set API key for Google Gemini
genai.configure(api_key=GENAI_API_KEY)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join(page.get_text("text") for page in doc)
    return text


# Function to chunk long texts
def chunk_text(text, chunk_size=5000):
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


# Function to summarize text with different levels
@st.cache_data(show_spinner="Generating summary...", ttl=3600)
def summarize_text(text, level):
    model = genai.GenerativeModel("gemini-2.0-flash")
    chunks = chunk_text(text)  # Break into manageable chunks
    summaries = []

    prompt_map = {
        "Short": "Provide a **very brief** summary (1-2 sentences):\n\n{chunk}\n\nSummary:",
        "Medium": "Summarize this text in **a few paragraphs**:\n\n{chunk}\n\nSummary:",
        "Detailed": "Summarize this text **with all important details**:\n\n{chunk}\n\nSummary:",
    }

    for chunk in chunks:
        prompt = prompt_map[level].format(chunk=chunk)
        response = model.generate_content(prompt)
        summaries.append(response.text)

    return "\n\n".join(summaries)


# Function to clean summary output
@st.cache_data(show_spinner="Generating summary...", ttl=3600)
def clean_summary(summary):
    summary = re.sub(r"<think>.*?</think>", "", summary, flags=re.DOTALL)
    return summary.replace("Summary:", "").strip()


# Function to answer a user question using Gemini AI
def answer_question(pdf_text, user_question):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"Document: {pdf_text}\n\nQuestion: {user_question}\nAnswer:"

    response = model.generate_content(prompt)
    return response.text


# Function to translate text
def translate_text(text, target_language):
    return GoogleTranslator(source="auto", target=target_language).translate(text)


# Function to generate a summary stream
def summary_stream(summary):
    for word in summary.split():
        yield word + " "
        time.sleep(0.05)


# Streamlit UI Design
st.set_page_config(page_title="PDF Summarizer & QA", layout="wide", page_icon="📄")

# Upload File Section
st.title("Summar-AI-zer 🤖📄")
st.caption("Turning long reads into quick insights!")
st.divider()
uploaded_file = st.file_uploader("📂 Upload a PDF file", type=["pdf"])

if uploaded_file:
    pdf_text = extract_text_from_pdf(uploaded_file)

    if len(pdf_text) > 5000:
        st.warning("⚠️ Long document detected! Using chunked summarization.")

    st.markdown("#####")

    # Tabs for better UI
    tab1, tab2, tab3 = st.tabs(
        ["📜 Summary", "🌎 Translate Summary", "🔍 Ask a Question"]
    )

    # 📜 Summary Tab
    with tab1:
        # Summarization Level Selector
        level = st.radio(
            "🎯 Select Summary Level",
            ["Short", "Medium", "Detailed"],
            index=1,
            horizontal=True,
        )

        # Generating Summary
        summary = summarize_text(pdf_text, level)
        summary = clean_summary(summary)

        st.write(summary)

        st.download_button("📥 Download Summary", summary, "summary.txt", "text/plain")

    # 🌍 Translation Tab
    with tab2:
        languages = {
            "English": "en",
            "French": "fr",
            "Spanish": "es",
            "German": "de",
            "Hindi": "hi",
            "Chinese": "zh",
            "Japanese": "ja",
        }
        target_language = st.selectbox("Choose language:", list(languages.keys()))

        if target_language:
            translated_summary = translate_text(summary, languages[target_language])
            st.write(translated_summary)

            st.download_button(
                "📥 Download Translated Summary",
                translated_summary,
                f"translated_summary_{target_language}.txt",
                "text/plain",
            )

    # 🔍 Q&A Tab
    with tab3:
        # # Initialize chat history
        # if "messages" not in st.session_state:
        #     st.session_state.messages = []

        # # Display chat messages from history on app rerun
        # for message in st.session_state.messages:
        #     with st.chat_message(message["role"]):
        #         st.markdown(message["content"])

        # # User input for asking questions
        # if user_question := st.chat_input("Ask a question"):
        #     # Display user message in chat message container
        #     with st.chat_message("user"):
        #         st.markdown(user_question)
        #     # Add user message to chat history
        #     st.session_state.messages.append({"role": "user", "content": user_question})
        #     # Generate answer using Gemini AI
        #     answer = answer_question(pdf_text, user_question)
        #     # Display assistant message in chat message container
        #     with st.chat_message("assistant"):
        #         st.markdown(answer)
        #     # Add assistant message to chat history
        #     st.session_state.messages.append({"role": "assistant", "content": answer})
        user_question = st.text_input(
            "Ask a question",
            placeholder="Type your question here...",
            label_visibility="hidden",
        )
        if user_question:
            answer = answer_question(pdf_text, user_question)
            st.info("Answer:")
            st.write(answer)
    
st.divider()
st.caption("🛠️ Designed and developed by Nandini Toshniwal")
st.markdown(
    """
	<style>
	footer {
		visibility: hidden;
	}
	</style>
	""",
    unsafe_allow_html=True,
)
