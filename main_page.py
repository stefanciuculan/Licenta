import streamlit as st
from streamlit_option_menu import option_menu

this = option_menu(
    menu_title = None,
    options=["Home", "Library", "My Loans"],
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                #"icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#711A1A"},
            }
)

if this == "Home":
    st.title(f"You have selected {this}")
if this == "Library":
    st.title(f"You have selected {this}")
if this == "My Loans":
    st.title(f"You have selected {this}")