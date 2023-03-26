from json import dump
from time import sleep

from selenium import webdriver


def calculate_stop_reviews(total_reviews):
    stop_loop_for = int(
        int(total_reviews.replace(".", "").replace("(", "").replace(")", "")) / 5
    )
    if stop_loop_for % 2 == 0:
        stop_loop_for += 1
    else:
        stop_loop_for += 2
    return stop_loop_for


def get_all_reviews(hotel, language):
    review_total_pages = []
    page = webdriver.Chrome("./chromedriver.exe")
    page.get(hotel)
    sleep(2)
    # Click in the List of all Language
    page.execute_script(
        "document.querySelector('.hotels-review-list-parts-LanguageFilter__taLnk--3iBfk').click();"
    )
    sleep(2)
    # Click in the Language selected
    page.execute_script(f"document.querySelector('input[value={language}]').click();")
    sleep(2)

    # Get data
    language_id = page.find_element_by_xpath(
        f'//input[@value="{language}"]'
    ).get_attribute("id")
    hotel_name = page.find_element_by_xpath('//h1[@id="HEADING"]').text
    total_reviews = page.find_element_by_xpath(
        f'//label[@for="{language_id}"]/span[@class="hotels-review-list-parts-LanguageFilter__paren_count--EHwQo"]'
    ).text
    hotel_rating = page.find_element_by_class_name(
        "hotels-hotel-review-about-with-photos-Reviews__overallRating--vElGA"
    ).text
    stop_loop_for = calculate_stop_reviews(total_reviews)

    url_remove_http = hotel.replace("https://www.tripadvisor.co", "")
    url_split = url_remove_http.split("-Reviews-")

    # Extrac reviews for every Page
    for pagination in range(1, 3):
        print(f"Reviews Page: {pagination}")
        if pagination == 1:
            # Click in "Read More"
            page.execute_script(
                "document.querySelector('.hotels-review-list-parts-ExpandableReview__cta--3U9OU').click();"
            )
            sleep(2)
        else:
            sleep(2)
            click = (pagination - 1) * 5
            href = url_split[0] + "-Reviews-or" + str(click) + "-" + url_split[1]
            # Click in the next Page
            page.execute_script(
                f"""document.querySelector('a[href="{href}"]').click();"""
            )
            sleep(2)
            # Click in "Read More"
            page.execute_script(
                "document.querySelector('.hotels-review-list-parts-ExpandableReview__cta--3U9OU').click();"
            )
            sleep(2)

        # Get all Reviews information
        reviews = page.find_elements_by_xpath(
            '//div[@class=""]/div/div[@class="hotels-hotel-review-community-content-Card__ui_card--3kTH_ hotels-hotel-review-community-content-Card__card--1MJgB hotels-hotel-review-community-content-Card__section--28b0a"]'
        )
        reviews_count = 0
        for review in reviews:
            review_dict = {
                "review_text": review.find_elements_by_xpath(
                    '//q[@class="hotels-review-list-parts-ExpandableReview__reviewText--3oMkH"]'
                )[reviews_count].text,
                "review_date": review.find_elements_by_xpath(
                    '//div[@class="hotels-review-list-parts-EventDate__event_date--CRXs4"]'
                )[reviews_count].text,
                "review_header": review.find_elements_by_xpath(
                    '//div[@class="hotels-review-list-parts-ReviewTitle__reviewTitle--2Fauz"]'
                )[reviews_count].text,
                "review_rating": "XXXXX",
                "review_author": review.find_elements_by_xpath(
                    '//a[@class="ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC"]'
                )[reviews_count].text,
            }
            review_total_pages.append(review_dict)
            reviews_count += 1
    page.quit()
    data = {
        "hotel_name": hotel_name,
        "total_reviews": total_reviews,
        "ratings": hotel_rating,
        "language": language,
        "reviews": review_total_pages,
    }
    return data


def core():
    hotels = [
        "https://www.tripadvisor.co/Hotel_Review-g150807-d152886-Reviews-The_Ritz_Carlton_Cancun-Cancun_Yucatan_Peninsula.html"
    ]
    language = "en"
    for hotel in hotels:
        print(f"IN PROCESS FOR: {hotel}")
        response = get_all_reviews(hotel, language)
        file = open("hotel_reviews.json", "w", encoding="utf8")
        dump(response, file, indent=4, ensure_ascii=False)
        file.close()


if __name__ == "__main__":
    core()
