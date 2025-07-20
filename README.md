===============================
RAG_MODEL SYSTEM OVERVIEW
===============================

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
