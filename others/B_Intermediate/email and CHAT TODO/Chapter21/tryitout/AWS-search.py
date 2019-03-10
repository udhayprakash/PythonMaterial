import urllib
author = "Joyce, James"
subscriptionID = [your subscription id]
url = "http://xml.amazon.com/onca/xml3?f=xml&t=webservices-20&dev-t=%s&type=lite&mode=books&AuthorSearch=%s" % (subscriptionID, urllib.quote(author))
print urllib.urlopen(url).read()
