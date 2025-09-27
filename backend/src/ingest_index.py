from src.ingest import load_document, split_document
from src.embed import get_embedding
from src.vector_store import create_vectorstore, save_vectorstore
import os

def build_index():
    data_dir= "data/"

    docs= []
    for file in os.listdir(data_dir):
        if file.endswith(".pdf"):
            file_path= os.path.join(data_dir, file)
            doc= load_document(file_path)
            docs.extend(doc)

    chunks = split_document(docs)

    embeddings = get_embedding()
    vectorstore = create_vectorstore(chunks, embeddings)
    save_vectorstore(vectorstore, "vectorstore.faiss")