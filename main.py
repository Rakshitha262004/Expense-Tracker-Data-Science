import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Generate Synthetic Data
# -------------------------------

np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=200)

categories = ["Food", "Travel", "Rent", "Shopping", "Entertainment"]
payment_methods = ["Cash", "Card", "UPI"]

data = {
    "Date": np.random.choice(dates, 200),
    "Category": np.random.choice(categories, 200),
    "Amount": np.random.randint(100, 5000, 200),
    "Payment_Method": np.random.choice(payment_methods, 200)
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("data/expenses.csv", index=False)

# -------------------------------
# 2. Data Cleaning
# -------------------------------

df.dropna(inplace=True)
df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------
# 3. Feature Engineering
# -------------------------------

df["Month"] = df["Date"].dt.month

# -------------------------------
# 4. Analysis
# -------------------------------

category_spending = df.groupby("Category")["Amount"].sum()
monthly_spending = df.groupby("Month")["Amount"].sum()

print("\nCategory-wise Spending:\n", category_spending)
print("\nMonthly Spending:\n", monthly_spending)

# -------------------------------
# 5. Visualization
# -------------------------------

plt.figure()
category_spending.plot(kind='bar')
plt.title("Category-wise Spending")
plt.savefig("outputs/category_spending.png")
plt.close()

plt.figure()
monthly_spending.plot(kind='line')
plt.title("Monthly Spending Trend")
plt.savefig("outputs/monthly_trend.png")
plt.close()

# Pie chart
plt.figure()
category_spending.plot(kind='pie', autopct='%1.1f%%')
plt.title("Spending Distribution")
plt.savefig("outputs/pie_chart.png")
plt.close()

# -------------------------------
# 6. Insights
# -------------------------------

highest_category = category_spending.idxmax()
print(f"\nHighest spending category: {highest_category}")

if category_spending.max() > 20000:
    print("⚠️ Overspending detected!")