# Classes for HTTP access to Open Trivia DB
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-26

import json
import requests
import api
import pandas as pd

foo = api.Endpoints.GLB_QUES_CNT_LKU_URI #= "https://opentdb.com/api_count_global.php" # URI for global question count lookup


class Scrapy:
    lst_http_req_uri:str = None # last request URI
    lst_http_resp:requests.models.Response = None # last response object instance
    dta:dict = None
    df:pd.DataFrame = None
    max_amt:int  = 50
    tok: str = None
    
    def __init__(self, tok:str=None):
        self.tok = tok
    
    
    def get(self, uri, root=None):
        if self.tok is not None:
            uri += f'&token={self.tok}'
        self.lst_http_req_uri = uri
        self.lst_http_resp = requests.get(uri)
        
        if self.lst_http_resp.status_code == requests.codes.ok:
            self.dta = self.lst_http_resp.json()
            self.df = pd.DataFrame(data=self.dta[root])
        else: 
            raise requests.RequestException('Error ' + str(self.lst_http_resp.status_code))
        
    def get_questions(self, amt:int = 5):
        if amt > self.max_amt:
            amt = self.max_amt
        self.get(api.Endpoints.RTV_AMNT_QST.format(amt), 'results')
    
    def meta(self):
        self.get(api.Endpoints.GLB_QUES_CNT_LKU_URI)
        return self.dta["overall"]["total_num_of_questions"]
    
    def dry_run(self):
        amt = self.meta()
        print(f"Wir haben {amt} Quizfragen, bei {self.max_amt} / Request sind das {amt/self.max_amt} Requests")
        

dta = json.load(open('../data/new.json'))['results']

df_0 = pd.DataFrame(dta)
#print(df_0)

#exit()

        
reader = api.OTDBApi()
tok = reader.get_session_token()


scrapeMe = Scrapy(tok=tok)
scrapeMe.get_questions(5)
print(scrapeMe.lst_http_resp.text)
exit()




df = scrapeMe.df
print(df.head(), df_0.head())


#
#scrapeMe.get_questions(5)
#df2 = scrapeMe.df
#print(df2)

df.merge(df_0)
df.to_csv('foo_newest.csv')


# df.to_csv('foo.csv')

#print(df, len(df))






print(scrapeMe.lst_http_req_uri)