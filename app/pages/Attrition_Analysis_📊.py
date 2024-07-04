import streamlit as st
import requests

st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: gray;
        font-size: 1.5em;
    }
    .section-header {
        text-align: left;
        margin-top: 20px;
        font-size: 1.3em;
        font-weight: bold;
    }
    .numbered-list {
        text-align: left;
        margin-top: 10px;
        font-size: 1.2em;
    }
    .numbered-list ol {
        list-style-position: inside;
        padding-left: 0;
    }
    .numbered-list li {
        margin-bottom: 5px;
    }
    </style>
    <h1 class="title">Attrition Rate Analysis</h1>
    <h2 class="subtitle">Why are your employees leaving your company?</h2>
    <h3 class="section-header">Key Factors Affecting Attrition</h3>
    <div class="numbered-list">
        <ol>
            <li>Top 5 most important according to model</li>
            <li>.</li>
            <li>.</li>
            <li>.</li>
            <li>.</li>
        </ol>
    </div>
    <h4 class="section-header">Employee Profiling</h4>
    <div class="numbered-list">
        <ol>
            <li>I assume graphs</li>
            <li>.</li>
            <li>.</li>
            <li>.</li>
            <li>.</li>
        </ol>
    </div>
    """,
    unsafe_allow_html=True
)

plot = st.radio(
    "Choose your graph",
    ["Feature importance", "Time spent in the company",
     "Salary", "Number of projects", "Step counts"],
    captions = ["Short explanation", "Short explanation",
                "Short explanation", "Short explanation",
                "Short explanation"])

if plot == "Feature importance":
    # ************************** Connection to API : Feature importance ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_feature_importance"

    # sending get request and saving the response as response object
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************

if plot == "Time spent in the company":
        # ************************** Connection to API : Time spent in the company ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_time_spend_company"

    # sending get request and saving the response as response object
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************

if plot == "Salary":
    # ************************** Connection to API  : Salary ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_salary"

    # sending get request and saving the response as response object
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************


if plot == "Number of projects":
    # ************************** Connection to API :  Number of projects ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_number_projects"

    # sending get request and saving the response as response object
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************


if plot == "Step counts":
    # ************************** Connection to API ***************************************
    # api-endpoint
    URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_step_count"

    # sending get request and saving the response as response object
    # r = requests.post(url = URL, params = {'feature' : col})
    r = requests.post(url = URL)

    st.image(r.content,
                caption=None,
                width=None,
                use_column_width=None,
                clamp=False,
                channels="RGB",
                output_format="PNG")
    # **************************************************************************************
