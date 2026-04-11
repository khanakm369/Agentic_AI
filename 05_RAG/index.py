from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from langchain_community.chains import RetrievalQA
# -----------------------------
# 1. Load PDF
# -----------------------------
pdf_path = Path(__file__).parent / "SystemDesignInterview.pdf"
loader = PyPDFLoader(file_path=str(pdf_path))
docs = loader.load()

# -----------------------------
# 2. Split into chunks
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(docs)

# -----------------------------
# 3. Create embeddings
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# 4. Store in vector DB
# -----------------------------
vectorstore = FAISS.from_documents(chunks, embeddings)

# -----------------------------
# 5. Create Retriever
# -----------------------------
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# -----------------------------
# 6. Load LLM (local)
# -----------------------------
pipe = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)

llm = HuggingFacePipeline(pipeline=pipe)

# -----------------------------
# 7. Create RAG Chain
# -----------------------------
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# -----------------------------
# 8. Ask Questions
# -----------------------------
query = "What is system design?"
result = qa_chain.run(query)

print(result)