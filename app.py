import streamlit as st


st.title("Rent Payment Tracker")
st.write("A simple Python project for a property management capstone milestone.")

with st.form("rent_calculator"):
    tenant_name = st.text_input("Tenant name")
    monthly_rent = st.number_input("Monthly rent ($)", value=0.0, step=0.01, format="%.2f")
    amount_paid = st.number_input("Amount paid ($)", value=0.0, step=0.01, format="%.2f")
    calculate = st.form_submit_button("Calculate")

if calculate:
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

        st.subheader("Calculation result")
        st.write(f"Tenant: {tenant_name.strip()}")
        st.metric("Remaining balance", f"${balance:,.2f}")
        st.write(f"Payment status: **{status}**")
