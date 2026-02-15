import streamlit as st
import os
import sys
import time
from crewai import Crew, Process
from agents import FinancialCrewAgents
from tasks import FinancialCrewTasks

# Page Config
st.set_page_config(
    page_title="AI Financial Analyst Team",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar: Configuration ---
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    
    # API Keys (Ideally from env, but editable)
    openai_key = st.text_input("OpenAI API Key", type="password", placeholder="sk-...", help="Required for GPT-4")
    serper_key = st.text_input("Serper API Key", type="password", placeholder="Search API...", help="Required for Web Search")
    
    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key
    if serper_key:
        os.environ["SERPER_API_KEY"] = serper_key
        
    st.markdown("---")
    st.markdown("### 🤖 The Crew")
    st.markdown("""
    - **Financial Researcher**: Digs into SEC filings
    - **Competitor Analyst**: Scouts the rivals
    - **Sentiment Analyst**: Gauges the market mood
    - **Investment Writer**: Crafts the final report
    """)

# --- Main Interface ---
st.title("AI Financial Analyst Team 💹")
st.markdown("### Enterprise-grade financial research powered by Multi-Agent AI")

# Input Section
with st.container():
    company_name = st.text_input("Enter Company Name or Ticker", "Tesla (TSLA)")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        run_btn = st.button("🚀 Analyze Company")
    with col2:
        st.empty() # Spacer

# Execution Logic
if run_btn:
    if not os.environ.get("OPENAI_API_KEY") or not os.environ.get("SERPER_API_KEY"):
        st.error("Please provide valid API Keys in the sidebar to proceed.")
    else:
        # Placeholder for real-time logs
        status_container = st.container()
        
        with status_container:
            st.markdown("### 🔄 Analysis in Progress...")
            prog_bar = st.progress(0)
            status_text = st.empty()
            
            # 1. Instantiate Agents
            status_text.text("Recruiting analysts...")
            prog_bar.progress(10)
            
            agents = FinancialCrewAgents()
            researcher = agents.financial_researcher()
            competitor_analyst = agents.competitor_analyst()
            sentiment_analyst = agents.sentiment_analyst()
            writer = agents.investment_writer()
            
            # 2. Instantiate Tasks
            status_text.text("Assigning tasks...")
            prog_bar.progress(20)
            
            tasks = FinancialCrewTasks()
            task1 = tasks.research_task(researcher, company_name)
            task2 = tasks.competitor_task(competitor_analyst, company_name)
            task3 = tasks.sentiment_task(sentiment_analyst, company_name)
            task4 = tasks.report_task(writer, company_name)
            
            # 3. Create Crew
            crew = Crew(
                agents=[researcher, competitor_analyst, sentiment_analyst, writer],
                tasks=[task1, task2, task3, task4],
                process=Process.hierarchical,
                manager_llm=agents.llm,
                verbose=True
            )
            
            st.write("Crew Assembled. Starting mission...")
            
            # 4. Kickoff
            with st.spinner("Agents are working... this might take a minute or two."):
                try:
                    result = str(crew.kickoff())
                    prog_bar.progress(100)
                    status_text.text("Analysis Complete!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    result = None

        # Output Display
        if result:
            st.markdown("## 📊 Investment Report")
            st.markdown(result)
            
            # Download Button
            st.download_button(
                label="📥 Download Report as Markdown",
                data=result,
                file_name=f"{company_name}_Investment_Report.md",
                mime="text/markdown"
            )
