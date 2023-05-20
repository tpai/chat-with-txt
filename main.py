import argparse

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Load embeddings and database
embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings)

# Initialize the argument parser
parser = argparse.ArgumentParser(description='Ask a question')
parser.add_argument('question', type=str)
args = parser.parse_args()

# Create a retrieval chain with the ChatOpenAI model
chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0), chain_type="stuff", retriever=db.as_retriever(search_kwargs={"k": 10}))

# Get the answer to the question
chain.run(args.question)
