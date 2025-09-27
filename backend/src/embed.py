from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding():
    return HuggingFaceEmbeddings(model= "sentence-transformers/all-MiniLM-L6-v2")