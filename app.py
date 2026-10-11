import csv
from pathlib import Path

import streamlit as st


PAYMENTS_FILE = Path(__file__).with_name("payments.csv")
COLUMNS = ["Tenant Name", "Monthly Rent", "Amount Paid", "Remaining Balance", "Payment Status"]


def save_payment(payment):
    file_has_data = PAYMENTS_FILE.exists() and PAYMENTS_FILE.stat().st_size > 0
    with PAYMENTS_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        if not file_has_data:
            writer.writeheader()
        writer.writerow(payment)


def load_payments():
    if not PAYMENTS_FILE.exists():
        return []
    with PAYMENTS_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


st.title("Rent Payment Tracker")
st.write("A simple Python project for a property management capstone milestone.")

with st.form("rent_calculator"):
    tenant_name = st.text_input("Tenant name")
    monthly_rent = st.number_input("Monthly rent ($)", value=0.0, step=0.01, format="%.2f")
    amount_paid = st.number_input("Amount paid ($)", value=0.0, step=0.01, format="%.2f")
    calculate = st.form_submit_button("Calculate")

if calculate:
    st.session_state["payment_to_save"] = None
    # Check the inputs before calculating a balance.
    if not tenant_name.strip():
        st.error("Please enter a tenant name.")
    elif monthly_rent <= 0:
        st.error("Monthly rent must be greater than zero.")
    elif amount_paid < 0:
        st.error("Amount paid cannot be negative.")
    elif amount_paid > monthly_rent:
        st.error("Amount paid cannot exceed monthly rent.")
    else:
        # Round to cents so the displayed balance matches dollar amounts.
        balance = round(monthly_rent - amount_paid, 2)

        if balance == 0:
            status = "Paid"
        elif amount_paid == 0:
            status = "Unpaid"
        else:
            status = "Partial"

        st.session_state["payment_to_save"] = {
            "Tenant Name": tenant_name.strip(),
            "Monthly Rent": f"{monthly_rent:.2f}",
            "Amount Paid": f"{amount_paid:.2f}",
            "Remaining Balance": f"{balance:.2f}",
            "Payment Status": status,
        }

payment = st.session_state.get("payment_to_save")
if payment:
    # Changing an input requires a new calculation before saving.
    if (tenant_name.strip() != payment["Tenant Name"]
            or f"{monthly_rent:.2f}" != payment["Monthly Rent"]
            or f"{amount_paid:.2f}" != payment["Amount Paid"]):
        st.session_state["payment_to_save"] = None
        payment = None

if payment:
    st.subheader("Calculation result")
    st.write(f"Tenant: {payment['Tenant Name']}")
    st.metric("Remaining balance", f"${float(payment['Remaining Balance']):,.2f}")
    st.write(f"Payment status: **{payment['Payment Status']}**")

    if st.button("Save Payment"):
        save_payment(payment)
        st.session_state["payment_to_save"] = None
        st.success("Payment saved.")

st.subheader("Payment history")
saved_payments = load_payments()
if saved_payments:
    st.table(saved_payments)
else:
    st.info("No payments saved yet.")
