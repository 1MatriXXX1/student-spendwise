# app.py
import streamlit as st
import pandas as pd
import logic  

st.title("Student SpendWise")


if 'expenses' not in st.session_state:
    st.session_state.expenses = {"Food": {}, "Fun": {}, "Bills": {}, "Other": {}}
if 'budget' not in st.session_state:
    st.session_state.budget = 0.0


st.sidebar.header("Budget Settings")
st.session_state.budget = st.sidebar.number_input("Monthly Budget:", value=st.session_state.budget)


st.subheader("Add New Expense")
category = st.selectbox("Category", list(st.session_state.expenses.keys()))
item = st.text_input("Item Name")
price = st.number_input("Price", min_value=0.0)

if st.button("Add"):
    if logic.add_expense(st.session_state.expenses, category, item, price):
        st.success("Expense added!")


total = logic.calculate_total_spent(st.session_state.expenses)
status, diff = logic.check_budget_status(total, st.session_state.budget)

st.metric("Total Spent", f"${total:.2f}")

if status == "Safe":
    st.success(f"Safe! You have ${diff:.2f} left.")
elif status == "Warning":
    st.warning(f"Exceeded budget by ${diff:.2f}!")

st.dataframe(pd.DataFrame(st.session_state.expenses))