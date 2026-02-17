# 💹 AI Financial Analyst Team

An enterprise-grade multi-agent AI application that performs comprehensive financial research on public companies. Built with **CrewAI** for orchestration and **Streamlit** for the user interface.

## 🚀 Features

- **Multi-Agent Orchestration**: A team of 4 specialized AI agents working together:
  - 🕵️ **Financial Researcher**: Scrapes SEC filings, earnings calls, and financial metrics.
  - ⚔️ **Competitor Analyst**: Identifies rivals and compares market position/SWOT.
  - 📈 **Sentiment Analyst**: Analyzes news, social media, and analyst ratings.
  - ✍️ **Investment Writer**: Synthesizes all data into a professional investment report.
- **Hierarchical Delegation**: Uses a manager agent to coordinate tasks and ensure quality.
- **Real-time Web Search**: Powered by **SerperDev** for up-to-the-minute market data.
- **Modern UI**: A sleek, dark-mode Glassmorphism interface built with Streamlit.
- **Exportable Reports**: Generates detailed Markdown reports ready for download.

## 🛠️ Architecture

```mermaid
graph TD
    User[User Input: "Tesla"] --> Manager[Manager Agent]
    Manager --> Researcher[Financial Researcher]
    Manager --> Competitor[Competitor Analyst]
    Manager --> Sentiment[Sentiment Analyst]
    Researcher --> Data[SEC Filings/Earnings]
    Competitor --> Rivals[Competitor Analysis]
    Sentiment --> News[Market Sentiment]
    Data & Rivals & News --> Writer[Investment Writer]
    Writer --> Report[Final Investment Report]
```

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shubh-vedi/financial-analyst-team.git
   cd financial-analyst-team
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Configuration

You need valid API keys for:
- **OpenAI** (for GPT-4o capabilities)
- **Serper** (for Google Search capabilities)

You can enter these directly in the Streamlit Sidebar UI, or set them in a `.env` file (rename `.env.example` to `.env`).

## ▶️ Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** to `http://localhost:8501`.

3. **Enter API Keys** in the sidebar.

4. **Enter a company name** (e.g., "NVIDIA", "Apple", "TSLA") and click **Analyze**.

5. **Wait for the agents** to complete their research (1-3 minutes).

6. **Download** the final report.

## 📁 Project Structure

- `app.py`: Main Streamlit application and UI logic.
- `agents.py`: Definition of the 4 CrewAI agents and their roles.
- `tasks.py`: Specific research and writing tasks assigned to agents.
- `requirements.txt`: Python dependencies.

## ⚠️ Note on Signals
You may see a warning in the terminal: `ValueError: signal only works in main thread`. This is a known behavior when running CrewAI within Streamlit and does **not** affect functionality.

## 📄 License
MIT License
