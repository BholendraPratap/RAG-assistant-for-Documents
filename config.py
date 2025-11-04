# --- Configuration File ---

# File and Directory Paths
UPLOAD_DIRECTORY = "uploads"
VECTOR_STORE_BASE_DIR = "vector_stores"
METADATA_FILENAME = "metadata.json"

# Google Generative AI Models
LLM_MODEL_NAME = "gemini-2.5-flash"
EMBEDDING_MODEL_NAME = "models/gemini-embedding-001"

# Text Splitting Parameters
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# Vector Store and Retrieval Parameters
SIMILARITY_SEARCH_K = 3 # Number of relevant chunks to retrieve

# Rate Limiting for Embeddings
EMBEDDING_BATCH_SIZE = 50 # Number of chunks to process at a time
RATE_LIMIT_DELAY = 60 # Seconds to wait between batches