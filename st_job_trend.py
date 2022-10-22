#plotly_chart.py
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import datetime
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
        'koyfin_etf' : 'https://investrecipes.s3.amazonaws.com/industry/fundamental/comparisoncharts/etfworld_industry_all_koyfin-list.png',
        'macro_market_charts': 'https://investrecipes.s3.amazonaws.com/market/fundamental/comparisoncharts/etfworld_sector_all_market-finviz-charts.png',    
        'sector_market_charts': 'https://investrecipes.s3.amazonaws.com/sector/fundamental/comparisoncharts/etfworld_sector_all_finviz-charts.png'

    }
    return url_dict[option]

def draw_milestone_fig():

    l = ['52wkhigh', '60plusrsi','golden_cross']
    sector_option = st.radio( "Stocks hitting technical milestones",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    st.caption ( ', '.join (df[cols].symbols.tolist()) )
    st.write(df[cols])
    st.markdown("""---""") 
 
    st.caption ('charts')
    st.image (  take_string_give_url ( sector_option ).split('.csv')[0] + '-charts.png' )
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


    l = ['unusual_volume', 'price_up_and_volume_up']
    sector_option = st.radio( "Stocks with eechnical tailwinds",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = [x for x in df.columns.tolist() if 'Unnamed' not in x]
    st.caption ( ', '.join (df[cols].symbols.tolist()) )
    st.write(df[cols])

def draw_etf_fig() :
    l = ['etf_in_momentum', 'etf_etfs_rsi','etf_in_rsi']
    sector_option = st.radio( "Technical",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    df = pd.read_html ( take_string_give_url ( sector_option ) )[0]
    cols = ['Symbol','Name']
    st.write(df[cols])
    st.image (take_string_give_url ( sector_option ).split('.html')[0]+'-rrg.png')

def draw_etf_image() :
    l = ['koyfin_etf']
    sector_option = st.radio( "Performance",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.image ( take_string_give_url ( sector_option ) )

def draw_market_sector() :

    l = ['macro_market_charts','sector_market_charts']
    sectors = ['xlp','xlv','xlre','xlf','xlc','xle','xlre','xlb','xli','xlk','xly']
    l.extend(['xlp','xlv','xlre','xlf','xlc','xle','xlre','xlb','xli','xlk','xly'])
    sector_option = st.radio( "Market Performance",  l , key = 'Market Performance' )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    
    if 'x' not in sector_option :

        st.image ( take_string_give_url ( sector_option ) )
        st.image ( take_string_give_url ( sector_option ).split('-charts')[0]+'-list.png' )

    else :
        adf = pd.read_html('https://investrecipes.s3.amazonaws.com/all-files.html')[0]
        xlydf = adf [ (adf.key.str.contains('.png') ) & (adf.key.str.contains('industry_'+sector_option)) ]
        images = xlydf.key.tolist()
        urls = [ 'https://investrecipes.s3.amazonaws.com/'+ x for x in images]
        captions = [x.split('/')[-1].split('-finviz')[0] for x in urls]
        st.image(urls,width=600,caption=captions)
         
def draw_momentum_figs():
    l = ['industries_rrg']
    sector_option = st.radio( "industries_rrg",  l  )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
   
    adf = pd.read_html('https://investrecipes.s3.amazonaws.com/all-files.html')[0]
    images = [ x for x in adf.key.tolist() if 'industries_rrg' in x]
    urls = [ 'https://investrecipes.s3.amazonaws.com/'+ x for x in images]
    captions = [x.split('/')[-1].split('-finviz')[0] for x in urls]
    st.image(urls,width=600,caption=captions)
 

def make_clickable(val):
    return '<a href="{}">{}</a>'.format(val,val)

## main



#df_custom = kdf.copy()
#l = df_custom.Sector.unique().tolist()
#l.append('All')

#l = ['52wkhigh', '60plusrsi']
#sector_option = st.radio( "Technical",  l  )
#st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#sector_option =  st.selectbox ( 'Select Sector', df_custom.Sector.unique().tolist() )
st.set_page_config(page_title="JobsMills",layout='wide')


with st.sidebar:
    add_radio = st.radio(
        "Role",
        ("Executive", "Manager", "Individual" )
    )



pdf = pd.read_csv('https://worldopen.s3.amazonaws.com/product_management.csv')

joindf=pdf.copy()

dcols = ['Post_Date', 'Job_Title', 'Company_Name','Company_Location', 'Job_Link','Company_Description']

joindf.Post_Date = pd.to_datetime(joindf.Post_Date)
joindf = joindf[joindf.Post_Date > datetime.datetime.now() - pd.to_timedelta("30day")]

joindf=joindf[joindf.Company_Name.str.len() > 2]
joindf=joindf[joindf.Job_Title.str.len() > 2]


#print (joindf.columns)

joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace("set()", "NA", regex=True)
joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace("}", "", regex=True)
joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace("{", "", regex=True)
joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace("(", "", regex=True)
joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace(")", "", regex=True)
joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace("\\", "", regex=True)
joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace("'.", "'", regex=True)



joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace("xa0", "", regex=True)
joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace("\u200e", "", regex=True)

joindf['Company_Description'] = joindf['Company_Description'].astype(str).str.replace("www.owler.com", "", regex=True)
joindf=joindf.sort_values('Post_Date' , ascending=False).drop_duplicates(subset=['Job_Title', 'Company_Name'], keep='last')


tlist =[' vp ','officer', 'president'] 
must_term = 'product manag'
print (must_term)

joindf=joindf[joindf.Job_Title.str.lower().str.contains (must_term) ]

joindfd=joindf[joindf.Job_Title.str.lower().str.contains('|'.join(tlist) , na=False) ]


l = joindfd.Company_Name.tolist()

sector_option = st.radio( "Hiring Companies",  l  )
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

joindf = joindfd [ joindf.Company_Name.str.contains (sector_option) ]   



joindf.style.format(make_clickable)
 
st.markdown ( joindf[dcols].to_html(escape=False , render_links=True  ), unsafe_allow_html=True )

st.write(add_radio)
