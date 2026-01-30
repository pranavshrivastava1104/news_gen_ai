# 📰 News Gen AI

An **AI-powered news summarization CLI tool** that fetches the latest news in real time and generates concise, source-grounded summaries using **Google Gemini** via **LangChain**.

This project combines **live web search**, **LLM-based reasoning**, and **prompt engineering** to produce reliable, up-to-date summaries strictly based on fetched news articles.

---

## 📌 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Project Architecture](#project-architecture)
* [Tech Stack](#tech-stack)
* [Folder Structure](#folder-structure)
* [How It Works](#how-it-works)
* [Installation & Setup](#installation--setup)
* [Environment Variables](#environment-variables)
* [Running the Project](#running-the-project)
* [Example Usage](#example-usage)
* [Prompt Design](#prompt-design)
* [Limitations](#limitations)
* [Future Improvements](#future-improvements)
* [License](#license)

---

## 🔍 Overview

**News Gen AI** is a command-line application that:

1. Fetches the **latest news articles** for a given topic using DuckDuckGo Search.
2. Feeds the retrieved articles into **Google Gemini (LLM)** via LangChain.
3. Generates a **5-bullet-point summary** grounded strictly in the retrieved news.
4. Appends **verifiable source URLs** for transparency.

The system ensures **low hallucination risk** by explicitly constraining the model to use only the provided news items.

---

## ✨ Features

* 🔎 Real-time news retrieval (DuckDuckGo)
* 🤖 LLM-powered summarization using Google Gemini
* 🧠 Prompt-controlled, source-grounded summaries
* 📎 Automatic citation of sources
* 💻 Interactive CLI interface
* 🔐 Secure API key management via `.env`

---

## 🏗 Project Architecture

```
User Input (Topic)
      ↓
DuckDuckGo News Search
      ↓
Structured News Items
      ↓
Prompt Template (LangChain)
      ↓
Google Gemini LLM
      ↓
Bullet-point Summary + Sources
```

---

## 🧰 Tech Stack

| Layer            | Technology                         |
| ---------------- | ---------------------------------- |
| Language         | Python 3.9+                        |
| LLM              | Google Gemini (`gemini-2.5-flash`) |
| Framework        | LangChain                          |
| Search Engine    | DuckDuckGo Search API              |
| Environment Mgmt | python-dotenv                      |
| Interface        | Command Line (CLI)                 |

---

## 📁 Folder Structure

```
news_gen_ai/
│
├── news_gemini_langchain.py   # Main application script
├── .env.example               # Environment variable template
├── .gitignore                 # Ignored files (.env, .venv, etc.)
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ How It Works

1. User enters a **news topic** via CLI.
2. DuckDuckGo returns the latest related news articles.
3. Articles are formatted into a structured text block.
4. A **LangChain prompt template** injects topic + articles into Gemini.
5. Gemini produces a **5-point summary** followed by **source URLs**.

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/news_gen_ai.git
cd news_gen_ai
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows PowerShell
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_gemini_api_key
```

> ⚠️ **Never commit `.env` to GitHub**. Use `.env.example` instead.

---

## ▶️ Running the Project

```bash
python news_gemini_langchain.py
```

You will be prompted to enter a topic:

```
Enter topic (or 'exit'): artificial intelligence
```

Type `exit` to stop the program.

---

## 🧪 Example Usage

**Input:**

```
Enter topic: electric vehicles
```

**Output:**

* EV adoption rises due to lower battery costs
* Major automakers expand EV production lines
* Government incentives accelerate market growth
* Charging infrastructure improves globally
* Analysts forecast strong EV sales in 2025

**Sources:**

* [https://example-news-1.com](https://example-news-1.com)
* [https://example-news-2.com](https://example-news-2.com)

---

## 🧠 Prompt Design

The summarization prompt enforces:

* Fixed bullet count
* Strict grounding to provided news
* Mandatory source citation

This significantly reduces hallucinations and improves trustworthiness.

---

## ⚠️ Limitations

* Depends on DuckDuckGo news availability
* Requires valid Google Gemini API key
* CLI-only (no web UI yet)
* No persistent storage of summaries

---

## 🔮 Future Improvements

* 🌐 Web UI using Streamlit / React
* 📊 Topic trend analysis
* 🗂 Multi-source news aggregation
* 🧪 Evaluation metrics (ROUGE, factuality)
* 🧠 RAG with vector database

---

## 📄 License

This project is licensed under the **MIT License**.

---

### 👤 Author

**Pranav Shrivastava**
AI / ML | Generative AI | LangChain | RAG

---

⭐ If you found this project useful, consider giving it a star on GitHub!
