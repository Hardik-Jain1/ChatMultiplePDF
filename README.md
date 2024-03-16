# ChatMultiplePDF
A RAG model uses the LangChain and OpenAI to chat with multiple PDFs.

This app is to let users load multiple PDF files and ask questions about it, with LangChain and OpenAI API working together to find precise answers from the PDFs.

![alt_text](https://github.com/Hardik-Jain1/ChatPDF/blob/main/chatpdf_img.jpg)

**PDFs + Question ------------>**  **LangChain + OpenAI + Streamlit** **------------> Response**


Features:
* PDF Upload: Users can upload one or multiple PDF documents containing information.
* Interactive Querying: Users can ask questions related to the content of the uploaded PDF documents.
* Contextual Answering: The application utilizes OpenAI's language model to provide detailed answers based on the context of the documents.

Installation:
* Clone the repository: git clone https://github.com/Hardik-Jain1/ChatMultiplePDF.git
* Navigate to the project directory: cd pdf-chat-openai
* Install dependencies: pip install -r requirements.txt

Configuration:
* Obtain an API key for OpenAI and store it in a .env file as OPEN_API_KEY=your_api_key.

Usage:
* Run the application: streamlit run app.py
* Access the application through the provided URL in the terminal.
* Upload PDF documents using the file uploader in the sidebar.
* Ask questions related to the content of the uploaded PDF documents in the text input field.
* Click on "Submit & Process" to generate answers based on the questions asked.
