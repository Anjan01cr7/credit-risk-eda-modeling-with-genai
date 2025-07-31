import matplotlib.pyplot as plt

# Data
labels = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied']
sizes = [40, 35, 15, 10]
colors = ['#66B3FF', '#99FF99', '#FFCC99', '#FF6666']

# Plot
plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors,
        startangle=140, wedgeprops={'edgecolor': 'black'})
plt.title('Customer Feedback on AI-Driven Outreach')
plt.tight_layout()

# Save
plt.savefig("Customer_Feedback_Pie_Chart.png")
plt.show()
