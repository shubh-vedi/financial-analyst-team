from crewai import Task

class FinancialCrewTasks:
    def research_task(self, agent, company_name):
        return Task(
            description=f"""
                Conduct a comprehensive financial research on {company_name}.
                1. Find the ticker symbol.
                2. Analyze the latest 10-K and 10-Q filings.
                3. Extract key financial metrics (Revenue, Net Income, P/E Ratio, Debt levels).
                4. Summarize the latest earnings call transcripts.
                Focus on the last fiscal year and the most recent quarter.
            """,
            expected_output="A detailed financial research report containing key metrics, filing summaries, and earnings highlights.",
            agent=agent
        )

    def competitor_task(self, agent, company_name):
        return Task(
            description=f"""
                Analyze the competitive landscape for {company_name}.
                1. Identify top 3 direct competitors.
                2. Compare {company_name}'s market share, product offerings, and pricing strategies against these competitors.
                3. detailed SWOT analysis (Strengths, Weaknesses, Opportunities, Threats) relative to competitors.
            """,
            expected_output="A comparative analysis report identifying key competitors and a SWOT analysis.",
            agent=agent
        )

    def sentiment_task(self, agent, company_name):
        return Task(
            description=f"""
                Analyze the market sentiment for {company_name}.
                1. Search for recent news articles (last 3 months) and identifying the prevailing tone (Positive, Negative, Neutral).
                2. Look for analyst ratings and price targets.
                3. summarizes key controversies or positive catalysts mentioned in the media.
            """,
            expected_output="A market sentiment report summarizing news tone, analyst ratings, and key catalysts.",
            agent=agent
        )

    def report_task(self, agent, company_name):
        return Task(
            description=f"""
                Synthesize all gathered research into a final investment report for {company_name}.
                The report must include:
                1. Executive Summary
                2. Financial Analysis (from Research Task)
                3. Competitive Landscape (from Competitor Task)
                4. Market Sentiment (from Sentiment Task)
                5. Investment Recommendation (Buy/Hold/Sell) with reasoning.
                
                Format the output as professional Markdown.
            """,
            expected_output="A final structured investment report in Markdown format, including a clear recommendation.",
            agent=agent,
            output_file="investment_report.md"
        )
