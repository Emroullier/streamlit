import streamlit as st


t.write('# This is the homepage')

st.set_page_config(page_title="HR Data analytics")

st.markdown(
    """ # HR Data analytics
    ## Analysing HR data to predict and improve employee attrition rates.
    What is the probability that your current employee will leave the company, and what are the main factors due to influence this decision ?
    """

)

url = "https://netchex.com/wp-content/uploads/2022/12/HR-Analytics.png"
st.image(url)

homepage = st.Page("pages/homepage.py", title="Homepage")
EDA_page = st.Page("pages/EDA_page.py", title="EDA")
hiring_page = st.Page("pages/hiring_page.py", title="Hiring")
leaving_page = st.Page("pages/leaving_page.py", title="Leaving")

pg = st.navigation([homepage, EDA_page, hiring_page, leaving_page])
pg.run()
