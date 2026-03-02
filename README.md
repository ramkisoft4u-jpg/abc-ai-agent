# ABC AI Agent (RAG + LangChain + HuggingFace/Groq)

This project turns ABC REST APIs into an AI Agent using:

- LangChain
- RAG (FAISS vector store)
- HuggingFace or Groq LLMs
- FastAPI backend
- Custom LangChain Tools that call SMP APIs

## Setup



# SMP AI Agent (LangChain + LangGraph + RAG + MySQL)

This project implements a multi-agent workflow for SMP:

- Validate user input (dates, product, reservationId)
- Check dose availability via SMP APIs
- Create hold reservations
- Create orders in MySQL `smp.order`
- Release/delete reservations
- Use RAG over SMP docs
- Orchestrate with LangGraph

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env





smp-ai-agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── ingest.py
│   │   ├── pipeline.py
│   │   └── vectorstore/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── orchestrator_agent.py
│   │   ├── demand_planning_agent.py
│   │   ├── order_agent.py
│   │   └── reservation_agent.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── smp_api_tools.py
│   │   └── mysql_tools.py
│   ├── graph/
│   │   ├── __init__.py
│   │   └── workflow.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── order.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   └── reservation.py
│   └── utils/
│       ├── __init__.py
│       └── date_utils.py
│
├── data/
│   └── knowledge_base/
│       └── (PDFs, Markdown, SOPs, API docs)
│
├── scripts/
│   ├── ingest_docs.py
│   └── init_db.py
│
├── tests/
│   ├── __init__.py
│   ├── test_agents.py
│   ├── test_graph.py
│   └── test_api.py
│
├── .env.example
├── requirements.txt
├── README.md
└── Dockerfile



