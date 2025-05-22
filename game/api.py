# Classes for HTTP access to Open Trivia DB
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16

import json
import requests


class Endpoints:
    USE_SESS_TOK_URI = "https://opentdb.com/api.php?amount=10&token={}" # URI for using a session token
    RETR_SESS_TKN_URI = "https://opentdb.com/api_token.php?command=request" # URI for retrieve a session token
    RST_SESS_TKN_URI = "https//opentdb.com/api_token.php?command=reset&token={}" # URI for reset a session token
    WITH_ENC_TYP_URI = "https://opentdb.com/api.php?amount=10&encode=url3986" # URI for api call with encode type
    CAT_LKU_URI = "https//opentdb.com/api_category.php" # URI for category lookup
    CAT_QST_CNT_LKU_URI = "https://opentdb.com/api_count.php?category={}" # URI for category question count lookup
    GLB_QUES_CNT_LKU_URI = "https://opentdb.com/api_count_global.php" # URI for global question count lookup
    RTV_AMNT_QST = "https://opentdb.com/api.php?amount={}"  # URI for Retrieving amount of questions


class OTDBApi:
    req: requests
    dta: dict
    main_uri: str = Endpoints.RTV_AMNT_QST
    response_code: int

    def __init__(self):
        pass

    def get_questions_raw(self, number: int = 10) -> dict:
        response = requests.get(self.main_uri.format(number))
        self.response_code = response.status_code
        self.dta = response.json()
        return self.dta["results"]
