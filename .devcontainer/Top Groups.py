import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import datetime
import numpy as np
import plotly as plt

sp = pd.read_csv('study_performance.csv')

average_scores = sp.groupby('parental_level_of_education')[['math_score', 'reading_score', 'writing_score']].mean().reset_index()
average_scores['average_score'] = average_scores[['math_score', 'reading_score', 'writing_score']].mean(axis=1)
st.title('Top Groups by Average Score')
top_n = st.slider('Select number of groups', 1, len(average_scores), 1)
top_groups = average_scores.nlargest(top_n, 'average_score')
fig = px.bar(top_groups, x='parental_level_of_education', y='average_score', title=f"Top {top_n} Groups That Have Highest Average Score")
st.plotly_chart(fig)
