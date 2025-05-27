from langchain import OpenAI, LLMChain, PromptTemplate
from integrators.asana import AsanaIntegrator

asana = AsanaIntegrator()

TEMPLATE = PromptTemplate(
    input_variables=["tasks"],
    template="""
Generate a concise status report for the following tasks:

{tasks}

Report:
"""
)
chain = LLMChain(llm=OpenAI(model_name="gpt-4"), prompt=TEMPLATE)

def run_task_report(project_gid):
    tasks = list(asana.list_tasks(project_gid, opt_fields=['name','due_on','completed']))
    return chain.run(tasks=tasks)
