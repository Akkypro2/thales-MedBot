from langchain_community.vectorstores import FAISS

def create_vectorstore(docs, embeddings):
    return FAISS.from_documents(docs, embeddings)

def save_vectorstore(vs, path="vectorstore.faiss"):
    vs.save_local(path)

def load_vectorstore(path, embeddings):
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)

