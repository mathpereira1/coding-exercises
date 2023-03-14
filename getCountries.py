import requests

def getCountries(s, p):
    count = 0
    url = "https://jsonmock.hackerrank.com/api/countries/search?name=" + s
    response = requests.get(url)
    data = json.loads(response.text)
    countries = data["data"]
    for country in countries:
        if country["population"] > p:
            count += 1
    return count