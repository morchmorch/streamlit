#plotly_chart.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("Welcome to Streamlit!")

df_custom = pd.read_csv ("https://investrecipes.s3.amazonaws.com/basic/all_stocks/just-all-custom-finviz.csv")

fig = px.scatter_3d(
        df_ec,
        #x="Profit Margin",
        #y="Industry",
        z = 'Sector',
        y = 'Market Cap' ,
        x='Industry',

)

st.write("Pie chart in Streamlit")
st.plotly_chart(fig)
