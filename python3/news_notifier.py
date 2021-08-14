# /usr/bin/python3
"""
Purpose: 
    Breaking News Notifications for every one minute
"""
import requests
from scrapy.selector import HtmlXPathSelector
import pynotify
from time import sleep


def sendmessage(title, message):
        pynotify.init("Test")
        notice = pynotify.Notification(title, message)
        notice.show()
        return
url = "http://www.thehindu.com/"
while True:
        r = requests.get(url)
        while r.status_code is not 200:
                        r = requests.get(url)

        response = r.text
        xxs = HtmlXPathSelector(text=response)
        news = '\n'.join(xxs.select('//div[@class="breakingNews_list"]//h3/a/text()').extract()[:6])
        sendmessage("Breaking News", news)
        sleep(10) 
