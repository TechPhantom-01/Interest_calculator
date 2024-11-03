import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.title("Interest Amount Calculator")

# User inputs
start_date = st.date_input("Select Start Date")
end_date = st.date_input("Select End Date")
principal = st.number_input("Enter Principal Amount", min_value=0.0, step=0.01)
interest_rate = st.number_input("Enter Annual Interest Rate (%)", min_value=0.0, step=0.01)

# Validate dates
if end_date <= start_date:
    st.error("End date should be after the start date.")
else:
    if st.button('Calculate'):
    # Calculate time difference in months and days
        delta = relativedelta(end_date, start_date)
        months = delta.months + delta.years * 12
        days = delta.days

    # Calculate the total interest
        month_interest = principal * (interest_rate / 100)
        daily_interest = month_interest / 30
        interest_amount = (month_interest) * months + daily_interest * days
        total_amount = principal + interest_amount

    # Display results
        st.write(f"Total Duration: {months} months and {days} days")
        st.write(f"Interest Amount: ${interest_amount:.2f}")
        st.write(f"Total Amount (Principal + Interest): ${total_amount:.2f}")
