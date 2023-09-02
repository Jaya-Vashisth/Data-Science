from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the ChromeDriver (replace 'path/to/chromedriver' with the actual path)
driver = webdriver.Chrome()

def scrape_reviews(url):
    reviews = []

    driver.get(url)

    try:
        while True:
            load_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Load More')]")
            if load_more_button.is_displayed():
                load_more_button.click()
                driver.implicitly_wait(5)
            else:
                break
    except:
        pass

    review_elements = driver.find_elements(By.CLASS_NAME, "text.show-more__control")
    for review_element in review_elements:
        reviews.append(review_element.text)

    return reviews

movie_url = "https://www.imdb.com/title/tt15398776/reviews"
reviews = scrape_reviews(movie_url)

for i, review in enumerate(reviews):
    print(f"Review {i+1}: {review}\n")

print(f"Total reviews scraped: {len(reviews)}")

driver.quit()
