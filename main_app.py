import streamlit as st
from streamlit_option_menu import option_menu

from main_page import main_page
from school_of_computing import school_of_computing
from school_of_engineering import school_of_engineering
from school_of_humanities_natural_and_sicial_sciences import school_of_humanities_natural_and_social_sciences
from school_of_management import school_of_management
from summary import summary

st.set_page_config(
    page_title="New Uzbekistan University Resit Exam",
    layout="wide",
    page_icon='logo.png',
)

with st.sidebar:
    options = option_menu(
        menu_title="NewUU Departments",
        options=[
            "Main Page",
            "School Of Computing",
            "School of Engineering",
            "School of Humanities, Natural & Social Sciences",
            "School of Management",
            "Summary",
        ],
        icons=[
            "house",
            "cpu",
            "gear",
            "globe",
            "briefcase",
            "bar-chart-line",
        ],
        menu_icon="cast",
        default_index=0,
    )

if options == "Main Page":
    main_page()

if options == "School Of Computing":
    school_of_computing()

if options == "School of Engineering":
    school_of_engineering()

if options == "School of Humanities, Natural & Social Sciences":
    school_of_humanities_natural_and_social_sciences()

if options == "School of Management":
    school_of_management()

if options == "Summary":
    summary()