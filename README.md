# Install poetry
- Install pipx using pip in **CMD** `python -m pip install --user pipx`
- Ensure pipx's binary directory is in your PATH `python -m pipx ensurepath`
- Restart your terminal
- Run `pipx install poetry`
- Check the version `run poetry --version`

# Install LangChain CLI
- pip install -U langchain-cli
# Create new app   
- langchain app new my-app --package retrieval-agent-fireworks

- Choose **N** to installing templates into your environment.
  Add import om the top of server.py file, 
 `from retrieval_agent_fireworks import agent_executor as retrieval_agent_fireworks_chain`
  Add path on the same file as well  `"\retrieval-agent-fireworks")`

- poetry run langchain serve
