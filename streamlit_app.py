import streamlit as st
from datetime import datetime, timedelta

st.title("Interest Calculator")

amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")
start_date = st.date_input("Select the start date:", datetime.today())
end_date = st.date_input("Select the end date:", datetime.today())
interest_rate = st.number_input("Enter the monthly interest rate (in %):", min_value=0.0, format="%.2f")

if st.button("Calculate"):
    # Calculate the total number of days
    delta = end_date - start_date
    total_days = delta.days

    # Calculate full months
    full_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    # Adjust full months if the end day is less than the start day
    if end_date.day < start_date.day:
        full_months -= 1

    # If full months is less than 0, it means the dates are less than a month apart
    if full_months < 0:
        full_months = 0

    # Calculate the end of the last full month
    last_full_month_end = (start_date.replace(day=1) + timedelta(days=(full_months + 1) * 30)).replace(day=1) - timedelta(days=1)

    # Calculate remaining days after the last full month
    remaining_days = (end_date - last_full_month_end).days

    # Adjust remaining days if full months are zero
    if full_months == 0:
        remaining_days = total_days

    # Total days calculated from full months and remaining days
    calculated_total_days = (full_months * 30) + remaining_days

    # Calculate interest
    total_amount = amount * (1 + (interest_rate / 100) * full_months)

    # If there are remaining days, calculate daily interest
    if remaining_days > 0 and interest_rate > 0:
        daily_interest_rate = (interest_rate / 100) / 30  # Assuming 30 days in a month
        total_amount += amount * daily_interest_rate * remaining_days

    # Display results
    st.write(f"Total days between the two dates: {total_days} days")
    st.write(f"Number of full months: {full_months} months")
    st.write(f"Remaining days after full months: {remaining_days} days")
    st.write(f"Total days calculated from full months and remaining days: {calculated_total_days} days")
    st.write(f"Total amount after applying interest: ${total_amount:.2f}")

    # Check if calculated total days matches the total days
    if calculated_total_days == total_days:
        st.write("The calculated total days match the total days between the two dates.")
    else:
        st.write("The calculated total days do NOT match the total days between the two dates.")
