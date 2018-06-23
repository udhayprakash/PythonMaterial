import json
import urllib2

f = urllib2.urlopen('http://api.wunderground.com/api/bef95257316a31ed/conditions/q/CA/San_Francisco.json')
json_string = f.read()
parsed_json = json.loads(json_string)

# pprint(parsed_json)
location = parsed_json['current_observation']['display_location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()
