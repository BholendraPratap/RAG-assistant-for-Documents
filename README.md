# 🧠  RAG Assistant for Technical Documentation

This project is a sophisticated Retrieval-Augmented Generation (RAG) application built with Python, Streamlit, and Google's Gemini models. It allows users to upload technical PDF documents and engage in an intelligent conversation about their content. The assistant is designed to understand user intent, differentiating between specific questions and general queries (like summaries) to provide the most accurate and relevant answers.

> **Note:** This is not a standard RAG implementation. It features a two-stage pipeline that uses an LLM for intent classification before deciding on the optimal retrieval strategy.

---

## 🚀 Live Access

This application is deployed and publicly accessible via Streamlit Community Cloud. You can interact with the live version without any local setup.

**[➡️ Click here to access the live application](https://rag-assistant-for-documents-bvzyrvdcijefuaacjpjm6k.streamlit.app/)**



---

## ✨ Key Features

- **Advanced Intent Detection**: Uses a preliminary LLM call to semantically classify user queries as either `general_query` or `specific_question`, moving beyond simple keyword matching.
- **Dual-Strategy Response Pipeline**:
  - **Full-Text for General Queries**: Intelligently uses the entire document's content to answer broad requests like "summarize this" or "what are the key takeaways?".
  - **Vector Search for Specific Questions**: Employs a classic RAG pipeline to find and use the most relevant document chunks for answering detailed, factual questions.
- **Resilient Fallback Mechanism**: If the retrieved context for a specific question is insufficient, the assistant can use its general knowledge and **clearly disclaims** that the answer is not from the document.
- **Polished & Interactive UI**: A modern, professionally styled interface built with Streamlit, featuring:
  - A two-column layout with the chat on the left and a persistent, real-time log viewer on the right.
  - Custom CSS for a clean, visually appealing user experience.
  - Sidebar for document management, chat statistics, and clearing history.
- **Efficient Caching**: Caches document embeddings in a local ChromaDB vector store. It uses file hashes to instantly load previously processed documents, avoiding redundant and costly processing.
- **Modular & Maintainable Code**: The project is organized into logical modules for document processing, vector store management, and RAG logic, making it easy to understand and extend.

## 🛠️ Tech Stack

- **Backend**: Python
- **Frontend**: Streamlit
- **LLM & Embeddings**: Google Generative AI (Gemini)
- **Orchestration**: LangChain
- **Vector Database**: ChromaDB
- **Document Loading**: PyMuPDF

## 📂 Project Structure

```
j:/Technical RAG/
├── 📄 app.py               # Main Streamlit application, UI, and state management
├── 📄 rag_handler.py         # Core logic for handling queries, including intent detection
├── 📄 vector_store_manager.py # Manages creating, loading, and persisting vector stores
├── 📄 document_processor.py   # Handles PDF loading, text extraction, and chunking
├── 📄 config.py             # Central configuration for models, paths, and parameters
├── 📁 uploads/              # Default directory for uploaded files
├── 📁 vector_stores/         # Directory for cached ChromaDB vector stores
├── 📄 requirements.txt      # Python dependencies
└── 📄 .env                  # For storing API keys (must be created by user)
```

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

You need a Google Generative AI API key to use the Gemini models.

1.  Create a file named `.env` in the root directory of the project.
2.  Add your API key to this file:

    ```
    GOOGLE_API_KEY="your_google_api_key_here"
    ```

## 🚀 How to Run

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run app1.py
```

This will start the web server and open the application in your default web browser.

## 🧠 How It Works

The application follows a systematic workflow to provide intelligent answers from your documents.

1.  **File Upload**: The user uploads a PDF document through the web interface.
2.  **Processing & Caching**:
    - A unique hash (MD5) of the file is generated.
    - The system checks if a vector store for this hash already exists.
    - If not, the document is loaded, split into smaller text chunks, and processed by Google's embedding model to create vector embeddings.
    - These embeddings are saved in a local ChromaDB database, indexed by the file's hash for future use.
3.  **Chat Interaction**: The user asks a question in the chat interface.
4.  **Intent Detection**: A lightweight, preliminary LLM call classifies the user's query as either `general_query` or `specific_question`. This is the "smart" routing step.
5.  **Strategy Selection**:
    - If the intent is `general_query`, the application retrieves the **full text** of the document.
    - If the intent is `specific_question`, the application performs a **similarity search** against the vector store to retrieve the most relevant text chunks.
6.  **Response Generation**: The retrieved context (either full text or specific chunks) is combined with the user's question in a final prompt and sent to the Gemini LLM to generate a coherent, context-aware answer.
7.  **Display**: The final answer is displayed in the chat UI, and the processing steps are shown in the real-time log panel.

## 🔧 Configuration

You can customize the behavior of the RAG pipeline by modifying the `config.py` file. Key parameters include:

- `LLM_MODEL_NAME`: The Gemini model to use for generation.
- `EMBEDDING_MODEL_NAME`: The model used for creating text embeddings.
- `CHUNK_SIZE` / `CHUNK_OVERLAP`: Parameters for text splitting.
- `SIMILARITY_SEARCH_K`: The number of relevant chunks to retrieve for specific questions.
- `RATE_LIMIT_DELAY`: A delay to manage API rate limits during batch embedding.

## 🧑‍💻 Authors

This project was developed by:

- **Shubham Kumar**
- **Anurag Kumar**

From Galgotias University.
