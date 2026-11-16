
import streamlit as st
import csv
import io

st.set_page_config(
    page_title="Student Expense Tracker",
    page_icon="💰"
)

st.title("Student Expense Tracker")
st.write("Manage your daily expenses easily!")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.subheader("Add New Expense")

name = st.text_input("Expense Name")

category = st.selectbox(
    "Category",
    ["Food", "Travel", "Education", "Shopping", "Other"]
)

amount = st.number_input(
    "Amount (₹)", min_value=0.0, step=10.0
)

expense_date = st.date_input("Expense Date")

if st.button("Add Expense"):
    if name.strip() and amount > 0:
        st.session_state.expenses.append({
            "Name": name,
            "Category": category,
            "Amount": amount,
            "Date": str(expense_date)
        })
        st.success("Expense added successfully!")
    else:
        st.warning("Enter a valid name and amount.")

st.divider()
st.subheader("Your Expenses")

if st.session_state.expenses:
    total = sum(
        item["Amount"] for item in st.session_state.expenses
    )

    st.metric("Total Expenses", f"₹{total:.2f}")

    for item in st.session_state.expenses:
        st.write(
            f'{item["Date"]} | {item["Name"]} | '
            f'{item["Category"]} | ₹{item["Amount"]:.2f}'
        )

    st.subheader("Category-wise Summary")

    category_totals = {}

    for item in st.session_state.expenses:
        cat = item["Category"]
        category_totals[cat] = (
            category_totals.get(cat, 0) + item["Amount"]
        )

    st.bar_chart(category_totals)

    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=["Name", "Category", "Amount", "Date"]
    )
    writer.writeheader()
    writer.writerows(st.session_state.expenses)

    st.download_button(
        "Download Expenses as CSV",
        output.getvalue(),
        "expenses.csv",
        "text/csv"
    )

    if st.button("Clear All Expenses"):
        st.session_state.expenses = []
        st.rerun()

else:
    st.info("No expenses added yet.")
