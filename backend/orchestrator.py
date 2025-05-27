import os
from langchain import OpenAI
from langchain.agents import initialize_agent, Tool
from backend.integrators.gmail import GmailIntegrator
from backend.integrators.asana import AsanaIntegrator
from backend.integrators.calendar import CalendarIntegrator
from backend.pipelines.email_pipeline import run_email_summary
from backend.pipelines.task_pipeline import run_task_report
from backend.pipelines.meeting_pipeline import run_meeting_recap

# Tools wrapping our pipelines
gmail = GmailIntegrator()
asana = AsanaIntegrator()
calendar = CalendarIntegrator()

tools = [
    Tool(name="summarize_emails", func=lambda _: run_email_summary(), description="Summarize unread emails"),
    Tool(name="report_tasks", func=lambda _: run_task_report(os.environ.get("ASANA_PROJECT_GID")), description="Generate task status report"),
    Tool(name="recap_meetings", func=lambda _: run_meeting_recap(os.environ.get("TIME_MIN"), os.environ.get("TIME_MAX")), description="Recap meetings"),
]

llm = OpenAI(model_name="gpt-4")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def process(user_id: str, query: str):
    return agent.run(query)
