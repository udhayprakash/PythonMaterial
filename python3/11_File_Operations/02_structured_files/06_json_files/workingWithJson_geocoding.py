import urllib
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location: ")  # Hyderabad, IN
    if len(address) < 1:
        break

    url = serviceurl + urllib.urlencode({"sensor": "false", "address": address})

    print("Retrieving", url)
    uh = urllib.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted_address"]
    print(location)
    print
    "-" * 80
    choice = input("Do you want to retry: Y or N: ")
    if choice.lower() == "n":
        break
