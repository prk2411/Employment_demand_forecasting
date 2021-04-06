# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:05:13 2021

@author: PRK
"""

import streamlit as st
import pickle
from statsmodels.tsa.statespace.sarimax import SARIMAX
from analysis_functions import plot_models, industry_preprocess

def forecasting(df):
    st.title('Forecasting Employment in Industries')
    
    st.subheader('Select an Industry to forecast')
    industry_list = df['NOC'].tolist()
    industry_name = st.selectbox('',(industry_list))
    fig = plot_models(df, industry_name)
    st.plotly_chart(fig, use_container_width=True)