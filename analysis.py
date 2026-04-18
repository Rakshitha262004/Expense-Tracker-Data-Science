def category_spending(df):
    return df.groupby("Category")["Amount"].sum()

def monthly_spending(df):
    return df.groupby("Month")["Amount"].sum()

def highest_spending_category(category_data):
    return category_data.idxmax(), category_data.max()