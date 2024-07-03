import streamlit as st

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
