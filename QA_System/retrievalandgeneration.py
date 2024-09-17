import boto3
from langchain_community.embeddings import BedrockEmbeddings
import os
from langchain_community.document_loaders import PyPDFLoader
import faiss
from langchain_community.vectorstores import FAISS
from langchain_aws import ChatBedrock
from langchain.chains import RetrievalQA

bedrock_client = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0", client=bedrock_client)

def get_response_llm(query):
    persisted_vectorstore = FAISS.load_local("faiss_index_constitution", bedrock_embeddings, allow_dangerous_deserialization=True)
    llm = ChatBedrock(model_id="meta.llama3-8b-instruct-v1:0", model_kwargs=dict(temperature=0))
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=persisted_vectorstore.as_retriever())
    result = qa.run(query)
    return result

def main():
    print("get response llm call")
    print(get_response_llm("hei my name is mustafa. what is RAG?"))

if __name__ == "__main__":
    main()
