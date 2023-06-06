#plotly_chart.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image

#blah

def get_data () :
    df_custom = pd.read_csv ("https://investrecipes.s3.amazonaws.com/basic/all_stocks/just-all-custom-finviz.csv")
    return df_custom

def draw_t_fig () :
    tdf = pd.read_csv ( "https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/industries-rsi-adx-consolidated-stockcharts.csv")
    #print (tdf.shape)
    #kdf = pd.read_csv ('https://investrecipes.s3.amazonaws.com/koyfin_all_stocks.csv')

    #kdf['growth_evsales_ratio'] = kdf['Total Revenues/CAGR (2Y FY)'] / kdf[ 'EV/Sales (EST FY1)' ]

    #kdf['growth_evsales_ratio'] = pd.to_numeric (kdf['growth_evsales_ratio'])

    #kdf = kdf [ kdf [  'Net Income Margin % (FY)' ] > 10 ]

    #kdf = kdf [ kdf [  'Net Income Margin % (FY)' ] < 100 ]

    #kdf = kdf [ kdf [ 'Total Revenues/CAGR (2Y FY)' ] > 10 ]

    #kdf = kdf [ kdf [ 'Total Revenues/CAGR (2Y FY)' ] < 1000 ]


    st.write (tdf.columns.tolist())
    df_custom = tdf.copy()
    l = df_custom.Sector.unique().tolist()
    l.append('All')
    sector_option = st.radio( "Sector",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df_custom = df_custom[ df_custom ['Daily RSI(14,Daily Close)'] > 40 ]
    df_custom = df_custom[ df_custom ['Daily Slope(5,Daily RSI(14,Daily Close))'] > 0 ]
    #df_custom = df_custom[ df_custom [ 'Daily Slope(5,Daily ADX Line(14))' ] > 0 ]
    df_custom = df_custom[ df_custom [ 'Daily ADX Line(14)' ] > 0 ]

    if sector_option is not 'All':
        df_custom = df_custom [ df_custom.Sector == sector_option  ]. sort_values(by ='Daily ADX Line(14)' )
    else :
        df_custom = df_custom. sort_values(by  = 'Daily ADX Line(14)' )

    camera = dict ( up=dict(x=1.5, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=2.5, y=1.5, z=2) )


    fig = px.scatter_3d(
            df_custom,
            #df_custom [ df_custom.Sector == sector_option ],
            #x="Profit Margin",
            #y="Industry",
            z = 'Daily Slope(5,Daily RSI(14,Daily Close))',
            y = 'Daily ADX Line(14)' ,
            x='Industry',
            width=1000,
            height=800,
            hover_name="Name",
            #hover_data= ['Company','Market Cap','Profit Margin'],
            hover_data= ['Name', 'Ticker', 'Industry' ],
            #size = 'Market Cap',
            labels={ 'Daily Slope(5,Daily RSI(14,Daily Close))' : 'rsi-slope' ,'Daily Slope(5,Daily ADX Line(14))':'adx-sllope', "Industry": ""} ,
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


def draw_f_fig () :

    kdf = pd.read_csv ('https://investrecipes.s3.amazonaws.com/koyfin_all_companies.csv')
    
    kdf = kdf [ kdf [  'Net Income Margin % (FY)' ] < 100 ]
    kdf = kdf [ kdf [  'Net Income Margin % (FY)' ] > 0 ]

    st.write (kdf.columns.tolist())
    kdf['growth_evsales_ratio'] = kdf['Total Revenues/CAGR (2Y FY)'] / kdf[ 'EV/Sales (EST FY1)' ]

    kdf['growth_evsales_ratio'] = pd.to_numeric (kdf['growth_evsales_ratio'])

    #kdf = kdf [ kdf [  'Net Income Margin % (FY)' ] > 10 ]


    #kdf = kdf [ kdf [ 'Total Revenues/CAGR (2Y FY)' ] > 10 ]

    #kdf = kdf [ kdf [ 'Total Revenues/CAGR (2Y FY)' ] < 1000 ]



    df_custom = kdf.copy()
    l = df_custom.Sector.unique().tolist()
    l.append('All')
    sector_option = st.radio( "Sector",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    #sector_option =  st.selectbox ( 'Select Sector', df_custom.Sector.unique().tolist() )



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
            hover_data= ['Name', 'Ticker', 'Industry',  'Total Revenues/CAGR (2Y FY)', 'Net Income Margin % (FY)', "Total Revenues (FY)"],
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
        '52wkhigh(fv)': 'https://investrecipes.s3.amazonaws.com/all_stocks/technical/52wkhigh/stockworld_all_52wkhigh-finviz.csv-agg.html',
        '60plusrsi' : 'https://investrecipes.s3.amazonaws.com/all_sectors/fundamental/comparisoncharts/stockworld_all_60plusrsi-finviz.csv-agg.html',
        'insider_buying': 'https://investrecipes.s3.amazonaws.com/apps/insiderbuying/insider-buying-finviz.csv-agg.html',
        'in_news': 'https://investrecipes.s3.amazonaws.com/apps/news/finviz_major_news.csv-agg.html',
        'strong_patterns': 'https://investrecipes.s3.amazonaws.com/all_stocks/technical/strongpatterns/stockworld_all_52wkhigh-strong-patterns-finviz.csv-agg.html',
        'etf_unusual_relative_volume': 'https://investrecipes.s3.amazonaws.com/apps/volumegainers/etfworld-relative_volume-finviz.csv-agg.html',
        'stock_unusual_relative_volume': 'https://investrecipes.s3.amazonaws.com/apps/volumegainers/stockworld-relative-volume_finviz.csv-agg.html',
        'price_up_and_volume_up': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_price_up_volume_up-stockcharts.csv-agg.html',
        'high_adx_slope':'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_adx_slope-stockcharts.csv-agg.html',
        'golden_cross': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_crossover_50_200-stockcharts.csv-agg.html',
        'industries_momentum' : 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_industries_momentum-stockcharts.csv.html',
        'etf_etfs_rsi': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_etfs_aroon-positive-pmo-above-zero_pmo-above-signal_cmf-positive-stockcharts.csv.html',
        'industries_rsi': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_industries_aroon_rsi_slope-stockcharts.csv.html' ,
        'industries_pmo_cmf': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_etfs_aroon-positive-pmo-above-zero_pmo-above-signal_cmf-positive-stockcharts.csv-agg.html',
        'koyfin_etf' : 'https://investrecipes.s3.amazonaws.com/industry/fundamental/comparisoncharts/etfworld_industry_all_koyfin-list.png',
        'etf_heatmap' : 'https://investrecipes.s3.amazonaws.com/industry/fundamental/comparisoncharts/etfworld_industry_all_heatmap-finviz.png',
        'macro_market_charts': 'https://investrecipes.s3.amazonaws.com/market/fundamental/comparisoncharts/etfworld_sector_all_market-finviz-charts.png',    
        'sector_market_charts': 'https://investrecipes.s3.amazonaws.com/sector/fundamental/comparisoncharts/etfworld_sector_all_finviz-charts.png',
        'sector_rrg': 'https://investrecipes.s3.amazonaws.com/sector/fundamental/comparisoncharts/etfworld_sector_all_stockcharts-rrg.png',
        'industries_20_50_sma': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_industries_sma_20_50-stockcharts.csv.html',
        'stocks_20_50_sma': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_sma_20_50-stockcharts.csv-agg.html',
        'etfs_20_50_sma' : 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfkworld_adx_slope-stockcharts.csv.html',
        'industries_50_200_sma': 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_industries_sma_50_200-stockcharts.csv.html',
        'etfs_50_200_sma':'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/etfworld_sma_50_200-stockcharts.csv.html',
        'stocks_50_200_sma' : 'https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_sma_50_200-stockcharts.csv-agg.html'

    }
    return url_dict[option]

def draw_milestone_fig():

    l = [ '60plusrsi','52wkhigh', '52wkhigh(fv)', 'golden_cross']
    sector_option = st.radio( "Stocks hitting technical milestones",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    #st.caption ( ', '.join (df[cols].symbols.tolist()) )
    st.write(df[cols])
    st.markdown("""---""") 
 
    st.caption ('charts')
    st.image (  take_string_give_url ( sector_option ).split('.csv')[0] + '.png' )
    #st.write ( take_string_give_url ( sector_option ).split('-agg')[0] + '-rrg.png' )
    st.image (  take_string_give_url ( sector_option ).split('-agg')[0] + '-rrg.png' )
    st.markdown("""---""") 
    cols = ['Ticker','Company','Profit Margin','Sales growth quarter over quarter']
    
    html_page =  take_string_give_url ( sector_option ).split('-agg')[0] + ".html"
    df = pd.read_html ( html_page )[0]
    st.caption ('fundamentals')

    if not df.empty :

        try :
            st.write(df[cols])
        except :
            #st.write (df.columns.tolist())
            st.write (df [['Symbol','Name','SCTR']] )
     
def draw_external_fig():


    l = ['insider_buying', 'in_news']
    sector_option = st.radio( "Stocks with external tailwinds",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    st.caption ( ', '.join (df[cols].symbols.tolist()) )
    st.write(df[cols])
    st.markdown("""---""")  
    #st.write (  take_string_give_url ( sector_option ).split('-agg')[0] + '-charts.png' )
 
    st.caption ('charts')
    st.image (  take_string_give_url ( sector_option ).split('.csv')[0] + '-charts.png' )
    #st.write ( take_string_give_url ( sector_option ).split('-agg')[0] + '-rrg.png' )
    st.image (  take_string_give_url ( sector_option ).split('-agg')[0] + '-rrg.png' )
    st.markdown("""---""") 

    cols = ['Ticker','Company','Profit Margin','Sales growth quarter over quarter']
    html_page =  take_string_give_url ( sector_option ).split('-agg')[0] + ".html"
    df = pd.read_html ( html_page )[0]
    st.caption ('fundamentals')
    st.write(df[cols])
    
def draw_technical_fig():


    l = [ 'strong_patterns', 'etf_unusual_relative_volume', 'stock_unusual_relative_volume' , 'price_up_and_volume_up','high_adx_slope']
    sector_option = st.radio( "Stocks with technical tailwinds",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.markdown("""---""")  

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    st.caption ( ', '.join (df[cols].symbols.tolist()) )
    st.write(df[cols])
    st.markdown("""---""")  
 
    st.caption ('charts')
    st.image (  take_string_give_url ( sector_option ).split('.csv')[0] + '.png' )
    #st.write ( take_string_give_url ( sector_option ).split('-agg')[0] + '-rrg.png' )
    st.image (  take_string_give_url ( sector_option ).split('-agg')[0] + '-rrg.png' )
    st.markdown("""---""") 

    cols = ['Ticker','Company','Profit Margin','Sales growth quarter over quarter']
    html_page =  take_string_give_url ( sector_option ).split('-agg')[0] + ".html"
    try :
        df = pd.read_html ( html_page )[0]
        st.caption ('fundamentals')
        st.write(df[cols])
    except : st.write ('no page found')
    

def draw_etf_fig() :
    l = ['industries_momentum', 'industries_rsi', 'etf_etfs_rsi']
    sector_option = st.radio( "Industry Groups and ETFs with Technical Strengths",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = ['Symbol','Name']
    st.write(df[cols])
    st.image (take_string_give_url ( sector_option ).split('.html')[0]+'-rrg.png')

def draw_etf_image() :
    l = ['koyfin_etf','etf_heatmap']
    sector_option = st.radio( "Performance",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.image ( take_string_give_url ( sector_option ) )

def draw_market_sector() :

    l = ['macro_market_charts','sector_market_charts','sector_rrg']
    sectors = ['xlp','xlv','xlre','xlf','xlc','xle','xlre','xlb','xli','xlk','xly']
    l.extend(['xlp','xlv','xlre','xlf','xlc','xle','xlre','xlb','xli','xlk','xly'])
    sector_option = st.radio( "Macro and Sector Weekly Performance",  l , key = 'Market Performance' )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    
    if 'x' not in sector_option :
        images = []
        images.append ( take_string_give_url ( sector_option ) )
        images.append ( take_string_give_url ( sector_option ).split('-charts')[0]+'-list.png' )
        st.image (images, width=1000)
        #st.image ( take_string_give_url ( sector_option ) )
        #st.image ( take_string_give_url ( sector_option ).split('-charts')[0]+'-list.png' )

    else :
        adf = pd.read_html('https://investrecipes.s3.amazonaws.com/all-files.html')[0]
        #xlydf = adf [ (adf.key.str.contains('.png') ) & (adf.key.str.contains('industry_'+sector_option)) ]
        #images = xlydf.key.tolist()
        images = adf.key.tolist()

        # industry rrg
        #i = [x for x in images if 'industries_rrg' in x and 'stockworld' in x]
        i = [x for x in adf.key.tolist() if 'technical/rrg/' in x and 'industr' in x] 
        i = [ x for x in i if str(sector_option).strip() in x]
        urls = [ 'https://investrecipes.s3.amazonaws.com/'+ x for x in i ]
        captions = [x.split('/')[-1].split('-finviz')[0] for x in urls]

        st.write ('industry and companies rrg')
        st.image(urls,width=600,caption=captions)
 
        # companiees rrg
        #i= [x for x in images if 'stockworld_' + sector_option + '_rrg' in  x]
        i = [x for x in adf.key.tolist() if 'technical/rrg/' in x and 'stockcharts_'+ sector_option+"_rrg" in x ] 
        i = [ x for x in i if sector_option in x]
        urls = [ 'https://investrecipes.s3.amazonaws.com/'+ x for x in i]
        captions = [x.split('/')[-1].split('-finviz')[0] for x in urls]
        #st.image(urls,width=600,caption=captions)
 

         # koyfin etf
        i = [x for x in images if 'koyfin' in x and 'etf' in x and str(sector_option).strip() in x and 'watchlist' in x]
        urls = [ 'https://investrecipes.s3.amazonaws.com/'+ x for x in i]
        captions = [x.split('/')[-1].split('-finviz')[0] for x in urls]
        
        st.write (' ETF ')
        
        st.image(urls,width=600,caption=captions)

        #finviz companies by industry
        i = [x for x in images if 'industry_' in x and 'finviz' in x and 'rrg' not in x and '60' not in x and '52' not in x and str(sector_option).strip() in x and 'png' in x]
        urls = [ 'https://investrecipes.s3.amazonaws.com/'+ x for x in i]
        captions = [x.split('/')[-1].split('-finviz')[-1] for x in i]
        st.write ('companies by industry')
        st.image(urls,width=600,caption=i)
        
        
        

        
def draw_momentum_figs():
    print ( 'draw_momentum_figs' )
    l = ['industries_rrg', "companies_rrg"]
    sector_option = st.radio( "Relative Rotation Graphs, Industries and Companies in each Sector",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    images  = [] 
    adf = pd.read_html('https://investrecipes.s3.amazonaws.com/all-files.html')[0]

    if 'industries' in sector_option :
        images =  [ x for x in adf.key.tolist() if 'rrg' in x and 'industries_' in x and 'stock' in x and 'industry_' in x] 
    if 'companies' in sector_option:
        images = [ x for x in adf.key.tolist() if x.startswith ('industry_') and x.endswith('.png') and 'rrg' in x  and 'companies' in x ]


    urls = [ 'https://investrecipes.s3.amazonaws.com/'+ x for x in images]
    captions = [x.split('/')[-1].split('-finviz')[0] for x in urls]
    st.image(urls,width=600,caption=captions)
 


## main


#kdf = pd.read_csv ('https://investrecipes.s3.amazonaws.com/koyfin_all_stocks.csv')

#kdf['growth_evsales_ratio'] = kdf['Total Revenues/CAGR (1Y FY)'] / kdf[ 'EV/Sales (EST FY1)' ]

#kdf['growth_evsales_ratio'] = pd.to_numeric (kdf['growth_evsales_ratio'])


#kdf = kdf [ kdf [  'Net Income Margin % (LTM)' ] < 100 ]


#kdf = kdf [ kdf [ 'Total Revenues/CAGR (1Y FY)' ] < 1000 ]



#df_custom = kdf.copy()
#l = df_custom.Sector.unique().tolist()
#l.append('All')

#l = ['52wkhigh', '60plusrsi']
#sector_option = st.radio( "Technical",  l  )
#st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#sector_option =  st.selectbox ( 'Select Sector', df_custom.Sector.unique().tolist() )
#st.set_page_config(page_title="Investrecipes",layout='wide')
st.set_page_config( page_title="momentum lists", layout='wide')
st.title ('momentum lists')

tab1, tab2,tab3,tab4,tab5,tab6 = st.tabs([ " (etfs - technical analysis) ", "(stocks-technical analysis)", " (market - weekly performance) " , " (momentum views) ", " (fundamental explore) ", " ( technical explore ) " ])


with tab1:
    st.header("(ETFs)")
    
    col1, col2 = st.columns(2)

    with col1:
        draw_etf_fig()
    with col2 :
        draw_etf_image() 

    

    #st.caption ('Correlated')
    #df = pd.read_html ('https://investrecipes.s3.amazonaws.com/apps/stockcharts_as/stockworld_runbook_sources_ranking-agg.html')[0]
    #cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    #st.write(df[cols])
    #st.dataframe (use_container_width = True)

with tab2:
    st.header("(Stocks)")

    col1, col2 , col3 = st.columns(3)

    with col1:
        draw_technical_fig()

    with col3:
        draw_external_fig()
   
    with col2:
        draw_milestone_fig()

with tab3:
    st.header("(Weekly Performance)")
    
    #col1, col2 = st.columns(2)

    #with col1:
        #draw_market_sector()   
    
    draw_market_sector()

with tab4:
    st.header("(momentum views across stocks, industries, etfs )")
    l = ['silver cross', 'golden cross']
    sector_option = st.radio( "Industries , ETFs, Stocks by technical factor",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    col1, col2 , col3 = st.columns(3)

    with col1:
        st.write ('industries')
        if 'silver' in sector_option :
            col2_sector_option = "industries_20_50_sma"
        if 'gold' in sector_option :
            col2_sector_option = "industries_50_200_sma"
        df = pd.read_html ( take_string_give_url ( col2_sector_option ) )[0]
        cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
        cols = ['Symbol','Name']
        #st.caption ( ', '.join (df[cols].symbols.tolist()) )
        st.dataframe ( df[cols], height=1000)
        #st.write(df[cols])


    with col2:
        st.write ('etfs')
        if 'silver' in sector_option :
            col3_sector_option = "etfs_20_50_sma"
        if 'gold' in sector_option :
            col3_sector_option = "etfs_50_200_sma"
        df = pd.read_html ( take_string_give_url ( col3_sector_option ) )[0]
        cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
        cols = ['Symbol','Name']
        #st.caption ( ', '.join (df[cols].symbols.tolist()) )
        #st.write(df[cols])
        st.dataframe ( df[cols], height=1000)

    with col3 :
        st.write ('stocks')
        if 'silver' in sector_option :
            col1_sector_option = "stocks_20_50_sma"
        if 'gold' in sector_option :
            col1_sector_option = "stocks_50_200_sma"
        
        try :
            df = pd.read_html ( take_string_give_url ( col1_sector_option ) )[0]
            cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
            #st.caption ( ', '.join (df[cols].symbols.tolist()) )
            st.dataframe ( df[cols], height=1000)
        except Exception as e :
            st.write (e)
            st.write ('no data')

    #draw_momentum_figs()    

with tab5:
    st.header("(fundamental)")
    draw_f_fig()

with tab6:
    st.header("(technical)")
    draw_t_fig()

      


