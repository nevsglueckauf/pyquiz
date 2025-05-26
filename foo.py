import pyquiz.api

api = pyquiz.api.OTDBApi()

response = api.get_session_token()
response = 23
san_uri = api.get_foo()

print(type(api.http_response), api.dta, api.session_token, san_uri)

