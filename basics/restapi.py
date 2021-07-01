import requests
import json

# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
base_url = "https://api.datamuse.com/words"
d = {"rel_rhy": "funny"}
page = requests.get(base_url, params=d)
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object or x = json.loads(page.text)
# x = json.loads(page.text)
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x[:4], indent=2)) # pretty print the results