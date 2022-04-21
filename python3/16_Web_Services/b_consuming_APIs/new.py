import urllib.request
import json

url = "https://jsonmock.hackerrank.com/api/countries/search?name="


def getCountries(s, p):
    pg = 1
    min_pop_countries = set()
    while True:
        url = f"https://jsonmock.hackerrank.com/api/countries/search?name={s}&page={pg}"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        for each_record in data["data"]:
            # from pprint import pprint; pprint(each_record)
            if each_record["population"] >= p:
                min_pop_countries.add(each_record["name"])
        del data["data"]
        print(data)
        if data["page"] == data["total_pages"]:
            break
        pg += 1
    return min_pop_countries


print(getCountries("in", 1000000))
