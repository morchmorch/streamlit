#plotly_chart.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
#blah

def get_data () :
    df_custom = pd.read_csv ("https://investrecipes.s3.amazonaws.com/basic/all_stocks/just-all-custom-finviz.csv")
    return df_custom


def draw_f_fig (df_custom, sector_option) :

    if sector_option is not 'All':
        df_custom = df_custom [ df_custom.Sector == sector_option  ]. sort_values(by =  'Net Income Margin % (FY)')
    else :
        df_custom = df_custom. sort_values(by =  'Net Income Margin % (FY)')

    camera = dict ( up=dict(x=1.5, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=2.5, y=1.5, z=2) )

    fig = px.scatter_3d(
            df_custom ,
            #x="Profit Margin",
            #y="Industry",
            z = 'Total Revenues/CAGR (2Y FY)',
            y =  'Net Income Margin % (FY)' ,
            x='Industry',
            width=1000,
            height=800,
            hover_name="Name",
            #hover_data= ['Company','Market Cap','Profit Margin'],
            hover_data= ['Name', 'Ticker', 'Industry',  'Total Revenues/CAGR (2Y FY)', 'Net Income Margin % (FY)'],
            #size = 'Market Cap',
            labels={ 'Total Revenues/CAGR (2Y FY)' : 'Revenues CAGR (2YFY)' ,'Net Income Margin % (FY)':'NI Margin(%)', "Industry": ""} ,
            color = 'Industry',
            color_continuous_scale=px.colors.sequential.RdBu_r,
            #template="plotly_white"


    )
    fig.update_layout(
        scene = dict(
            xaxis = dict (nticks=0,ticktext =["x"], ticks='outside', gridcolor="white", showbackground=True,backgroundcolor="rgb(200, 200, 230)",
            tickfont=dict(
                                color='white',
                                size=1,
                                family='Old Standard TT, serif',)
            ) ,
            xaxis_title='',
            #xaxis_showspikes=False,
            yaxis = dict(nticks=0, backgroundcolor="rgb(230, 230,200)" ),
            zaxis = dict( nticks=0 ,ticktext =[""] ),
            
            
            camera=camera
        ),
    )
    #st.sidebar.multiselect( "Please select the sector:", options=df_custom["Sector"].unique(),)

    st.plotly_chart(fig)

def take_string_give_url (option):
    url_dict = {
        '52wkhigh' :  'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_crossover_52wkhigh-stockcharts.csv-agg.html',
        '60plusrsi' : 'https://investrecipes.s3.amazonaws.com/all_sectors/fundamental/comparisoncharts/stockworld_all_60plusrsi-finviz.csv-agg.html',
        'insider_buying': 'https://investrecipes.s3.amazonaws.com/apps/insiderbuying/insider-buying-finviz.csv-agg.html',
        'in_news': 'https://investrecipes.s3.amazonaws.com/apps/news/finviz_major_news.csv-agg.html',
        'unusual_volume': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_unusual-volume-finviz-agg.html',
        'price_up_and_volume_up': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_price_up_volume_up-stockcharts.csv-agg.html',
        'golden_cross': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_crossover_50_200-stockcharts.csv-agg.html',
        'etf_in_momentum' : 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_industries_momentum-stockcharts.csv.html',
        'etf_etfs_rsi': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_etfs_aroon-positive-pmo-above-zero_pmo-above-signal_cmf-positive-stockcharts.csv.html',
        'etf_in_rsi': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_industries_aroon_rsi_slope-stockcharts.csv.html' ,
        'koyfin_etf' : 'https://investrecipes.s3.amazonaws.com/industry/fundamental/comparisoncharts/etfworld_industry_all_koyfin-list.png'

    }
    return url_dict[option]

def draw_trend_fig():

    l = ['52wkhigh', '60plusrsi','golden_cross']
    sector_option = st.radio( "Technical",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    st.caption ( ', '.join (df[cols].symbols.tolist()) )
    st.write(df[cols])
 

def draw_external_fig():


    l = ['insider_buying', 'in_news']
    sector_option = st.radio( "External",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    st.caption ( ', '.join (df[cols].symbols.tolist()) )
    st.write(df[cols])
 


def draw_technical_fig():


    l = ['unusual_volume', 'price_up_and_volume_up']
    sector_option = st.radio( "Technical",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    st.caption ( ', '.join (df[cols].symbols.tolist()) )
    st.write(df[cols])

def draw_etf_fig() :
    l = ['etf_in_momentum', 'etf_etfs_rsi','etf_in_rsi']
    sector_option = st.radio( "Technical (stocks hitting milestones)",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = ['Symbol','Name']
    st.write(df[cols])


def draw_etf_image() :
    l = ['koyfin_etf']
    sector_option = st.radio( "Technical",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.image ( take_string_give_url ( sector_option ) )


## main


kdf = pd.read_csv ('https://investrecipes.s3.amazonaws.com/koyfin_all_stocks.csv')

kdf['growth_evsales_ratio'] = kdf['Total Revenues/CAGR (2Y FY)'] / kdf[ 'EV/Sales (EST FY1)' ]

kdf['growth_evsales_ratio'] = pd.to_numeric (kdf['growth_evsales_ratio'])

kdf = kdf [ kdf [  'Net Income Margin % (FY)' ] > 10 ]

kdf = kdf [ kdf [  'Net Income Margin % (FY)' ] < 100 ]

kdf = kdf [ kdf [ 'Total Revenues/CAGR (2Y FY)' ] > 10 ]

kdf = kdf [ kdf [ 'Total Revenues/CAGR (2Y FY)' ] < 1000 ]



#df_custom = kdf.copy()
#l = df_custom.Sector.unique().tolist()
#l.append('All')

#l = ['52wkhigh', '60plusrsi']
#sector_option = st.radio( "Technical",  l  )
#st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#sector_option =  st.selectbox ( 'Select Sector', df_custom.Sector.unique().tolist() )
st.set_page_config(page_title="Investrecipes",layout='wide')


tab1, tab2 = st.tabs(["stocks", "etfs"])

with tab1:
    
    st.header("Stocks")

    col1, col2 , col3 = st.columns(3)

    with col1:
        draw_trend_fig()
    with col2:
        draw_external_fig()
    with col3:
        draw_technical_fig()

    st.caption ('Correlated')
    df = pd.read_html ('https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_runbook_sources_ranking-agg.html')[0]
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    #st.write(df[cols])
    st.dataframe (use_container_width = True)
with tab2:
    st.header("ETFs")
    
    col1, col2 = st.columns(2)

    with col1:
        draw_etf_fig()
    with col2 :
        draw_etf_image() 

