#plotly_chart.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
#blah

def get_data () :
    df_custom = pd.read_csv ("https://investrecipes.s3.amazonaws.com/basic/all_stocks/just-all-custom-finviz.csv")
    return df_custom

def clean_data () :
    df_arr = []

    slist = ['xlf','xle','xlk','xlp','xlre','xlk','xlc','xlv','xlb','xly']
    for sstr in slist :

        try :

            surl = 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/' + sstr + '-industries-rsi-stockcharts.csv'
            
            print (surl)
            fdf = pd.read_csv (surl)
            df_arr.append(fdf)
            #fig = px.strip(fdf.sort_values (by='Daily RSI(14,Daily Close)',ascending=False), x='Daily RSI(14,Daily Close)',y='Industry',color=fdf.Sector,hover_name="Name",hover_data=['Symbol'])
            #fig.show()
        except Exception as e: print(e)


    adf = pd.concat(df_arr)

    df_arr = []
    slist = ['xlf','xle','xlk','xlp','xlre','xlk','xlc','xlv','xlb','xly']
    for sstr in slist :

        try :
            surl = 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/' + sstr + '-industries-rsii-slope-stockcharts.csv'
            
            print (surl)
            fdf = pd.read_csv (surl)
            df_arr.append(fdf)
            #fig = px.strip(fdf.sort_values (by='Daily RSI(14,Daily Close)',ascending=False), x='Daily RSI(14,Daily Close)',y='Industry',color=fdf.Sector,hover_name="Name",hover_data=['Symbol'])
            #fig.show()
        except Exception as e: print(e)

    rsislopedf = pd.concat(df_arr)


    df_arr = []
    slist = ['xlf','xle','xlk','xlp','xlre','xlk','xlc','xlv','xlb','xly']
    for sstr in slist :
        try :

            surl = 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/' + sstr + '-industries-adx-slope-stockcharts.csv' 
            
            print (surl)
            fdf = pd.read_csv (surl)
            df_arr.append(fdf)
            
            #fig = px.strip(fdf.sort_values (by='Daily RSI(14,Daily Close)',ascending=False), x='Daily RSI(14,Daily Close)',y='Industry',color=fdf.Sector,hover_name="Name",hover_data=['Symbol'])
            #fig.show()
        except Exception as e: print(e)

    adxslopedf = pd.concat(df_arr)
    
    rsiandslopetdf = pd.merge(adf,rsislopedf[['Daily Slope(5,Daily RSI(14,Daily Close))','Symbol']], on = ['Symbol'])

    rsiandslopedf = pd.merge(rsiandslopetdf,adxslopedf[['Daily Slope(5,Daily ADX Line(14))','Symbol']], on = ['Symbol'])


    df_custom = pd.read_csv ("https://investrecipes.s3.amazonaws.com/basic/all_stocks/just-all-custom-finviz.csv")

    df_custom ['Symbol']=df_custom['Ticker']

    df_custom ['Profit Margin'] = df_custom ['Profit Margin'].fillna(0)
    df_custom ['Market Cap'] = df_custom ['Market Cap'].fillna(0)
    df_custom ['Sales growth quarter over quarter'] = df_custom ['Sales growth quarter over quarter'].fillna(0)



    df_custom ['Profit Margin'] = df_custom ['Profit Margin'].astype(str).str.split('%').str.get(0)

    df_custom ['Profit Margin'] = df_custom ['Profit Margin'].astype(float).astype(int)


    df_custom ['Sales growth quarter over quarter'] = df_custom ['Sales growth quarter over quarter'].astype(str).str.split('%').str.get(0)

    df_custom ['Sales growth quarter over quarter'] = df_custom ['Sales growth quarter over quarter'].astype(float).astype(int)


    rsiandslopedf['Ticker'] = rsiandslopedf ['Symbol']

    df_sources_custom = rsiandslopedf.merge( df_custom[['Ticker','Symbol','Company',  'Market Cap','Performance (Week)', 'Performance (Month)', '52-Week High', '52-Week Low','20-Day Simple Moving Average', '50-Day Simple Moving Average', '200-Day Simple Moving Average', 'Relative Strength Index (14)', 'Analyst Recom', 'Relative Volume','Earnings Date' ,'Sales growth quarter over quarter', 'Profit Margin','EPS growth next year' ]], on = 'Ticker')


    df_sources_custom ['Market Cap'] = df_sources_custom ['Market Cap'].fillna(0)


    df_sources_custom ['Profit Margin'] = df_sources_custom ['Profit Margin'].fillna(0)

    return df_sources_custom


def draw_f_fig (df_custom) :

    fig = px.scatter_3d(
            df_custom, 
            #x="Profit Margin",
            #y="Industry",
            z = 'Total Revenues/CAGR (1Y FY)',
            y = 'Net Income Margin % (LTM)' ,
            x='Industry',
            width=1000,
            height=800,
            #hover_name="Company",
            #hover_data= ['Company','Market Cap','Profit Margin'],
            hover_data= ['Name', 'Ticker' ],
            #size = 'Market Cap',
            color = 'Industry',
            color_continuous_scale=px.colors.sequential.RdBu_r,
            #template="plotly_white"


    )
    #st.sidebar.multiselect( "Please select the sector:", options=df_custom["Sector"].unique(),)

    st.plotly_chart(fig)


def draw_t_fig (df_custom, sector_optionn) :
    df_custom = df_custom[ df_custom ['Daily RSI(14,Daily Close)'] > 50 ]
    df_custom = df_custom[ df_custom ['Daily Slope(5,Daily RSI(14,Daily Close))'] > 0 ]
    df_custom = df_custom[ df_custom [ 'Daily Slope(5,Daily ADX Line(14))' ] > 0 ]

    fig = px.scatter_3d(
            df_custom,
            #df_custom [ df_custom.Sector == sector_option ],
            #x="Profit Margin",
            #y="Industry",
            z = 'Daily Slope(5,Daily RSI(14,Daily Close))',
            y = 'Daily Slope(5,Daily ADX Line(14))' ,
            x='Industry',
            width=1000,
            height=800,
            #hover_name="Company",
            hover_data= ['Name', 'Ticker' ],
            #size = 'Market Cap',
            color = 'Industry',
            color_continuous_scale=px.colors.sequential.RdBu_r,
            #template="plotly_white"


    )
    st.plotly_chart(fig)




## main

#df_custom = get_data ()

#df_custom = clean_data()

#df_custom = pd.read_csv ( "https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/industries-rsi-adx-consolidated-stockcharts.csv")

kdf = pd.read_csv ('https://investrecipes.s3.amazonaws.com/koyfin_all_stocks.csv')

kdf['growth_evsales_ratio'] = kdf['Total Revenues/CAGR (2Y FY)'] / kdf[ 'EV/Sales (EST FY1)' ]

kdf['growth_evsales_ratio'] = pd.to_numeric (kdf['growth_evsales_ratio'])

kdf = kdf [ kdf [  'Net Income Margin % (FY)' ] > 10 ]

kdf = kdf [ kdf [  'Net Income Margin % (FY)' ] < 100 ]

kdf = kdf [ kdf [ 'Total Revenues/CAGR (2Y FY)' ] > 10 ]

kdf = kdf [ kdf [ 'Total Revenues/CAGR (2Y FY)' ] < 1000 ]

df_custom = kdf.copy()

#sector_option =  st.selectbox ( 'Select Sector', df_custom.Sector.unique().tolist() )


draw_f_fig(df_custom)

#st.plotly_chart(fig)
#st.dataframe(df_custom)

