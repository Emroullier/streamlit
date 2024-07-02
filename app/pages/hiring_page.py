import streamlit as st
import requests
import pandas as pd
import json
from io import StringIO

def app():
    st.title("Hiring Page")
    st.write("Welcome to the Hiring Page!")

    st.markdown(
        """
        # Support to HR decisions in new hiring
        ## Based on job opening requirements and applicant's information, which applicant is more likely to stay in the company?
        """
    )

    # ************************** Connection to API ***************************************
    uploaded_file = st.file_uploader("Upload a JSON file")

    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()

        json_data = json.loads(bytes_data)
        X = pd.DataFrame(json_data)
        hiring_features_cols = ['Department','GEO','Role',
                                'average_montly_hours','salary',
                                'Will_Relocate','Gender']

        X = X[hiring_features_cols]

        st.write(f"## Description of candidates")
        st.write(X)

        # API endpoint
        URL = "https://hrdataanalytics-4bdr2jy2qa-od.a.run.app/upload_predict_hiring"

        # Sending POST request and saving the response as a response object
        r = requests.post(url=URL, files={'upload_file': bytes_data})

        st.write(f"## Ranking of applicants based on probability to stay with the company:")
        ranking = json.loads(r.text)
        ranking_df = pd.DataFrame(ranking['Ranking'])
        st.write(ranking_df)
    else:
        st.write("Waiting for input...")
Update app.py
