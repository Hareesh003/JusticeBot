Justice Bot

Justice Bot is a legal expert AI chatbot that helps users retrieve insights from legal documents. It utilizes LangChain, Hugging Face embeddings, and Pinecone for efficient document retrieval and query processing.

Features

Processes and stores legal documents for quick retrieval.

Uses Hugging Face embeddings to understand context.

Stores vectorized data in Pinecone.

Retrieves relevant legal insights based on user queries.

Installation

Prerequisites

Make sure you have the following installed:

Python 3.8+

pip

virtualenv (optional but recommended)

setup

1. Clone the repository:
    git clone https://github.com/yourusername/justice-bot.git
    cd justice-bot

2. Create a virtual environment (optional but recommended):
    python -m venv venv
    source venv/bin/activate 

3. Install dependencies
    pip install -r requirements.txt

4. Set up environment variables:
    Create a .env file in the root directory and add the following:
    PINECONE_API_KEY=your_pinecone_api_key
    HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token

Usage

Running the Chatbot

To start the chatbot, run:
    python app.py

Processing Documents

1. Place your legal PDF files inside the data/ folder.

2. Run the indexing script:
    python store_index.py
