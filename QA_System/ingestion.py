import boto3
from langchain.embeddings import BedrockEmbeddings
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain.schema import Document  

bedrock_client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0", client=bedrock_client)

def load_and_split_pdfs():
    data_folder = r"C:\Users\musta\OneDrive\Desktop\LLMOPS_practice\data"  
    chunk_size = 500
    chunk_overlap = 200
    
    all_chunks = []
    
    pdf_files = [f for f in os.listdir(data_folder) if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(data_folder, pdf_file)
        
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        
        for doc in documents:
            chunks = text_splitter.split_text(doc.page_content)
            
            all_chunks.extend([Document(page_content=chunk, metadata={"source": pdf_file}) for chunk in chunks])
    
    return all_chunks

def create_faiss_index(chunks):
    vectorstore = FAISS.from_documents(chunks, bedrock_embeddings)
    
    vectorstore.save_local("faiss_index_constitution")
    
    persisted_vectorstore = FAISS.load_local("faiss_index_constitution", bedrock_embeddings,allow_dangerous_deserialization=True)
    
    return persisted_vectorstore

def main():
    print("Loading and splitting PDFs...")
    chunks = load_and_split_pdfs()
    print(f"Total chunks created: {len(chunks)}")
    
    print("Creating and saving FAISS index...")
    persisted_vectorstore = create_faiss_index(chunks)
    
    query = "What is the role of the constitution?"
    print(f"Performing similarity search for query: {query}")
    
    docs = persisted_vectorstore.similarity_search(query)
    
    print("Search results:")
    for i, doc in enumerate(docs):
        print(f"Document {i+1}: {doc.page_content[:200]}...")  

if __name__ == "__main__":
    main()
