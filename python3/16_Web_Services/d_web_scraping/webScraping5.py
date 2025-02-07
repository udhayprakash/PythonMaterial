"""
Purpose: scraping
"""
from bs4 import BeautifulSoup
from security import safe_requests

res = safe_requests.get("https://www.whoishostingthis.com/tools/user-agent/", timeout=60)
soup = BeautifulSoup(res.text, "lxml")
print(soup.prettify())
