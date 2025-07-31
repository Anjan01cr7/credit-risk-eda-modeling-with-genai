import matplotlib.pyplot as plt

# Data
methods = ['Traditional Collections', 'AI-Powered Collections']
delinquency_rates = [100, 65]

# Plot
plt.figure(figsize=(6, 4))
bars = plt.bar(methods, delinquency_rates, color=['#FF6666', '#66B3FF'])
plt.title('Projected Delinquency Reduction')
plt.ylabel('Delinquency Rate (%)')
plt.ylim(0, 120)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add labels
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
             f'{bar.get_height()}%', ha='center')

# Save
plt.tight_layout()
plt.savefig("Projected_Delinquency_Reduction.png")
plt.show()
