import pandas as pd
import numpy as np

def generate_data(n=200):
    np.random.seed(42)

    dates = pd.date_range(start="2024-01-01", periods=n)

    categories = ["Food", "Travel", "Rent", "Shopping", "Entertainment"]
    payment_methods = ["Cash", "Card", "UPI"]

    data = {
        "Date": np.random.choice(dates, n),
        "Category": np.random.choice(categories, n),
        "Amount": np.random.randint(100, 5000, n),
        "Payment_Method": np.random.choice(payment_methods, n)
    }

    df = pd.DataFrame(data)
    return df