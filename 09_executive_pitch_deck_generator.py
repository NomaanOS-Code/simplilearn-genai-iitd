import json

print("="*65)
print("  NomaanOS - IHFC IIT Delhi Executive Pitch Deck Generator")
print("="*65)

title = "NomaanOS Shield"
subtitle = "Autonomous Edge Security & Threat Triaging via Local GenAI Agents"
scholar = "Nomaan Khan"
program = "Professional Certificate Program in GenAI & ML"
institution = "IHFC - Technology Innovation Hub of IIT Delhi x Simplilearn x Microsoft"

slides = [
    ("Slide 1: Executive Title & Credentials", "**Project:** NomaanOS Shield\n**Target:** Autonomous Threat Triaging on Constrained Edge Nodes\n**Scholar:** Nomaan Khan\n**Hub:** IHFC (IIT Delhi Technology Innovation Hub)"),
    ("Slide 2: The Core Problem", "1. **High Cloud Latency:** Traditional SOCs take minutes to process zero-day attack vectors.\n2. **Data Leakage Risks:** Cloud-based GenAI APIs expose sensitive telemetry logs during inspection.\n3. **Hardware Constraints:** Existing LLMs cannot run on resource-constrained edge gateways."),
    ("Slide 3: The Innovation (NomaanOS Shield)", "- **100% Data Sovereignty:** Zero cloud API dependencies; all processing happens locally.\n- **Hybrid Math & Neural Engine:** Lightweight ML models handle filtering, while ReAct GenAI Agents handle complex triaging.\n- **Sub-Second Containment:** Threat classification & RAG context injection under <100ms."),
    ("Slide 4: Integrated Laboratory Suite", "| Module | Engine File | Function |\n| :--- | :--- | :--- |\n| **Data Analysis** | `01_data_science_basics.py` | Telemetry Parsing |\n| **Regression** | `02_linear_regression_engine.py` | Load Forecasting |\n| **Classification** | `03_knn_classification_engine.py` | Threat Categorization |\n| **Clustering** | `04_kmeans_clustering_engine.py` | Anomaly Isolation |\n| **Neural Net** | `05_perceptron_neural_network.py` | Decision-Gate Scoring |\n| **RAG Vector** | `06_vector_similarity_rag_engine.py` | Context Retrieval |\n| **Agentic Loop** | `07_agentic_ai_orchestrator.py` | ReAct Autonomous Tool Execution |"),
    ("Slide 5: End-to-End System Architecture Flow", "```\n[Network Traffic Telemetry]\n       |\n       v\n[K-Means Anomaly Filter] --(Unsupervised)--> [Isolate Suspicious Cluster]\n       |\n       v\n[KNN & Perceptron Engine] --(Scoring)-----> [Calculate Threat Probability]\n       |\n       v\n[ReAct Agentic Loop] -----(Reasoning)----> [Tool Action: Invoke Local RAG Context]\n       |\n       v\n[Automated Edge Mitigation & Local Threat Containment (<100ms)]\n```"),
    ("Slide 6: Market & Defense Use Cases", "- **Enterprise SOC Automation:** Automated Tier-1 alert triaging without log leakage.\n- **Industrial IoT & Smart Grids:** Edge security for cyber-physical systems.\n- **Defense & Tactical Communications:** Air-gapped network intrusion protection."),
    ("Slide 7: Incubation Ask & Next Milestones", "- **Incubation Support:** IHFC IIT Delhi Incubation Track Alignment.\n- **Hardware Access:** Prototyping on NVIDIA Jetson / Edge AI Accelerators.\n- **Target Seed Ask:** Pre-seed incubation grant for Pilot Deployment.")
]

deck_md = f"# Executive Pitch Deck: {title}\n### *{subtitle}*\n\n**Presenter:** {scholar}  \n**Program:** {program}  \n**Institution:** {institution}  \n\n---\n\n"

for head, body in slides:
    deck_md += f"## {head}\n\n{body}\n\n---\n\n"

deck_md += "*Generated & Presented via NomaanOS Engine (`09_executive_pitch_deck_generator.py`)*\n"

with open("EXECUTIVE_PITCH_DECK.md", "w") as f:
    f.write(deck_md)

print("\n[+] Generated Deck: 'EXECUTIVE_PITCH_DECK.md'")
print(f"[+] Total Presentation Slides: {len(slides)}")
print("\n[🚀 Pitch Deck Generator]: Executive Slide Presentation Successfully Live!")
