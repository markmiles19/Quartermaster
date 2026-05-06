from crewai import Agent, Task, Crew

analyst = Agent(
    role="Financial Analyst",
    goal="Assess financial health and detect risks",
    backstory="Expert in small business cash flow and forecasting"
)

strategist = Agent(
    role="Financial Strategist",
    goal="Recommend actions to prevent negative cash flow",
    backstory="Specializes in cost reduction and payment prioritization"
)

def run_financial_analysis(financial_data, forecast):
    final_balance = forecast.get("final_balance", 0)

    analysis_task = Task(
        description=f"""
        You are given financial data and a projected final balance.

        Current Data:
        {financial_data}

        Forecast:
        Final Balance: {final_balance}

        Determine the financial risk level (low, medium, high) and explain why.
        """,
        agent=analyst,
        expected_output="A short explanation of the financial risk level (low, medium, or high)."
    )

    strategy_task = Task(
        description=f"""
        Based on the financial analysis and projected balance of {final_balance},
        recommend specific actions to prevent negative cash flow.

        Suggestions may include:
        - Reducing discretionary expenses
        - Prioritizing critical payments
        - Delaying non-essential spending

        Provide a clear, actionable recommendation.
        """,
        agent=strategist,
        expected_output="A clear action plan to maintain or improve cash flow."
    )

    crew = Crew(
        agents=[analyst, strategist],
        tasks=[analysis_task, strategy_task],
        verbose=True
    )

    result = crew.kickoff()
    return result