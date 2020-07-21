import configparser
import json
import sys
import urllib.error
import urllib.request

config = configparser.ConfigParser()
config.read('weather.ini')

api_key = config.get('prod', 'APIKEY')
URL = 'http://api.wunderground.com/api/{apikey}/conditions/q/CA/San_Francisco.json'.format(apikey=api_key)
print('URL=', URL)

try:
    f = urllib.request.urlopen(URL)
except urllib.error.HTTPError as ex:
    print(ex)
    sys.exit(1)

json_string = f.read()
parsed_json = json.loads(json_string)

# pprint(parsed_json)
with open('weather.json', 'wb') as g:
    g.write(json_string)
    g.close()

location = parsed_json['current_observation']['display_location']['city']
temperature_string = parsed_json['current_observation']['temperature_string']
print("Current temperature in %s is: %s" % (location, temperature_string))
f.close()
