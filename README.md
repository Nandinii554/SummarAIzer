# 📑 SummarAIzer 

🚀 **A powerful Streamlit-based web application that allows users to summarize research papers, translate summaries into multiple languages, and ask AI-powered questions about the document.**  

---

## 📌 Project Overview  
This project is designed to help researchers, students, and professionals efficiently extract key insights from research papers. Often, academic papers are long and complex, making it difficult to grasp their main ideas quickly. This app solves that problem by using **AI-powered summarization** and **translation** to provide concise and readable summaries. Additionally, users can ask questions about the paper using an **interactive Q&A feature** powered by OpenAI or Google Gemini.  

### 🌟 Key Features  
✔ **PDF Upload** – Users can upload a research paper in PDF format.  
✔ **AI-Powered Summarization** – The system extracts the core content and presents a short summary.  
✔ **Multi-Language Translation** – Users can translate the summary into multiple languages.  
✔ **Interactive Q&A** – Users can ask AI questions related to the paper for better understanding.  

---
![image](https://github.com/user-attachments/assets/53e39fe1-d177-4eb4-9963-45212c395a3a)
![image](https://github.com/user-attachments/assets/fd55eb20-3c16-4e64-8f48-54e5a6366414)
![image](https://github.com/user-attachments/assets/d6570bb2-0f67-4a1b-bf3b-090643b5ff3c)
![image](https://github.com/user-attachments/assets/70064df3-dd47-4f3b-823c-609945d46e95)


---

## 🖥️ Tech Stack & Tools  
The project integrates **cutting-edge AI and NLP technologies** to deliver an efficient user experience.  

| **Component**        | **Technology Used**                         | **Purpose** |
|----------------------|--------------------------------------------|-------------|
| **Frontend**        | Streamlit                                 | Web interface |
| **Backend**         | Python                                    | Core logic |
| **AI Model**        | OpenAI / Google Gemini API                | Summarization & Q&A |
| **Translation**     | `deep-translator` (Google Translate API)  | Multi-language support |
| **PDF Processing**  | PyMuPDF (`fitz`)                          | Extracting text from PDFs |
| **Environment Config** | `.streamlit/config.toml`                 | Secure API key storage |

---

## 🚀 Project Workflow  
1. **User uploads a research paper (PDF).**  
2. The app extracts text from the PDF using **PyMuPDF (fitz)**.  
3. AI processes the extracted text and generates a **summary**.  
4. The user can **translate** the summary into different languages.  
5. The user can interact with the AI by asking **questions** related to the paper.  

---

## 🚀 Live Demo  
Check out the live app here: [Research Paper Summarizer](https://summar-aiz-er.streamlit.app/)
