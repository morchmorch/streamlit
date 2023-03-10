#from appsmills.streamlit_apps 
from helpers import openai_helpers
import streamlit as st
import numpy as np
from random import randrange
import openai,boto3,urllib, requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image
import re
## 

at = """ these are the attack techniques for business email compromise - - Exploiting Trusted Relationships
    - To urge victims to take quick action on email requests, attackers make a concerted effort to exploit an existing trusted relationship. Exploitation can take many forms, such as a vendor requesting invoice payments, an executive requesting iTunes gift cards, or an [employee sharing new payroll direct deposit details](https://www.armorblox.com/blog/payroll-fraud-when-direct-deposits-go-rogue).
- Replicating Common Workflows
    - An organization and its employees execute an endless number of business workflows each day, many of which rely on automation, and many of which are conducted over email. The more times employees are exposed to these workflows, the quicker they execute tasks from muscle memory. BEC attacks [try to replicate these day-to-day workflows](https://www.armorblox.com/blog/security-as-social-engineering-phishing-campaigns-spoofing-locked-account-workflows) to get victims to act before they think.
- Compromised workflows include:
    - Emails requesting a password reset
    - Emails pretending to share files and spreadsheets
    - Emails from commonly used apps asking users to grant them access
- Suspicious Attachments
    - Suspicious attachments in email attacks are often associated with malware. However, attachments used in BEC attacks forego malware in exchange for fake invoices and other social engineering tactics that add to the conversation’s legitimacy. These attachments are lures designed to ensnare targets further.
- Socially Engineered Content and Subject Lines
    - BEC emails often rely on subject lines that convey urgency or familiarity and aim to induce quick action.
    - Common terms used in subject lines include:
        - Request
        - Overdue
        - Hello FirstName
        - Payments
        - Immediate Action
    - Email content often follows along the same vein of trickery, with manipulative language that pulls strings to make specific, seemingly innocent requests. Instead of using phishing links, BEC attackers use language as the payload.
- Leveraging Free Software
    - Attackers make use of freely available software to lend BEC scams an air of legitimacy and help emails sneak past security technologies that block known bad links and domains.
    - For example, attackers use SendGrid to create spoofed email addresses and Google Sites to stand up phishing pages.
    - [Google Forms](https://www.armorblox.com/blog/ok-google-build-me-a-phishing-campaign)
"""

bc = """ these are the categories of business email compromise - - CEO Fraud
    - Attackers impersonate the CEO or executive of a company. As the CEO, they request that an employee within the accounting or finance department transfer funds to an attacker-controlled account.
- Lawyer Impersonation
    - Attackers pose as a lawyer or legal representative, often over the phone or email. These attacks’ common targets are lower-level employees who may not have the knowledge or experience to question the validity of an urgent legal request.
- Data Theft
    - Data theft attacks typically target HR personnel to obtain personal information about a company’s CEO or other high-ranking executives. The attackers can then use the data in future attacks like CEO fraud.
- Email Account Compromise
    - In an [email account compromise](https://www.armorblox.com/solutions/email-account-compromise) attack, an employee’s email account is hacked and used to request payments from vendors. The money is then sent to attacker-controlled bank accounts.
- Vendor Email Compromise
    - Companies with foreign suppliers are common targets of [vendor email compromise](https://www.armorblox.com/blog/identity-theft-invoices-and-impersonation). Attackers pose as suppliers, request payment for a fake invoice, then transfer the money to a fraudulent account.
"""


def display_text () :

    button_name = "Is it legit email ? !! "
    response_while = "Right on it, it should be around 2-5 seconds ..."
    response_after = "Here you go ...  "


    email_txt = st.text_area("Paste the email body", value="", height=400 )
    tab_button=st.button(button_name , key = "be" +  "1")
    if tab_button:
        
        r = openai_helpers.response( bc )
        r = openai_helpers.response( at )

        prompt = "determine if the below email is a business email compromise,  tell me the reasons , categorize it and tell me the attack technique as well - "
        email_txt = prompt + email_txt
        openai_helpers.get_write_response (email_txt)

    

def streamlit_main (url) :


    button_name = "Draft it for me !! "
    response_while = "Right on it, it should be around 2-5 seconds ..."
    response_after = "Here you go ...  "


    #url = 'https://worldopen.s3.amazonaws.com/prompts_sales.csv'
    r = requests.get(url, allow_redirects=True)

    open('/tmp/df.csv', 'wb').write(r.content)

    df = pd.read_csv ('/tmp/df.csv', encoding = 'cp1252')

    role = df.job.unique().tolist()[0]

    st.header ( role.strip() )

    # tabs are the tasks
    tab_list = df.tasks.unique().tolist()

    tabs = [ str(x) for x in tab_list if x is not np.nan ]

    tabs = st.tabs ( tabs )  


    i=0
    for tab in tabs :

        with tab :
            tab_name = tab_list[i]
            #st.write (tab_name)
            df_d = df [ df.tasks == tab_name ]

            # these are the list of questions
            dropdowns = df [ df.tasks == tab_name ].dropdown.tolist()
            #st.write (dropdowns)
            openai_helpers.draw_prompt(dropdowns, tab_name, df_d)

            i = i + 1

#page_title = "Detect Business Email Compromise"
#st.set_page_config(page_title=page_title,layout='wide')
           
display_text()

    
