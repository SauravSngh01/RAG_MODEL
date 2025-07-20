==========================
RAG_MODEL SYSTEM OVERVIEW
==========================

Purpose and Scope
-----------------
This document provides a comprehensive overview of the RAG_MODEL repository, a document question-answering system built using Retrieval-Augmented Generation (RAG) techniques. This includes system purpose, capabilities, architecture, use cases, and dependencies.

Refer to:
- "Getting Started" for setup instructions.
- "System Architecture and Core Components" for technical details.

-----------------------------
What is RAG_MODEL?
-----------------------------
RAG_MODEL is a Python-based document Q&A system combining semantic search and large language model (LLM) generation to answer questions using local PDF documents.

Key Technologies:
- **Azure OpenAI (gpt-4o-mini)**: Natural language generation
- **HuggingFace (all-MiniLM-L6-v2)**: Document embeddings
- **LlamaIndex**: RAG orchestration and document processing

Codebase: main.py (lines 1-45)

-------------------------------
Core System Components
-------------------------------

Architecture Breakdown:

1. **User Interface**
   - `gr.Interface()` (lines 36–42)
   - `demo.launch()` (line 44)

2. **Data Sources**
   - Local PDFs in `data/` directory
   - `.env` file for API credentials

3. **main.py Components**
   - `load_dotenv()` → loads env vars
   - `AzureOpenAI()` → Azure LLM (lines 16–22)
   - `HuggingFaceEmbedding()` → embeddings (line 25)
   - `Settings.llm`, `Settings.embed_model` → LLM setup (lines 23, 26)
   - `SimpleDirectoryReader("data")` → load documents (line 28)
   - `VectorStoreIndex.from_documents()` → indexing (line 29)
   - `index.as_query_engine()` → enable query (line 30)
   - `answer_question(query)` → respond (lines 32–34)

4. **External APIs**
   - Azure OpenAI (gpt-4o-mini)
   - HuggingFace Transformers (sentence-transformers)

-------------------------------
Processing Flow and Data Pipeline
-------------------------------

**Initialization**
- Load documents:
  `documents = SimpleDirectoryReader('data').load_data()` (line 28)
- Build vector index:
  `index = VectorStoreIndex.from_documents(documents)` (line 29)
- Create query engine:
  `query_engine = index.as_query_engine()` (line 30)

**Runtime Flow**
- User enters a query in Gradio textbox
- `answer_question(query)` is triggered
- Inside:
  - `response = query_engine.query(query)` (line 33)
  - `return str(response)` (line 34)
- Result shown via Gradio interface

Data Flow:
- User Query → Semantic Retrieval → Context + Query → LLM Synthesis → Response

-------------------------------
Core Capabilities
-------------------------------

| Capability           | Implementation                      | Code Location      |
|----------------------|--------------------------------------|--------------------|
| Document Loading     | SimpleDirectoryReader("data")        | main.py, line 28   |
| Vector Indexing      | VectorStoreIndex.from_documents()    | main.py, line 29   |
| Semantic Search      | query_engine.query()                 | main.py, line 33   |
| Answer Generation    | AzureOpenAI LLM                      | main.py, 16–22     |
| Web Interface        | gr.Interface()                       | main.py, 36–42     |
| Config Management    | load_dotenv(), os.getenv()           | main.py, 8–14      |

-------------------------------
Target Use Cases
-------------------------------

**Primary Use Cases**
- Document Research
- Knowledge Base Exploration
- Prototype RAG Development
- Educational Demos

**Technical Characteristics**
- Local single-user system
- PDF input documents
- Requires Azure & HuggingFace APIs
- Memory-based (no persistent index)

**Limitations**
- No multi-user support
- No persistent document storage
- PDF-only format via SimpleDirectoryReader
- Requires internet connection

-------------------------------
System Dependencies
-------------------------------

| Component        | Purpose                        | Config Location     |
|------------------|--------------------------------|---------------------|
| Azure OpenAI     | Text generation (gpt-4o-mini)  | main.py, 16–23      |
| HuggingFace      | Text embeddings                | main.py, 25–26      |
| LlamaIndex       | RAG pipeline                   | main.py, line 3     |
| Gradio           | Web interface                  | main.py, 36–44      |
| Env Variables    | API keys & config              | main.py, 8–14       |

Refer to:
- "Configuration and Environment" for setup
- "Core Components" for detailed docs

Sources: main.py (lines 1–45)
 
=======================================
RAG_MODEL Setup and Usage Guide
=======================================

Overview
--------
This document provides step-by-step instructions for setting up and running the RAG_MODEL document question-answering system. It includes environment configuration, API key setup, document preparation, and application launch procedures.

For system architecture, see: System Architecture
For environment options, see: Configuration and Environment

=========================
Prerequisites
=========================

Requirement             | Description                            | Purpose
------------------------|----------------------------------------|-----------------------------------
Python 3.8+             | Python runtime environment              | Core application runtime
Azure OpenAI API access| Azure subscription + API key           | Text generation
HuggingFace API token  | HuggingFace access token               | Document embeddings
PDF documents           | Local PDFs in 'data/' directory        | Knowledge base

=========================
1. Install Dependencies
=========================

Install required Python packages:

pip install gradio llama-index python-dotenv
pip install llama-index-embeddings-huggingface
pip install llama-index-llms-azure-openai

Setup Flow:
-----------
1. Install Python dependencies
2. Create `.env` file
3. Configure API keys
4. Create `data/` directory
5. Add your PDF documents
6. Run `main.py`
7. Access Gradio interface

Required Environment Variables:
-------------------------------
- AZURE_OPENAI_KEY
- AZURE_OPENAI_ENDPOINT
- HUGGINGFACEHUB_API_TOKEN

(Sources: main.py lines 1–7)

=========================
2. Environment Configuration
=========================

Create a `.env` file in the root project directory:

AZURE_OPENAI_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token

Loaded using `load_dotenv()` and accessed via `os.getenv()`

(Sources: main.py lines 5, 8, 10, 12–13)

=========================
3. Directory Structure
=========================

Structure:
RAG_MODEL/
├── main.py
├── .env
└── data/
    └── [your-pdf-files.pdf]

Documents are loaded by: SimpleDirectoryReader("data")

(Source: main.py line 28)

=========================
Configuration Details
=========================

Azure OpenAI Settings:
-----------------------
| Parameter        | Value                    | Source         |
|------------------|--------------------------|----------------|
| model            | "gpt-4o-mini"            | main.py line 17|
| deployment_name  | "gpt-4o-mini"            | main.py line 18|
| api_key          | from .env                | main.py line 19|
| azure_endpoint   | from .env                | main.py line 20|
| api_version      | "2024-08-01-preview"     | main.py line 21|

HuggingFace Settings:
----------------------
- Model: `sentence-transformers/all-MiniLM-L6-v2`
- Configured via: `HuggingFaceEmbedding`

(Source: main.py lines 25–26)

=========================
Application Initialization
=========================

Step-by-step execution:

1. `load_dotenv()`
2. Read env vars for Azure + HuggingFace
3. Initialize `AzureOpenAI` client
4. Set `Settings.llm`
5. Initialize `HuggingFaceEmbedding`
6. Set `Settings.embed_model`
7. Load PDFs via `SimpleDirectoryReader('data')`
8. Build index: `VectorStoreIndex.from_documents(documents)`
9. Create query engine: `index.as_query_engine()`
10. Setup Gradio Interface and launch: `demo.launch()`

(Sources: main.py lines 8–44)

=========================
Running the Application
=========================

To start the app:
python main.py

What happens:
-------------
- Loads environment variables
- Configures LLM and embeddings
- Indexes PDF documents
- Launches Gradio web UI

Web Interface:
--------------
- Title: Document Q&A with LlamaIndex + Hugging Face
- Input: Multi-line question text box
- Output: Answer generated using retrieved document context

=========================
Query Processing Flow
=========================

User submits query → 
`answer_question()` →
`query_engine.query(query)` →
Semantic document retrieval →
Context passed to LLM →
Response generated by Azure GPT-4o-mini →
Displayed via Gradio

(Sources: main.py lines 32–44)

=========================
First Steps and Usage
=========================

1. Prepare Documents
--------------------
- Place PDFs in `data/`
- Auto-discovered by `SimpleDirectoryReader`
- Processed at startup

2. Ask Questions
-----------------
- Use Gradio interface textbox
- Questions must relate to your documents
- Semantic search finds relevant chunks
- GPT-4o-mini generates the response

3. Expected Behavior
---------------------
- First run may take time (indexing)
- Later queries are faster
- Session memory retained during runtime

(Sources: main.py lines 28–34, 36–44)
