from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.retrievers.multi_query import MultiQueryRetriever

def build_rag(vectorstore):
    llm = ChatGoogleGenerativeAI(model= "gemini-2.5-flash", temperature= 0.7)
    retriever= MultiQueryRetriever.from_llm(retriever= vectorstore.as_retriever(), llm= llm)
    return RetrievalQA.from_chain_type(llm= llm, retriever= retriever)


def query_rag(pipeline, question: str):
    return pipeline.invoke(question)