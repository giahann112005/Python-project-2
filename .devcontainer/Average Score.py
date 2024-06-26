import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import datetime
import numpy as np
import plotly as plt

sp = pd.read_csv('study_performance.csv')

by_what_2 = st.radio(
            "Choose a subject score:",
            ('math_score', 'reading_score', 'writing_score'), 
            horizontal = True,
            key = "r2")
gender = ['male', 'female' ]
st.subheader("")
selected_gender = st.selectbox("Seletct gender", gender)
st.caption(f"You selected: {selected_gender}")
if selected_gender:
 filterd_data = sp[sp['gender'] == selected_gender]
chart= px.box(filterd_data,x= filterd_data['race_ethnicity'],
                  y= filterd_data[by_what_2], notched=True, points ='all', 
                  labels={"average_score": "average_score"},)
chart.update_layout(title=f"Students score in each subject of different ethnicity group in {selected_gender}",
                        xaxis_title="Race/Ethnicity", yaxis_title="Score",xaxis_tickangle=0)
chart.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=0, opacity=0.6)
st.plotly_chart(chart)
