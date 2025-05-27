from langchain import OpenAI
from langchain.agents import initialize_agent, Tool
from integrations.gmail import GmailIntegrator
from integrations.asana import AsanaIntegrator

# Initialize tools for LIGHT
gmail = GmailIntegrator()
asana = AsanaIntegrator()

tools = [
    Tool(name="gmail", func=gmail.send_email, description="Send emails via Gmail"),
    Tool(name="asana", func=asana.update_task, description="Update tasks in Asana"),
]

llm = OpenAI(model_name="gpt-4")
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")


def process(user_id: str, query: str):
    """
    Core entrypoint for LIGHT queries
    """
    result = agent.run(query)
    return result
