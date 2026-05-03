from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

# -----------------------------
# 1. Load embeddings
# -----------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------
# 2. Load saved vector DB 
# FIX: Added allow_dangerous_deserialization=True
# -----------------------------
vectorstore = FAISS.load_local(
    "faiss_index", 
    embeddings, 
    allow_dangerous_deserialization=True
)

# -----------------------------
# 3. Create retriever
# -----------------------------
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# -----------------------------
# 4. Load LLM
# -----------------------------
pipe = pipeline(
    "text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)

llm = HuggingFacePipeline(pipeline=pipe)

# -----------------------------
# 5. Create Chain (Modern LCEL approach)
# -----------------------------
# Define the system prompt to give the AI context
system_prompt = (
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, say that you don't know. "
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Create the chains
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# -----------------------------
# 6. Chat loop
# -----------------------------
print("Chat with your PDF (type 'exit' to quit)\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    # result now contains 'input', 'context', and 'answer'
    response = rag_chain.invoke({"input": query})
    print("AI:", response["answer"])