#!/usr/bin/python
"""
Purpose: Parsing the robots.txt file

    Ref: http://www.robotstxt.org/orig.html
"""
import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt")
rp.read()

rrate = rp.request_rate("*")
rrate.requests  # 3
rrate.seconds  # 20
rp.crawl_delay("*")  # 6

rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")  # False
rp.can_fetch("*", "http://www.musi-cal.com/")  # True


# https://www.google.com/robots.txt
# https://www.w3.org/robots.txt
# https://www.data.gov/robots.txt
# https://www.crops.org/robots.txt
# https://www.yale.edu/robots.txt
# https://www.linkedin.com/robots.txt
# https://www.jobsdb.com/robots.txt
# https://www.facebook.com/robots.txt
# https://www.instagram.com/robots.txt
# https://www.glassdoor.com/robots.txt
