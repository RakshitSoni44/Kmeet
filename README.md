# Job & Internship Search – Agentic AI System

An Agentic AI-based Job & Internship Finder that autonomously searches opportunities from the web, filters them based on user eligibility, and generates tailored CV bullet points to improve application success.

This project demonstrates end-to-end AI agent design using LLM reasoning, tool orchestration, vector similarity search, and FastAPI.

---

## Features

- Job & Internship Research Agent  
  - Searches the web using user-provided keywords  
  - Collects opportunities from multiple job platforms  

- Eligibility & Filtering Agent  
  - Matches jobs with user resume and preferences  
  - Uses semantic similarity (embeddings + vector database)  
  - Ranks jobs based on skill, experience, and role fit  

- CV Optimization Agent  
  - Generates ATS-friendly CV bullet points  
  - Aligns resume content with job descriptions  
  - Improves shortlisting probability  

- FastAPI Backend  
  - Modular API endpoints  
  - Easy integration with frontend or other services  

---

## Project Architecture

The system follows an Agent → Tool → Memory → API design pattern.

User Input  
↓  
Research Agent (Web Search)  
↓  
Filtering Agent (Eligibility + Ranking)  
↓  
CV Suggestion Agent  
↓  
Final Job Matches + CV Points  

---

## Repository Structure

```
job-intern-ai-agent/
│
├── services/
│   ├── agent.py                # Core AI agent logic
│   ├── planner.py              # Agent orchestration (optional)
│   └── memory.py               # Vector DB & embeddings
│
├── tools/
│   ├── job_research_tool.py    # Web search & scraping
│   ├── filter_tool.py          # Eligibility & ranking
│   ├── cv_suggestion_tool.py   # Resume optimization
│   └── alag_alag_tool_names.py # Tool registry
│
├── apis/
│   ├── job_search_api.py
│   ├── filter_api.py
│   └── cv_api.py
│
├── models/
│   ├── resume_schema.py
│   └── job_schema.py
│
├── utils/
│   ├── resume_parser.py
│   ├── prompt_templates.py
│   └── logger.py
│
├── data/
│   ├── embeddings/
│   └── temp/
│
├── main.py                     # FastAPI app entry
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Tech Stack

- LLMs: OpenAI / Claude / Llama  
- Agent Framework: LangChain / CrewAI  
- Embeddings: OpenAI / Sentence-Transformers  
- Vector Database: FAISS / ChromaDB  
- Backend: FastAPI + Uvicorn  
- Search / Scraping: Tavily, SerpAPI, Playwright  

---

## Setup Instructions

### Clone the repository
```
git clone https://github.com/your-username/job-intern-ai-agent.git
cd job-intern-ai-agent
```

### Create virtual environment
```
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Run the server
```
uvicorn main:app --reload
```

Server will start at:
http://127.0.0.1:8000

---

## Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key
SERP_API_KEY=your_key
```

`.env` and `.venv` are ignored using `.gitignore`.

---

## Project Timeline

- Day 1: Agent design and tool planning  
- Week 1: Core agent development, APIs, filtering logic  
- Phase 2: UI integration and deployment  

---

## Why This Project?

- Demonstrates real-world Agentic AI concepts  
- Uses LLM reasoning and tool orchestration  
- Production-ready architecture  
- Strong resume and interview value  

---

## License

This project is for educational and research purposes only.
