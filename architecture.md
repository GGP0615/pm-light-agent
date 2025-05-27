# LIGHT Architecture

```text
[ Slack ]
     ↕  Events & UI
[ Bolt App ] → [ Orchestrator ] → [ Pipelines ]
                                 ↳ [ Vector DB (Pinecone) ]
                                 ↳ [ Integrators ] → External APIs
