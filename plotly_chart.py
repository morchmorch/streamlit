#plotly_chart.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df_custom = pd.read_csv ("https://investrecipes.s3.amazonaws.com/basic/all_stocks/just-all-custom-finviz.csv")
sector_option =  st.selectbox ( 'Select Sector', df_custom.Sector.unique().tolist() )

st.write('You selected:', sector_option)


#st.title("Welcome to Streamlit!")


fig = px.scatter_3d(
        df_custom [ df_custom.Sector == sector_option ],
        #x="Profit Margin",
        #y="Industry",
        z = 'Sector',
        y = 'Market Cap' ,
        x='Industry',
        width=1000,
        height=800,
        #hover_name="Company",
        hover_data= ['Company','Market Cap','Profit Margin'],
        #size = 'Market Cap',
        color = 'Industry',
        color_continuous_scale=px.colors.sequential.RdBu_r,
        #template="plotly_white"


)
#st.sidebar.multiselect( "Please select the sector:", options=df_custom["Sector"].unique(),)

st.write("Pie chart in Streamlit")
st.plotly_chart(fig)

st.dataframe(df_custom)
