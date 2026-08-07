import numpy as np
import pandas as pd

print("="*50)
print("  NomaanOS - Simplilearn GenAI & ML Lab Environment")
print("="*50)

# 1. NumPy Array Operations
data = np.array([10, 20, 30, 40, 50])
print(f"\n[+] NumPy Mean: {np.mean(data)}")
print(f"[+] NumPy Standard Deviation: {np.std(data):.2f}")

# 2. Pandas Dataframe Setup
df = pd.DataFrame({
    'Module': ['Python', 'Data Science', 'Machine Learning', 'GenAI'],
    'Status': ['Completed', 'In-Progress', 'Upcoming', 'Upcoming'],
    'Score': [95, 88, 0, 0]
})

print("\n[+] Course Progress Tracker:")
print(df)
print("\n-> Lab Setup Operational & Ready for Module 2!")
