"""Example usage for Agentic Speculative Tool Call Dependency Graph & Parallel Batcher."""
from client import SpeculativeToolCallBatcher

if __name__ == "__main__":
    tools = [
        {"id": "t1", "name": "fetch_user_profile", "depends_on": []},
        {"id": "t2", "name": "fetch_account_balance", "depends_on": []},
        {"id": "t3", "name": "generate_summary_report", "depends_on": ["t1", "t2"]}
    ]
    res = SpeculativeToolCallBatcher.batch_tool_calls(tools)
    print("Execution Stages:", res["execution_stages_count"])
    print("Batches:", res["batches"])
