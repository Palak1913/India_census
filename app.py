# -*- coding: utf-8 -*-
"""
Created on Mon May 12 21:37:48 2025

@author: rkcas
"""

# Import 

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px



st.set_page_config(layout='wide')

p1 = r'district wise centroids.csv'
p2 = r'india-districts-census-2011.csv'

ll = pd.read_csv(p1)
cencus = pd.read_csv(p2)

ll.isnull().sum()

cencus = cencus[['District code','District name','Population','Male','Female','Literate','Households_with_Internet']]

latlong = ll.merge(cencus , left_on = 'District' , right_on = 'District name')
latlong  = latlong.drop(columns = 'District name')

latlong['sex_ratio'] = round((latlong['Female'] / latlong['Male'])*100)
latlong['litracy_rate'] = round((latlong['Literate'] / latlong['Population'])*100)

latlong  = latlong.drop(columns = ['Male','Female','Literate'])

st.sidebar.title('India Data')

state = list(latlong['State'].unique())
state.insert(0,'Overall India')
            

state_selected = st.sidebar.selectbox('State', state)
primary = st.sidebar.selectbox('primary', set(latlong.columns[5:]))
secondary = st.sidebar.selectbox('secondary', set(latlong.columns[5:]))

button = st.sidebar.button('Plot Graph')

if button:
    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    
    if state_selected == 'Overall India':
        fig = px.scatter_map(latlong, lat = 'Latitude' , lon = 'Longitude' , size = latlong[primary] , color=latlong[secondary], zoom=4 , hover_name='District',height=900)
        st.plotly_chart(fig,use_container_width=True)
    
    else:
        selected = latlong[latlong['State'] == state_selected]
        fig = px.scatter_map(selected, lat = 'Latitude' , lon = 'Longitude' , size = selected[primary] , color=selected[secondary],zoom=6 , hover_name='District',height=900)
        st.plotly_chart(fig,use_container_width=True)
    
    

