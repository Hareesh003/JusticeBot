from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embedding, get_huggingface_llm  
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import system_prompt
import os

app = Flask(__name__)
# Load environment variables
load_dotenv()

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')  # ADDED
if not PINECONE_API_KEY:
    raise EnvironmentError("PINECONE_API_KEY environment variable is not set.")
if not HUGGINGFACEHUB_API_TOKEN:
    raise EnvironmentError("HUGGINGFACEHUB_API_TOKEN environment variable is not set.")

# Initialize Hugging Face LLM
llm = get_huggingface_llm()  # INITIALIZE LLM

# Pinecone setup
embeddings = download_hugging_face_embedding()
index_name = "justicebot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever = docsearch.as_retriever(search_type="mmr", search_kwargs={"k": 3, "fetch_k": 10})

# Create a proper prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "Question: {input}\nContext: {context}")
])

def process_query(msg):
    print(f"🔍 User Input: {msg}")
    
    # Retrieve relevant documents
    docs = retriever.invoke(msg)
    if not docs:
        return "No relevant information found."
    
    # Combine documents into context
    context = "\n\n".join([doc.page_content for doc in docs])
    print(f"📄 Retrieved Context: {context}")
    
    # Format the prompt with context and question
    formatted_prompt = prompt_template.invoke({
        "input": msg,
        "context": context
    })
    
    # Get response from Featherless/Mistral model
    try:
        response = llm.invoke([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {msg}"}
        ])
        return response.content  # Extract the content from the AIMessage object
    except Exception as e:
        return f"Error generating response: {str(e)}"



@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("msg", "").strip()
    
    if not msg:
        return jsonify({"error": "Empty message"}), 400
        
    response = process_query(msg)
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)