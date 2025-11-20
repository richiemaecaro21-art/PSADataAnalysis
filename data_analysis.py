import matplotlib.pyplot as plt
import pandas as pd

# Read your cleaned CSV
data = pd.read_csv("cleaned_unemployment_underemployment_2025.csv")

# Manually add the month names (adjust if you have fewer/more)
months = [
    "Sep 2024", "Jan 2025", "Feb 2025", "Mar 2025",
    "Apr 2025", "May 2025", "Jun 2025", "Jul 2025",
    "Aug 2025", "Sep 2025"
]

# Example: use your extracted data for underemployment/unemployment
under_values = [5944, 6469, 4959, 6438, 7091, 6603, 5763, 6803, 5381, 5523]
unemp_values  = [328, 212, 385, 525, 248, 483, 362, 107, 342, 355]

# Plot
plt.figure(figsize=(8, 5), dpi=120)
plt.plot(months, under_values, marker='o', color='steelblue', label='Underemployed')
plt.plot(months, unemp_values, marker='o', color='orange', label='Unemployed')

plt.title("Underemployment vs Unemployment Trends (2024–2025)", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Number of Persons (in Thousands)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig("underemployment_vs_unemployment_2025_fixed.png")
plt.show()

import numpy as np

#“Which months in 2025 had the highest and lowest unemployment and underemployment in the Philippines?”
# Underemployment
max_under_idx = np.argmax(under_values)
min_under_idx = np.argmin(under_values)
print(f" Underemployment peaked in {months[max_under_idx]} with {under_values[max_under_idx]} thousand persons.")
print(f" Underemployment was lowest in {months[min_under_idx]} with {under_values[min_under_idx]} thousand persons.")

# Unemployment
max_unemp_idx = np.argmax(unemp_values)
min_unemp_idx = np.argmin(unemp_values)
print(f" Unemployment peaked in {months[max_unemp_idx]} with {unemp_values[max_unemp_idx]} thousand persons.")
print(f"Unemployment was lowest in {months[min_unemp_idx]} with {unemp_values[min_unemp_idx]} thousand persons.")

print("\nControversial Question Answer:") 

