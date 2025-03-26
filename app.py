import streamlit as st
import joblib
st.title('Loan Approval process Automation')
model=joblib.load('loan_data.joblib')
gender=st.number_input("Enter gender male:0 female:1")
married= st.number_input("enter marital status married:1 unmarried:0")
income=st.number_input("enter applicant income in thousands")
la=st.number_input("enter loan amount in thousands")
if st.button("predict Approval"):
    prediction=model.predict([[gender,married,income,la]])
    if prediction=='Y':
        st.text("loan Approved")
    else:
        st.text("loan Rejected")
