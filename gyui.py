import streamlit as st
from MemberView import GymMemberManager

member_instance = GymMemberManager()

tab1, tab2 = st.tabs(["Add Member", "View Members"])

with tab1:
    st.title("Add new members..!")
    name = st.text_input("Enter member name")
    place = st.text_input("Enter place")
    plan = st.selectbox("select plan", ["1 month", "2 months", "3 months", "6 months", "1 year"])
    mobile = st.text_input("Enter mobile number")
    fees = st.text_input("Enter fees")
    joining_date = st.date_input("Enter date")
    if st.button("Submit"):
        member_instance.post(name = name, place= place, plan = plan, mobile = mobile, fee = fees, joining_date = joining_date)
        st.success("Member added successfully..!")

with tab2:
    st.title("View member details...!")
    members = member_instance.get()
    if members:
        st.dataframe(members)
    else:
        st.warning("No member details..!")