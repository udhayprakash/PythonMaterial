import csv

from selenium import webdriver
from selenium.webdriver.common.by import By


def generate_dummy_data():
    # create a list of country names
    countries = [
        "USA",
        "Canada",
        "India",
        "Japan",
        "Australia",
        "China",
        "Germany",
        "France",
        "Brazil",
        "Mexico",
    ]

    # create a list of dummy data for each record
    data = []
    for i in range(10):
        record = {
            "name": f"John Doe {i}",
            "email": f"johndoe{i}@example.com",
            "country": countries[i],
        }
        data.append(record)

    # write the data to a CSV file
    with open("dummy_data.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "country"])
        writer.writeheader()
        writer.writerows(data)


def do_petition():
    # create a webdriver instance
    driver = webdriver.Chrome()

    # navigate to the form page
    driver.get(
        "https://petitions.eko.org/petitions/appointment-of-tspsc-chairmen-post-with-an-experienced-sincere-jntuh-professor"
    )

    # fill the form with the data from the CSV file
    with open("dummy_data.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # find the form fields by their names and fill them with the data from the CSV file
            first_name_field = driver.find_element(By.NAME, "signature[first_name]")
            first_name_field.send_keys(row["name"])

            last_name_field = driver.find_element(By.NAME, "signature[last_name]")
            last_name_field.send_keys(row["name"])

            email_field = driver.find_element(By.NAME, "signature[email]")
            email_field.send_keys(row["email"])

            country_field = driver.find_element(By.NAME, "country")
            country_field.send_keys(row["country"])

            # submit the form
            submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
            submit_button.click()

            # navigate back to the form page for the next record
            driver.get(
                "https://petitions.eko.org/petitions/appointment-of-tspsc-chairmen-post-with-an-experienced-sincere-jntuh-professor"
            )

    # close the browser window
    driver.quit()


if __name__ == "__main__":
    generate_dummy_data()
    do_petition()
