import duckduckgo 
import sys

# print dir(duckduckgo)

try:
    response = duckduckgo.query('DuckDuckGo')
except Exception as ex:
    print "request failed with error:", repr(ex) 
    sys.exit(1)

print response
print dir(response)

print 'API version   :', response.api_version
print 'response.type :', response.type
print 'No. of results:', len(response.results)

for each_result in response.results:
    print 'each_result.url :', each_result.url
    print 'each_result.text:', each_result.text
    print 'each_result.html:', each_result.html
    print 'each_result.icon:', each_result.icon
    print dir(each_result)