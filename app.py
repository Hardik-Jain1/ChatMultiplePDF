import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings


def get_vector_db(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
            
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    text_chunks = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPEN_API_KEY"))
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")



def user_input(user_question):
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPEN_API_KEY"))
    
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = OpenAI(openai_api_key=os.environ.get("OPEN_API_KEY"), temperature=0.3, verbose=True)
    
    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])
       


def main():
    st.set_page_config("RAG Based Search Tool")
    st.header("Chat with PDF using OpenAI💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files here", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                get_vector_db(pdf_docs)
                st.success("Done")

if __name__ == "__main__":
    main()