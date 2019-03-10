from selenium import webdriver
from time import sleep
#from scrapy.selector import Selector


# Opening the URL in Chrome
chromedriver = webdriver.Chrome(executable_path = '/Users/UserName/Downloads/chromedriver')
url = "https://www.olx.co.ke/ad/private-tutors-and-home-tuition-services-ID15PcCi.html"
chromedriver.get(url)

sleep(3)

# Clicking the "Show phone" button
show_phone = chromedriver.find_element_by_xpath('//*[@id="contact_methods"]')
show_phone.click()

sleep(3)

# Extracting the phone number
phone = chromedriver.find_element_by_xpath('//*[@class="contactbox-indent rel brkword"]/strong').text
print phone


# or using scrapying, comment the last two lines and uncomment these lines instead
#sel = Selector(text=chromedriver.page_source)
#phone = sel.xpath('//*[@class="contactbox-indent rel brkword"]/strong/text()').extract_first()
#print phone


# Closing the browser
chromedriver.quit()

