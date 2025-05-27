from langchain import OpenAI, LLMChain, PromptTemplate
from integrators.calendar import CalendarIntegrator

calendar = CalendarIntegrator()

TEMPLATE = PromptTemplate(
    input_variables=["events"],
    template="""
Create a bullet‑point recap and action items for these meetings:

{events}

Recap:
"""
)
chain = LLMChain(llm=OpenAI(model_name="gpt-4"), prompt=TEMPLATE)

def run_meeting_recap(time_min, time_max):
    events = calendar.list_events(time_min=time_min, time_max=time_max)
    return chain.run(events=events)
