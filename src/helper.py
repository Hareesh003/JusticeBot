from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
import os
from langchain_pinecone import PineconeVectorStore
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import create_retrieval_chain
from langchain_openai import ChatOpenAI 
load_dotenv()
def load_pdf_file(data):
    loader= DirectoryLoader(data,glob="*.pdf",loader_cls=PyPDFLoader)
    documents=loader.load()

    return documents

def text_split(extracted_data):
    text_splitter= RecursiveCharacterTextSplitter(chunk_size=500)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks

def download_hugging_face_embedding():
    embeddings= HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings

def get_huggingface_llm():
    # Remove the HuggingFaceEndpoint implementation and replace with:
    return ChatOpenAI(
        api_key=os.getenv('FEATHERLESS_API_KEY'),
        base_url="https://api.featherless.ai/v1",
        model="mistralai/Mistral-7B-Instruct-v0.2",
        temperature=0.5,
        max_tokens=256,
    )
