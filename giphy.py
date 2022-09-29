# import requests
# import pprint
#
# API_KEY = "JSDgBpAimyWPkDQGiBZq9yfCtWJSry5w"
# SEARCH_ENDPOINT = "https://api.giphy.com/v1/gifs/search"
#
# params = {
#     "api_key": API_KEY,
#     "q": "motivation",
#     "rating": "g",
#     "lang": "eng",
#     "limit": 1
# }
#
# response = requests.get(SEARCH_ENDPOINT, params=params)
# response.raise_for_status()
# pprint.pprint(response.json()["data"][0]["images"])
