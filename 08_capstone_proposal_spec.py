import json

print("="*65)
print("  NomaanOS - IHFC IIT Delhi Capstone Architecture Generator")
print("="*65)

proposal_data = {
    "project_title": "NomaanOS Shield: Autonomous Edge Security & Threat Triaging via Local GenAI Agents",
    "scholar": "Nomaan Khan",
    "institution": "IHFC - Technology Innovation Hub of IIT Delhi x Simplilearn x Microsoft",
    "core_problem": "Traditional Cloud SOCs suffer from high latency (minutes to hours) and expose sensitive network telemetry logs to third-party APIs during zero-day threat analysis.",
    "proposed_solution": "An edge-native, zero-leakage security orchestrator running local ML/DL models (KNN/K-Means/Perceptron) paired with a ReAct Agentic RAG framework for sub-second automated threat containment.",
    "technical_stack": [
        "Statistical Analytics Engine (iSH Native)",
        "Supervised ML Threat Classifier (Pure Math KNN & Linear Regression)",
        "Unsupervised Anomaly Detector (K-Means Clustering)",
        "Deep Learning Perceptron Neural Network",
        "Vector Cosine Similarity RAG Context Injection Engine",
        "ReAct Agentic AI Orchestrator Loop"
    ],
    "key_differentiator": "100% Data Sovereignty: All inference, vector similarity search, and agentic tool invocation happen on-device (constrained edge nodes) without external cloud dependencies."
}

# Generate Markdown Capstone Document
md_content = f"""# 🛡️ Capstone Project Proposal: {proposal_data['project_title']}

**Scholar:** {proposal_data['scholar']}  
**Institution:** {proposal_data['institution']}  

---

## 📌 Executive Summary
{proposal_data['core_problem']}

**NomaanOS Shield** addresses this by providing:  
_{proposal_data['proposed_solution']}_

---

## 🏗️ Integrated Engine Architecture

| Layer / Module | Built-in Engine | Functionality |
| :--- | :--- | :--- |
| **Data Engine** | `01_data_science_basics.py` | Local telemetry parsing & metrics calculation |
| **Predictive Analytics** | `02_linear_regression_engine.py` | Resource utilization & load trend forecasting |
| **Classification** | `03_knn_classification_engine.py` | Real-time network packet threat categorization |
| **Anomaly Detection** | `04_kmeans_clustering_engine.py` | Unsupervised zero-day traffic cluster isolation |
| **Neural Network** | `05_perceptron_neural_network.py` | Decision-gate threat scoring via backpropagation |
| **RAG Knowledge Base** | `06_vector_similarity_rag_engine.py` | Context retrieval via Vector Cosine Similarity |
| **Agentic Loop** | `07_agentic_ai_orchestrator.py` | ReAct Framework (Reasoning + Automated Tool Action) |

---

## 🔒 Key Differentiator
> **{proposal_data['key_differentiator']}**

---
*Generated & Managed via NomaanOS Lab Suite Engine (`08_capstone_proposal_spec.py`)*
"""

with open("CAPSTONE_PROPOSAL.md", "w") as f:
    f.write(md_content)

print(f"\n[+] Generated Document: 'CAPSTONE_PROPOSAL.md'")
print(f"[+] Project Title: {proposal_data['project_title']}")
print(f"[+] Total Integrated Engines: {len(proposal_data['technical_stack'])}")

print("\n[🚀 Capstone Spec Generator]: Proposal Document Live & Built!")
