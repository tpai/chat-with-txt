from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

import os

# Read all files in the "docs" directory and concatenate their content into a single string
docs_string = ""
for filename in os.listdir("docs"):
    with open(os.path.join("docs", filename), "r") as file:
        docs_string += file.read() + "\n\n"

# Initialize a CharacterTextSplitter with the specified separator, chunk_size, and chunk_overlap
splitter = CharacterTextSplitter(separator="\n\n",chunk_size=0,chunk_overlap=0)
# Create a list of documents by splitting the concatenated docs_string using the splitter
docs = splitter.create_documents([docs_string])

# Initialize OpenAIEmbeddings for generating embeddings
embeddings = OpenAIEmbeddings()
# Create a FAISS index from the documents using the embeddings
db = FAISS.from_documents(docs, embeddings)
# Save the FAISS index locally
db.save_local("faiss_index")