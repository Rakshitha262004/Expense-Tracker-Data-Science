import streamlit as st
import pandas as pd

from src.data_generator import generate_data
from src.preprocessing import clean_data, add_features
from src.analysis import category_spending, monthly_spending, highest_spending_category
from src.visualization import plot_category, plot_monthly, plot_pie

st.set_page_config(page_title="Expense Tracker", layout="wide")

st.title("💰 Expense Tracker Dashboard")

# Sidebar
st.sidebar.header("Options")
data_option = st.sidebar.radio("Data Source", ["Generate Data", "Upload CSV"])

# Load data
if data_option == "Generate Data":
    df = generate_data()
else:
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.warning("Upload a file")
        st.stop()

# Preprocessing
df = clean_data(df)
df = add_features(df)

# Show data
st.subheader("📊 Data Preview")
st.dataframe(df.head())

# Filters
category_filter = st.sidebar.multiselect(
    "Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

df = df[df["Category"].isin(category_filter)]

# Analysis
cat_data = category_spending(df)
month_data = monthly_spending(df)

# Charts
col1, col2 = st.columns(2)

with col1:
    st.pyplot(plot_category(cat_data))

with col2:
    st.pyplot(plot_monthly(month_data))

st.pyplot(plot_pie(cat_data))

# Insights
st.subheader("🧠 Insights")
cat, amt = highest_spending_category(cat_data)

st.write(f"Highest Spending Category: **{cat}**")
st.write(f"Amount: ₹{amt}")

if amt > 20000:
    st.warning("Overspending detected!")