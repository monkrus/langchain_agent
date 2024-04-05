# mistral_langchain_agent
- pip install -U langchain-cli
   
- langchain app new my-app --package retrieval-agent-fireworks
 
- Choose N to installing templates into your environment.
- Add import om the top of server.py file.

Like so : `from retrieval_agent_fireworks import agent_executor as retrieval_agent_fireworks_chain`
Add path on the same file as well : `"\retrieval-agent-fireworks")`

- pip install poetry
- poetry langchain serve
