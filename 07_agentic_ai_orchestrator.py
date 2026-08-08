import re

print("="*65)
print("  NomaanOS - Autonomous Security Agent (ReAct Framework)")
print("="*65)

# Simulated System Tools
def tool_threat_scanner(query):
    return "[Tool Output]: Scanned network payload -> High Packet Rate anomaly detected (THREAT)"

def tool_rag_search(query):
    return "[Tool Output]: RAG Context -> 'Local private AI models maintain data sovereignty on edge.'"

# Agent Thought & Action Loop Engine
class SecurityAgent:
    def __init__(self):
        self.tools = {
            "threat_scanner": tool_threat_scanner,
            "rag_search": tool_rag_search
        }

    def plan_and_execute(self, user_prompt):
        print(f"\n[+] User Instruction: '{user_prompt}'")
        
        # 1. Reasoning Step (Thought)
        if "threat" in user_prompt.lower() or "scan" in user_prompt.lower():
            action = "threat_scanner"
            thought = "User wants system security assessment. Invoking Threat Scanner Tool."
        elif "privacy" in user_prompt.lower() or "ai" in user_prompt.lower() or "sovereignty" in user_prompt.lower():
            action = "rag_search"
            thought = "User asked about AI architecture/privacy. Invoking Vector RAG Tool."
        else:
            action = None
            thought = "No specific tool required. Direct knowledge response."

        print(f" -> Thought: {thought}")
        
        # 2. Action Step (Execution)
        if action in self.tools:
            print(f" -> Executing Action: tool_{action}()")
            observation = self.tools[action](user_prompt)
            print(f" -> Observation: {observation}")
            final_response = f"Agent Action completed successfully using {action}."
        else:
            final_response = "General response generated without tool calls."

        return final_response

# Run Agent Simulation
agent = SecurityAgent()

print("\n--- Test Scenario 1: Automated Security Inspection ---")
res1 = agent.plan_and_execute("Perform a scan on incoming network payload for threats.")

print("\n--- Test Scenario 2: Knowledge Query Retrieval ---")
res2 = agent.plan_and_execute("Explain how private AI handles data sovereignty on edge.")

print("\n[🚀 Agent Status]: ReAct Autonomous Loop Successfully Executed!")
