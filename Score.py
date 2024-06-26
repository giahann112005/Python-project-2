import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import datetime
import numpy as np
import plotly as plt

sp = pd.read_csv('study_performance.csv')

by_what_1 = st.radio(
            "Choose a category:",
            ('lunch', 'gender', 'test_preparation_course','parental_level_of_education'), horizontal=True,
            key = "r1")
 sp['average_score'] = sp.apply(lambda row:(row.math_score + row.reading_score + row.writing_score) / 3, axis = 1)
fig1 = px.pie(sp, values = "average_score", names = by_what_1, hole = 0.7) 
fig1.update_traces(text = sp[by_what_1], textposition = "outside")
st.plotly_chart(fig1, theme = "streamlit", use_container_width=True)
