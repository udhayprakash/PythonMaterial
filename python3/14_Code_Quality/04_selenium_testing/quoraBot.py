# Check out pythonhowto.com for more code tutorials !!
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

email = ""  # Your Password Here
passy = ""  # Your Password Here
driver.get("http://quora.com")

soup = BeautifulSoup(driver.page_source, "lxml")
forms = soup.find_all(class_="form_column")

# Find Login Css Selectors Here
for x in forms:
    try:
        data = x.find("input")["name"]
        if data == "email":
            email_css = "#" + x.find("input")["id"]
        if data == "password":
            password_css = "#" + x.find("input")["id"]
    except:
        pass
    try:
        data = x.find("input")["value"]
        if data == "Login":
            login_css = "#" + x.find("input")["id"]
    except:
        pass

driver.find_element_by_css_selector(email_css).send_keys(email)
driver.find_element_by_css_selector(password_css).send_keys(passy)
time.sleep(2)
driver.find_element_by_css_selector(login_css).click()
time.sleep(2)
