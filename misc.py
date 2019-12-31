# -----------------------------------------------------------
# requests exercises in python
# -----------------------------------------------------------   

# Source: Jessica
#
# try to make an http call with Python and print out the results and the status code
# 
# GIPHY
#
# my from giphy: vXmA7LE7e20rK2zvMu9QB2BVUNEZWYK0
# public key: dc6zaTOxFJmzC

import requests

# url = "https://giphy.p.rapidapi.com/v1/gifs/search"

# querystring = {
#     "q":"hit the whoa",
#     "api_key":"vXmA7LE7e20rK2zvMu9QB2BVUNEZWYK0",
#     "limit":3
# }

# headers = {
#     'x-rapidapi-host': "giphy.p.rapidapi.com",
#     'x-rapidapi-key': "e4311cc350msh68c8124152cf9d1p18c0b5jsnf544303cb194"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.headers)

# status = response.status_code
# # print(status)

# data = response.json()

# titles = [i['title'] for i in data['data']]
# # print(titles)

# MediaWiki
url = "http://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "list": "search",
    "srsearch": "Harold",
    "format": "json"
}

response = requests.request("GET", url, params=params)

data = response.json()

print(data['query']['searchinfo'])

# snippets = [print(snippet['snippet']) for snippet in data['query']['search']]