# RevMind AI – Full-Stack Take-Home Assignment

## NovaBite Consumer Goods Conversational Insights Platform

A miniature business intelligence platform for **NovaBite Consumer Goods** that allows sales managers to:

* View business KPIs and revenue trends
* Ask natural language questions about sales data
* Receive AI-generated business insights powered by an LLM

---

# Tech Stack

## Backend

* Python 3.13
* FastAPI
* SQLite
* SQLAlchemy
* Pandas
* uv package manager
* Groq API (Llama 3.3 70B Versatile)

## Frontend

* Next.js 15 (App Router)
* TypeScript
* Tailwind CSS
* Axios
* Recharts

## Database

* SQLite

## Containerization

* Docker
* Docker Compose

---

# Project Structure

```text
revmind/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database.py
│   │   ├── config.py
│   │   └── main.py
│   ├── seed.py
│   ├── sales.db
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── Dockerfile
│   └── .env
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   ├── Dockerfile
│   └── .env.local
│
├── data/
│   └── novabite_sales_data.csv
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

# Features

## Dashboard

* Total Net Revenue KPI
* Gross Profit Margin KPI
* Top Region KPI
* Monthly Revenue Trend Chart

## Conversational Insights Chatbot

Supports natural language questions such as:

* Which region had the highest net revenue in Q1 2024?
* What is the gross profit margin for the Snacks category?
* Which sales rep closed the most units in 2025?
* Compare E-Commerce vs Modern Trade net revenue.
* What was the best performing product in the West region?

---

# API Endpoints

## Products

```http
GET /api/products
```

Returns:

```json
[
  {
    "product_name": "...",
    "total_net_revenue": 1000,
    "total_units": 200
  }
]
```

---

## Summary

```http
GET /api/summary
```

Returns:

```json
{
  "total_net_revenue": 123456,
  "total_units": 5000,
  "gross_profit_margin": 32.5,
  "top_region": "West",
  "top_channel": "E-Commerce",
  "top_product": "Nova Chips"
}
```

---

## Trends

```http
GET /api/trends
```

Returns:

```json
[
  {
    "month": "2024-01",
    "revenue": 12345
  }
]
```

---

## Chat

```http
POST /api/chat
```

Request:

```json
{
  "question": "Which region had the highest net revenue in Q1 2024?"
}
```

Response:

```json
{
  "answer": "West region had the highest net revenue in Q1 2024 with revenue of $..."
}
```

---

# Why Groq + Llama 3.3 70B?

I used **Groq's hosted Llama 3.3 70B Versatile model** because:

* Fast inference speed
* Free developer tier
* High-quality reasoning for analytical questions
* Easy integration through Python SDK
* Suitable for conversational business intelligence applications

---

# Prompt Design

The chatbot uses:

1. User question
2. SQL-generated business context
3. Structured instructions

Example prompt:

```text
You are NovaBite's business analytics assistant.

Question:
<user question>

Data:
<SQL query results>

Rules:
1. Use only the provided data.
2. Do not hallucinate.
3. Mention exact numbers.
4. Keep answers concise.
5. If information is unavailable, clearly state it.
```

This reduces hallucination and ensures responses remain grounded in the dataset.

---

# Running Locally (Without Docker)

## Prerequisites

* Python 3.13+
* Node.js 22+
* npm
* uv package manager

Install uv:

Linux/macOS:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

# Backend Setup

## Step 1

```bash
git clone <repository-url>
cd revmind/backend
```

## Step 2

Create environment file:

```bash
cp ../.env.example .env
```

Edit:

```env
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

## Step 3

Install dependencies:

```bash
uv sync
```

## Step 4

Seed database:

```bash
uv run python seed.py
```

## Step 5

Run backend:

```bash
uv run uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# Frontend Setup

## Step 1

```bash
cd ../frontend
npm install
```

## Step 2

Create:

```text
.env.local
```

Contents:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

## Step 3

Run:

```bash
npm run dev
```

Frontend:

```text
http://localhost:3000
```

Chat:

```text
http://localhost:3000/chat
```

---

# Running With Docker

## Build

```bash
docker compose build
```

## Run

```bash
docker compose up
```

or

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:3000
```

Backend:

```text
http://localhost:8000/docs
```

---

# Example Chat Questions

```text
Which region had the highest net revenue in Q1 2024?

What is the gross profit margin for the Snacks category?

Which sales rep closed the most units in 2025?

Compare E-Commerce vs Modern Trade net revenue.

What was the best performing product in the West region?
```

---

# Tradeoffs and Shortcuts

* Used SQLite instead of PostgreSQL for simplicity.
* Implemented rule-based SQL context extraction instead of full Text-to-SQL generation.
* Limited chatbot scope to business analytics supported by the provided dataset.
* No authentication implemented because it was not required by the assignment.

---

# Improvements With More Time

* Streaming responses from the LLM
* Full Text-to-SQL generation
* Chat history persistence
* Unit and integration tests
* Revenue by region and category visualizations
* User authentication and role-based access
* Caching frequently asked questions
* Production deployment with CI/CD pipelines

---

# Author

**Dibyajyoti Bose**

Full-Stack Engineer Candidate – RevMind AI Take-Home Assignment
