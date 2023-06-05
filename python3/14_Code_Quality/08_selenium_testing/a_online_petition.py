from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# initialize the Chrome web driver
driver = webdriver.Chrome()

# navigate to the page
driver.get(
    "https://petitions.eko.org/petitions/appointment-of-tspsc-chairmen-post-with-an-experienced-sincere-jntuh-professor?source=whatsapp-share-button&utm_source=whatsapp&share=d648e21d-d36f-428c-b098-9a20b899122a"
)

# fill in the form fields with dummy data
name = driver.find_element_by_name("name")
name.send_keys("John Doe")

email = driver.find_element_by_name("email")
email.send_keys("johndoe@example.com")

city = driver.find_element_by_name("city")
city.send_keys("New York")

comment = driver.find_element_by_name("comment")
comment.send_keys("This is a dummy comment.")

# submit the form
submit = driver.find_element_by_name("submit")
submit.click()

# close the browser window
driver.close()
