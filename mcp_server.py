"""MCP server for Agentic Speculative Tool Call Dependency Graph & Parallel Batcher."""
import sys
import json
from client import SpeculativeToolCallBatcher

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "batch_speculative_tool_calls",
                "description": "Constructs dependency DAGs and organizes tool invocations into parallel execution stages",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "tool_calls": {"type": "array"}
                    },
                    "required": ["tool_calls"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "batch_speculative_tool_calls":
            tools = params.get("arguments", {}).get("tool_calls", [])
            res = SpeculativeToolCallBatcher.batch_tool_calls(tools)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
