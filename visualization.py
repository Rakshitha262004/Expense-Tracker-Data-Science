import matplotlib.pyplot as plt

def plot_category(category_data):
    fig, ax = plt.subplots()
    category_data.plot(kind='bar', ax=ax)
    ax.set_title("Category-wise Spending")
    return fig

def plot_monthly(monthly_data):
    fig, ax = plt.subplots()
    monthly_data.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Monthly Spending Trend")
    return fig

def plot_pie(category_data):
    fig, ax = plt.subplots(figsize=(4,4))
    category_data.plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_title("Spending Distribution")
    return fig