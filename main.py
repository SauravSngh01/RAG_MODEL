import os
import gradio as gr
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv
from llama_index.llms.azure_openai import AzureOpenAI

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

api_key = os.getenv("AZURE_OPENAI_KEY")
azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
api_version = "2023-07-01-preview"

llm = AzureOpenAI(
    model="gpt-4o-mini",
    deployment_name="gpt-4o-mini",
    api_key=api_key,
    azure_endpoint=azure_endpoint,
    api_version="2024-08-01-preview",
)
Settings.llm = llm

embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
Settings.embed_model = embed_model

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

def answer_question(query):
    response = query_engine.query(query)
    return str(response)

demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(lines=2, placeholder="Ask a question about the document..."),
    outputs="text",
    title="Document Q&A with LlamaIndex + Hugging Face",
    description="Ask questions about the content of the PDF file (1.pdf)"
)

demo.launch()
