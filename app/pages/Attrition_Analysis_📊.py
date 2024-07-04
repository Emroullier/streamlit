import streamlit as st
# import requests
# from PIL import Image
# import io

style_markdown = """
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
        <ol>
            <li>Top 5 most important according to model</li>
            <li>.</li>
            <li>.</li>
            <li>.</li>
            <li>.</li>
        </ol>
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
