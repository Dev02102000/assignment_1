import streamlit as st
from page.introduction import introduction_page
from page.view_tables import view_tables_page
from page.filter_data import filter_data_page
from page.crud_operations import crud_page
from page.simulation import simulation_page
from page.insights import insights_page
from page.about import about_page




st.set_page_config(layout="wide", page_title="BankSight Dashboard")

st.sidebar.title("📊 BankSight Navigation")
option = st.sidebar.radio(
    "Go to:",
    (
        "Introduction",
        "View Tables",
        "Filter Data",
        "CRUD Operations",
        "Credit / Debit Simulation",
        "Analytical Insights",
        "About Creator"
    )
)

if option == "Introduction":
    introduction_page()

elif option == "View Tables":
    view_tables_page()

elif option == "Filter Data":
    filter_data_page()

elif option == "CRUD Operations":
    crud_page()

elif option == "Credit / Debit Simulation":
    simulation_page()

elif option == "Analytical Insights":
    insights_page()

elif option == "About Creator":
    about_page()