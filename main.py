from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

import config
import vector_store_manager
import rag_handler

def initialize_llm():
    """Initializes and returns the Generative AI model."""
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    
    return ChatGoogleGenerativeAI(
        model=config.LLM_MODEL_NAME,
        google_api_key=google_api_key,
        temperature=0,
        max_retries=2,
    )

def main():
    """Main function to run the RAG application."""
    llm = initialize_llm()
    vectordb = vector_store_manager.load_or_create_vector_store()
    
    # Start the interactive Q&A loop
    print("--- Ready to answer questions from the PDF. Type 'exit' to quit. ---")
    while True:
        user_query = input("\nPlease enter your question: ")
        if user_query.lower() == 'exit':
            print("Exiting application.")
            break
        if user_query:
            rag_handler.get_rag_response(user_query, vectordb, llm)

if __name__ == "__main__":
    main()
