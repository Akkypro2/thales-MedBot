from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.retrievers.multi_query import MultiQueryRetriever
from typing import List
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser

prompt= ChatPromptTemplate.from_messages([
    ("system", "Answer the user's question based on context:\n\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

def build_rag(vectorstore):
    llm = ChatGoogleGenerativeAI(model= "gemini-2.5-flash", temperature= 0.7)
    retriever= MultiQueryRetriever.from_llm(retriever= vectorstore.as_retriever(), llm= llm)
    chain= (RunnablePassthrough.assign(context= lambda x: retriever.invoke(x["input"]))) | prompt | llm | StrOutputParser()
    
    return chain


def query_rag(pipeline, question: str, message_hist: List[BaseMessage] ):
    input= {"input": question, "chat_history": message_hist}
    return pipeline.invoke(input)