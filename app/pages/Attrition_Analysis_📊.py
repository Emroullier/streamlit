import streamlit as st
<<<<<<< HEAD
import requests

markdown_1="""
=======
# import requests
# from PIL import Image
# import io

style_markdown = """
>>>>>>> f4972124331efa32a808abca08f35f20818eabec
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
    """


first_div_markdown="""
    <h3 class="section-header">Key Factors Affecting Attrition</h3>
    <div class="numbered-list">
    """

markdown_2="""
    </div>
    """
second_div_markdown="""
    <h4 class="section-header">Employee Profiling</h4>
    <div class="numbered-list">
        <ol>"""
image_1="""
            <li>Employee Retetion</li>
            <br>
        """
employee_rentention = "./app/images/employee_retention.png"

image_2="""
            <li>.</li>
            <br>
        """
image_3="""
            <li>.</li>
            <br>
        """
image_4="""
            <li>.</li>
            <br>
        """
image_5="""
            <li>.</li>
            <br>
        </ol>
    </div>
    """


<<<<<<< HEAD
st.markdown(markdown_1, unsafe_allow_html=True)

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

st.markdown(markdown_2, unsafe_allow_html=True)
=======
st.markdown(style_markdown, unsafe_allow_html=True)
st.markdown(first_div_markdown, unsafe_allow_html=True)
st.markdown(second_div_markdown, unsafe_allow_html=True)
st.markdown(image_1, unsafe_allow_html=True)
st.image(employee_rentention, caption="Employee Retention Graph")
st.markdown(image_2, unsafe_allow_html=True)
st.markdown(image_3, unsafe_allow_html=True)
st.markdown(image_4, unsafe_allow_html=True)
st.markdown(image_5, unsafe_allow_html=True)

# # Code for the request that doesn't require any input and returns an image
# st.markdown('<p class="header-text no-space">Execute to display the image</p>', unsafe_allow_html=True)


# # API endpoint for the image
# IMAGE_URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/plot_feature_importance"

# # Sending GET request to get the image
# response = requests.post(IMAGE_URL)

# if response.status_code == 200:
#     # Read the image from the response
#     image = Image.open(io.BytesIO(response.content))
#     st.image(image, caption="Generated Image")
# else:
#     st.write("Failed to retrieve the image")
#     st.write(f"Response status code: {response.status_code}")
>>>>>>> f4972124331efa32a808abca08f35f20818eabec
