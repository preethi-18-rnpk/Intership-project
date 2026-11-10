 
import streamlit as st

st.set_page_config(
    page_title="Student Expense Tracker",
    page_icon="💰"
)

st.title("Student Expense Tracker")
st.write("Manage your daily expenses easily!")

# Store expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.subheader("Add New Expense")

expense_name = st.text_input("Expense Name")
amount = st.number_input(
    "Amount (₹)",
    min_value=0.0,
    step=10.0
)

if st.button("Add Expense"):
    if expense_name.strip() and amount > 0:
        st.session_state.expenses.append({
            "Name": expense_name,
            "Amount": amount
        })
        st.success("Expense added successfully!")
    else:
        st.warning("Enter a valid expense name and amount.")

st.divider()

st.subheader("Your Expenses")

if st.session_state.expenses:
    total = 0

    for i, expense in enumerate(st.session_state.expenses):
        st.write(
            f"{i + 1}. {expense['Name']} - ₹{expense['Amount']:.2f}"
        )
        total += expense["Amount"]

    st.metric("Total Expenses", f"₹{total:.2f}")

    if st.button("Clear All Expenses"):
        st.session_state.expenses = []
        st.rerun()
else:
    st.info("No expenses added yet.")
