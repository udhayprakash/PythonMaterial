import urllib2
import urlparse

resp = urllib2.urlopen("https://www.youtube.com/watch?v=gvVHSndpkEg")
data = resp.read()
info = urlparse.parse_qs(data)
title = info['title'][0]
fname = title+".mp4"
stream_map = infor["url_encoded_fmt_stream_map"][0]
v_info = stream_map.split(",")
for video in v_info:
    item = urlparse.parse_qs(video)
    print item["quality"][0]
    print item["type"][0]
    print item["url"][0]
