from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

class Retriver:
    def __init__(self, course_info_path, agent_info_path, user_info_path):
        self.course_retriever =  self.create_retriever([course_info_path])
        self.agent_retriever =  self.create_retriever([agent_info_path])
        self.user_retriever =  self.create_retriever([user_info_path])
        
    def create(self):
        return self.course_info_retriever, self.agent_info_retriever, self.user_info_retriever
        
    def create_retriever(self, paths):
        embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        docments = []
        for path in paths:
            loader = PyPDFLoader(path)
            docments.extend(loader.load())
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=1500)
            splited_documents = text_splitter.split_documents(docments)
            vectorDB = FAISS.from_documents(splited_documents, embeddings)
        return vectorDB

    def course_info_retriever(self, question):
        docs = ""
        for result in self.course_retriever.similarity_search_with_relevance_scores(query=question):
            docs += result[0].page_content
        return docs  
        
    def agent_info_retriever(self, question):
        docs = ""
        for result in self.agent_retriever.similarity_search_with_relevance_scores(query=question):
            docs += result[0].page_content
        return docs 
        
    def user_info_retriever(self, question):
        docs = ""
        for result in self.user_retriever.similarity_search_with_relevance_scores(query=question):
            docs += result[0].page_content
        return docs 
