from langchain import LLMChain, PromptTemplate
from integrators.gmail import GmailIntegrator

gmail = GmailIntegrator()

TEMPLATE = PromptTemplate(
    input_variables=["thread"],
    template="""
Summarize this email thread into a short stakeholder update:

{text=thread['snippet']}

Summary:
"""
)
chain = LLMChain(llm=OpenAI(model_name="gpt-4"), prompt=TEMPLATE)

def run_email_summary(max_threads=3):
    threads = gmail.list_unread(max_threads)
    results = []
    for t in threads:
        summary = chain.run(thread=t)
        results.append({'thread_id': t['id'], 'summary': summary})
    return results
