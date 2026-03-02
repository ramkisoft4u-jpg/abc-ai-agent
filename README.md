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


