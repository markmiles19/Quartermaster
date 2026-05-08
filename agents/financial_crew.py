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

        STEP 1: Determine the financial risk level:
        - low
        - medium
        - high

        STEP 2: Choose whether a tool is needed:

        1. forecast
        - Use this if cash flow projections should be recalculated
        or future financial trends require deeper analysis.
        - Example use case:
        uncertain cash runway or changing daily net values.

        2. email
        - Use this if management or stakeholders should be notified.
        - Example use case:
        severe financial risk requiring escalation.
        
        YOU MUST RESPOND IN EXACT FORMAT:

        RISK: <low|medium|high>

        TOOL: <forecast|email|none>

        REASON: <brief explanation>

        If no tool is necessary, do not select one.
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