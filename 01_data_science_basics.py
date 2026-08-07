import statistics

print("="*55)
print("  NomaanOS - Simplilearn GenAI & ML Lab (iSH Native)")
print("="*55)

# 1. Array Operations (Pure Python / Math Engine)
data = [10, 20, 30, 40, 50]
mean_val = statistics.mean(data)
std_dev = statistics.stdev(data)

print(f"\n[+] Array Data: {data}")
print(f"[+] Mean: {mean_val}")
print(f"[+] Standard Deviation: {std_dev:.2f}")

# 2. Course Progress Tracker Table
modules = [
    {"Module": "Python Refresher", "Status": "Completed", "Score": 95},
    {"Module": "Data Science Basics", "Status": "In-Progress", "Score": 88},
    {"Module": "Machine Learning", "Status": "Upcoming", "Score": 0},
    {"Module": "Generative AI & RAG", "Status": "Upcoming", "Score": 0}
]

print("\n[+] Course Progress Tracker:")
print(f"{'Module':<22} | {'Status':<12} | {'Score':<5}")
print("-" * 45)
for m in modules:
    print(f"{m['Module']:<22} | {m['Status']:<12} | {m['Score']:<5}")

print("\n-> Lab Setup Operational & Fully Compatible with iSH!")
