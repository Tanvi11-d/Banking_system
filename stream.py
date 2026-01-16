from main import *
import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8002"

st.title("Bank Account Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Account",
        "View All Accounts",
        "View Account",
        "Update Account",
        "Delete Account",
        "Deposit",
        "Withdraw",
        "Transaction History",
        "All Transactions",
    ],
)

#  CREATE ACCOUNT 
if menu == "Create Account":
    st.header("Create New Account")

    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=1)
    city = st.text_input("City")
    balance = st.number_input("Initial Balance", min_value=0.0)

    if st.button("Create Account"):
        payload = {
            "name": name,
            "email": email,
            "age": age,
            "city": city,
            "balance": balance,
        }
        res = requests.post(f"{BASE_URL}/account/", json=payload)

        if res.status_code == 201:
            st.success("Account created successfully")
            st.json(res.json())
        else:
            st.error(res.text)

# VIEW ALL ACCOUNTS 
elif menu == "View All Accounts":
    st.header("All Accounts")

    res = requests.get(f"{BASE_URL}/account/")
    if res.status_code == 200:
        st.table(res.json())
    else:
        st.error(res.text)

# VIEW SINGLE ACCOUNT 
elif menu == "View Account":
    st.header("View Account")

    acc_id = st.number_input("Account ID", min_value=1)

    if st.button("Fetch Account"):
        res = requests.get(f"{BASE_URL}/account/{acc_id}")
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error(res.text)

#  UPDATE ACCOUNT 
elif menu == "Update Account":
    st.header("Update Account")

    acc_id = st.number_input("Account ID", min_value=1)
    name = st.text_input("New Name")
    email = st.text_input("New Email")
    age = st.number_input("New Age", min_value=1)
    city = st.text_input("New City")

    if st.button("Update"):
        payload = {
            "name": name,
            "email": email,
            "age": age,
            "city": city,
        }
        res = requests.put(f"{BASE_URL}/account/{acc_id}", json=payload)

        if res.status_code == 200:
            st.success("Account updated")
            st.json(res.json())
        else:
            st.error(res.text)

#DELETE ACCOUNT 
elif menu == "Delete Account":
    st.header("Delete Account")

    acc_id = st.number_input("Account ID", min_value=1)

    if st.button("Delete"):
        res = requests.delete(f"{BASE_URL}/account/{acc_id}")
        if res.status_code == 200:
            st.success("Account deleted")
            st.json(res.json())
        else:
            st.error(res.text)

# DEPOSIT 
elif menu == "Deposit":
    st.header("Deposit Money")

    acc_id = st.number_input("Account ID", min_value=1)
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Deposit"):
        payload = {"amount": amount}
        res = requests.post(f"{BASE_URL}/account/deposit/{acc_id}", json=payload)

        if res.status_code == 201:
            st.success("Deposit successful")
            st.json(res.json())
        else:
            st.error(res.text)

#  WITHDRAW 
elif menu == "Withdraw":
    st.header("Withdraw Money")

    acc_id = st.number_input("Account ID", min_value=1)
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Withdraw"):
        payload = {"amount": amount}
        res = requests.post(f"{BASE_URL}/account/withdraw/{acc_id}", json=payload)

        if res.status_code == 201:
            st.success("Withdraw successful")
            st.json(res.json())
        else:
            st.error(res.text)

#  TRANSACTION HISTORY 
elif menu == "Transaction History":
    st.header("Transaction History")

    acc_id = st.number_input("Account ID", min_value=1)

    if st.button("Get History"):
        res = requests.get(f"{BASE_URL}/account/history/{acc_id}")
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error(res.text)

#  ALL TRANSACTIONS 
elif menu == "All Transactions":
    st.header("All Transactions")

    res = requests.get(f"{BASE_URL}/account/history_all/")
    if res.status_code == 200:
        st.table(res.json())
    else:
        st.error(res.text)
