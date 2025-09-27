from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_document(file_path: str):
    loader= PyPDFLoader(file_path)
    return loader.load()

def split_document(docs, chunk_size= 1000, chunk_overlap= 200):
    text_split= RecursiveCharacterTextSplitter(chunk_size= 1000, chunk_overlap= 200, add_start_index= True)
    return text_split.split_documents(docs)

