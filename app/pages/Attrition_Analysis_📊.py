import streamlit as st
import requests

markdown_1="""
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
    """

markdown_2="""
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
    """

st.markdown(markdown_2, unsafe_allow_html=True)

st.write("----------------------------")

#Choose the kind of plot
option_plot = st.selectbox(
    "**What type of plot ?**",
    ('violin', 'crosstab', 'hist'),
    key = 'option_plot'
    )

if option_plot == 'violin':
    endpoint = 'plot_violin'
    selection = ('average_montly_hours',
                'LinkedIn_Hits',
                'Sensor_StepCount',
                'Sensor_Heartbeat(Average/Min)',
                'Sensor_Proximity(1-highest/10-lowest)',
                'last_evaluation')

if option_plot == 'crosstab':
    endpoint = 'plot_crosstab'
    selection = ('Gender',
                'promotion_last_5years',
                'Work_accident',
                'Rising_Star',
                'Percent_Remote',
                'number_project',
                'salary')

if option_plot == 'hist':
    endpoint = 'plot_freq'
    selection = ('time_spend_company', 'Rising_Star')

option_final = st.selectbox(
    "**Which feature do you want to plot ?**",
    selection,
    key='option_final'
    )

# ************************** Connection to API : Violin plots ***************
# api-endpoint
URL = f"https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/{endpoint}"
params = {'input' : option_final}
# sending get request and saving the response as response object
r = requests.post(url = URL, params = params)

st.image(r.content,
            caption=None,
            width=None,
            use_column_width=None,
            clamp=False,
            channels="RGB",
            output_format="PNG")
# ***************************************************************************
