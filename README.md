# agentic_agno

# Agentic AI YouTube Video Analyzer

An Agentic AI application that analyzes YouTube videos and generates structured insights using AI.

## Features

* YouTube video analysis
* Transcript-based content processing
* AI-generated summaries
* Key topic identification
* Timestamp-based analysis
* Key learning points
* Structured analysis reports
* Interactive Streamlit interface
* Downloadable analysis reports

## Tech Stack

* Python
* Agno
* Groq
* YouTube Transcript API
* Streamlit
* SQLite

## Project Structure

```text
agentic-ai-youtube-analyzer/
│
├── agent.py
├── finance.py
├── memory.py
├── team.py
├── youtube_analyzer.py
├── ui.py
├── README.md
├── .gitignore
└── requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd agentic-ai-youtube-analyzer
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### 6. Run the application

```bash
streamlit run ui.py
```

## Developer

**Madhu Patel**

B.Tech Data Science
