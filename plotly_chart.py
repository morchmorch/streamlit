#plotly_chart.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df_custom = pd.read_csv ("https://investrecipes.s3.amazonaws.com/basic/all_stocks/just-all-custom-finviz.csv")
sector_option =  st.selectbox ( df_custom.Sector.unique().tolist() )

st.write('You selected:', sector_option)


st.title("Welcome to Streamlit!")


fig = px.scatter_3d(
        df_custom,
        #x="Profit Margin",
        #y="Industry",
        z = 'Sector',
        y = 'Market Cap' ,
        x='Industry',

)
st.sidebar.multiselect(
    "Please select the sector:",
    options=df_custom["Sector"].unique(),
    )

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.button('1')
with col2:
    st.button('2')
with col3:
    st.button('3')

st.write("Pie chart in Streamlit")
st.plotly_chart(fig)

st.dataframe(df_custom)
