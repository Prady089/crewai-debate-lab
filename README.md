CrewAI Debate Lab

CrewAI Debate Lab is a multi-agent AI system built using CrewAI, OpenAI, and uv that simulates a structured debate on any user-provided motion.
It demonstrates how multiple AI agents can collaborate, argue opposing viewpoints, and arrive at a reasoned decision — similar to real-world policy analysis, consulting discussions, and decision-intelligence workflows.

✨ Key Features

🧩 Multi-Agent Architecture

Debater agent argues for and against a motion

Judge agent evaluates arguments and decides the winner

🗣️ User-Driven Input

Debate motion is provided at runtime via CLI

No code changes required per run

🔁 Sequential Reasoning

Propose → Oppose → Decide

Transparent, step-by-step execution

📄 Persistent Outputs

Each agent’s output is saved as Markdown files

Easy to audit, review, or reuse

⚙️ Production-Grade Setup

Uses uv for fast dependency management

GitHub Actions CI workflow included

Secure secrets handling via GitHub Secrets

📂 Project Structure
crewai-debate-lab/
├── src/
│   └── crewai_debate_lab/
│       ├── __init__.py
│       ├── crew.py
│       ├── main.py
│       └── config/
│           ├── agents.yaml
│           └── tasks.yaml
├── output/               # Generated debate outputs (markdown)
├── .github/workflows/
│   └── crewai.yml        # GitHub Actions CI
├── pyproject.toml
├── README.md

🚀 Getting Started
1️⃣ Prerequisites

Python 3.12+

An OpenAI API key

uv installed

2️⃣ Install Dependencies
pip install uv
uv sync

3️⃣ Set Environment Variable
Locally
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"

GitHub Actions / Codespaces

Add OPENAI_API_KEY as a GitHub Secret.

4️⃣ Run a Debate
uv run python -m crewai_debate_lab.main \
  --motion "Should small businesses adopt agentic AI for BI automation?"

📊 Outputs

After execution, results are written to:

output/
├── propose.md   # Argument in favor
├── oppose.md    # Argument against
└── decide.md    # Final judgment


This design supports explainability, auditability, and real-world decision workflows.

🤖 How It Works

Debater Agent

Generates a strong argument for the motion

Generates a strong argument against the motion

Judge Agent

Reviews both arguments

Selects the more convincing position

Explains the reasoning clearly

All agents are powered by OpenAI models and coordinated using CrewAI’s orchestration framework.

🛡️ Security & Best Practices

❌ API keys are never committed

✅ Secrets are injected via GitHub Secrets

✅ .env files are excluded from version control

✅ CI runs safely without exposing credentials

🔮 Future Enhancements (Optional)

This project is intentionally kept minimal, but can be extended to include:

Background research agents

Web search + citations

Multiple debate rounds

Scoring & confidence metrics

Web UI (Streamlit / FastAPI)

Local LLM support (Ollama)

📜 License

MIT License — feel free to fork, extend, and experiment.

👤 Author

Pradeep Kumar
GitHub: @Prady089
