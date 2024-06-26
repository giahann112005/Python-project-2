import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import datetime
import numpy as np
import plotly as plt

sp = pd.read_csv('study_performance.csv')

st.sidebar.header('Filter Options')
gender = st.sidebar.multiselect('Gender', options=sp['gender'].unique(), default=sp['gender'].unique())
race_ethnicity = st.sidebar.multiselect('Race/Ethnicity', options=sp['race_ethnicity'].unique(), default=sp['race_ethnicity'].unique())
parental_level_of_education = st.sidebar.multiselect('Parental Level of Education', options=sp['parental_level_of_education'].unique(), default=sp['parental_level_of_education'].unique())
lunch = st.sidebar.multiselect('Lunch', options=sp['lunch'].unique(), default=sp['lunch'].unique())
test_preparation_course = st.sidebar.multiselect('Test Preparation Course', options=sp['test_preparation_course'].unique(), default=sp['test_preparation_course'].unique())

# Filter the data based on user input
filtered_data = sp[
    (sp['gender'].isin(gender)) &
    (sp['race_ethnicity'].isin(race_ethnicity)) &
    (sp['parental_level_of_education'].isin(parental_level_of_education)) &
    (sp['lunch'].isin(lunch)) &
    (sp['test_preparation_course'].isin(test_preparation_course))
]

# Create an Altair chart
chart = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x='math_score',
    y='reading_score',
    color='writing_score',
    tooltip=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course', 'math_score', 'reading_score', 'writing_score']
).interactive()

# Display the chart in the Streamlit app
st.altair_chart(chart, use_container_width=True)
