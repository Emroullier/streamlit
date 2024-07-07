import streamlit as st
import requests

markdown_2="""
    <h4 class="section-header">Employee Profiling</h4>
    """

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

# ************************** Connection to API *****************************
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
