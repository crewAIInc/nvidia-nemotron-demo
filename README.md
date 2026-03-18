# SalesIntelligenceResearchAutomation Crew

Welcome to the SalesIntelligenceResearchAutomation Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/sales_intelligence_research_automation/config/agents.yaml` to define your agents
- Modify `src/sales_intelligence_research_automation/config/tasks.yaml` to define your tasks
- Modify `src/sales_intelligence_research_automation/crew.py` to add your own logic, tools and specific args
- Modify `src/sales_intelligence_research_automation/main.py` to add custom inputs for your agents and tasks

## Running the Project

There are two ways to run this project:

### Option 1: CLI

From the root folder of the project, run:

```bash
crewai run
```

This uses the crew defined in `src/sales_intelligence_research_automation/crew.py` with the YAML configs under `config/`. Make sure your API keys are set in the `.env` file.

### Option 2: Jupyter Notebook

Open `demo.ipynb` at the project root for a self-contained, interactive demo. The notebook inlines all agent and task definitions so you can read, tweak, and run everything cell-by-cell without needing to understand the project structure. It will prompt for API keys via `getpass` so no secrets are stored in the notebook.

```bash
jupyter notebook demo.ipynb
```

## Understanding Your Crew

The sales_intelligence_research_automation Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the SalesIntelligenceResearchAutomation Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
