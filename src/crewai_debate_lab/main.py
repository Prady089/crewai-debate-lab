from dotenv import load_dotenv
load_dotenv()

from crewai_debate_lab.crew import DebateCrew


def run():
    result = DebateCrew().crew().kickoff(
        inputs={
            "motion": "Should small businesses adopt agentic AI for BI automation?"
        }
    )
    print(result.raw)


if __name__ == "__main__":
    run()
