import streamlit as st
import requests

markdown_1="""
    <style>
    .title {
        text-align: center;
    }
    .subtitle {
        text-align: center;
        color: #c9c9c9;
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
    <div class="numbered-list">
    """

markdown_2="""
    </div>
    <p>
    This section allows you to explore different data visualization graphs.
    We wanted to provide, through 3 type of plots, a clear way to understand which data impact the employees retention and how.
    <br>
    Although there are a lot of graphs we decided to make a selection to present you what we need to retain from our analysis.
    <br>
    Feel free to explore our selection of violin, barplots and histograms graphs.
    </p>
    <h4 class="section-header">Visualization plots analysis</h4>
    <div class="numbered-list">
        <ol>
            <li>Average monthly hours in violin shape</li>
            <li>Number of project distribution</li>
            <li>Histogram of the time spent in the company</li>
            <li>.</li>
            <li>.</li>
        </ol>
    </div>
    """

st.markdown(markdown_1, unsafe_allow_html=True)
st.markdown(markdown_2, unsafe_allow_html=True)

st.write("Most important features determining employee status")

# Display static image of top important features from Random Forest
image_feature_imp = "app/images/feature_importance.png"
st.image(image_feature_imp)

st.write("----------------------------")

st.write("Plots with features influencing employee status in company")

# Choose the kind of plot
option_plot = st.selectbox(
    "**What type of plot ?**",
    ('Violin', 'Crosstab', 'Hist'),
    key = 'option_plot'
    )

if option_plot == 'Violin':
    endpoint = 'plot_violin'
    selection = ('average_montly_hours',
                'LinkedIn_Hits',
                'Sensor_StepCount',
                'Sensor_Heartbeat(Average/Min)',
                'Sensor_Proximity(1-highest/10-lowest)',
                'last_evaluation')

if option_plot == 'Crosstab':
    endpoint = 'plot_crosstab'
    selection = ('Gender',
                'promotion_last_5years',
                'Percent_Remote',
                'number_project',
                'salary')

if option_plot == 'Hist':
    endpoint = 'plot_freq'
    selection = ('time_spend_company', 'Rising_Star')

option_final = st.selectbox(
    "**Which feature do you want to plot ?**",
    selection,
    key='option_final'
    )

# ************************** Connection to API : Visualization plots ***************
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

# Display of Kmeans picture
st.write("Employee profiles")
image_feature_imp = "app/images/Employee_groups.png"
st.image(image_feature_imp)
st.write("0. Employees with an average mean score in the top 5 important features who are still in company.")
st.write("1. Employees with an high mean score in the top 5 important features who left in company.")
st.write("2. Employees with a low mean score in the top 5 important features who left in company.")
