import streamlit as st

st.set_page_config(page_title="HR Data Analytics", page_icon=":bar_chart:")

st.markdown(
    """
    # HR Data Analytics
    ## Analyzing HR data to predict and improve employee attrition rates.
    What is the probability that your current employee will leave the company, and what are the main factors that influence this decision?
    """
)

url = "https://netchex.com/wp-content/uploads/2022/12/HR-Analytics.png"
st.image(url)
