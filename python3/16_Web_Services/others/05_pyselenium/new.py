import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(
    # executable_path=r"C:\Users\User\Downloads\chromedriver.exe",
    options=options
)

url = "https://m.aiscore.com/basketball/20210610"
driver.get(url)
# Wait till the webpage is loaded
time.sleep(2)

# wait for 1sec after scrolling
scroll_wait = 1

# Gets the screen height
screen_height = driver.execute_script("return window.screen.height;")
driver.implicitly_wait(60)

# Number of scrolls. Initially 1
ScrollNumber = 1

# Set to store all the match links
ans = set()

while True:
    # Scrolling one screen at a time until
    driver.execute_script(f"window.scrollTo(0, {screen_height * ScrollNumber})")
    ScrollNumber += 1

    # Wait for some time after scroll
    time.sleep(scroll_wait)

    # Updating the scroll_height after each scroll
    scroll_height = driver.execute_script("return document.body.scrollHeight;")

    # Fetching the data that we need - Links to Matches
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for j in soup.select(".w100 .flex a"):
        if j["href"] not in ans:
            ans.add(j["href"])
    # Break when the height we need to scroll to is larger than the scroll height
    if (screen_height) * ScrollNumber > scroll_height:
        break


print(f"Links found: {len(ans)}")
