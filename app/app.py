import streamlit as st
from pages import homepage, EDA_page, hiring_page, leaving_page

st.set_page_config(page_title="HR Data Analytics", page_icon=":bar_chart:", layout="wide")

st.markdown(
    """
    # HR Data Analytics
    ## Analyzing HR data to predict and improve employee attrition rates.
    What is the probability that your current employee will leave the company, and what are the main factors that influence this decision?
    """
)

url = "https://netchex.com/wp-content/uploads/2022/12/HR-Analytics.png"
st.image(url)

PAGES = {
    "Home": homepage,
    "EDA": EDA_page,
    "Hiring": hiring_page,
    "Leaving": leaving_page
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()
