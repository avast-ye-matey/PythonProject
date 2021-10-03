# This project displays customer reviews for James Kraus while employed at Scheller's Fitness and Cycling.

# Import required packages
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Add options on chrome. These options allow selenium to do its work without opening the 
# browser window, thus speeding up the module.
chromeOptions = Options()
chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--disable-gpu")


# Locate elements by name
browser = webdriver.Chrome(options=chromeOptions)
browser.get("https://reviews.listen360.com/scheller-s-fitness-cycling-middletown-louisville")
time.sleep(1)

element = browser.find_element_by_tag_name("body")

# Scroll down on page to load older reviews on the infinite feed.
no_of_pagedowns = 10

while no_of_pagedowns:
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

# Find and print only the reviews that contain the name "James"
review_elements = browser.find_elements_by_xpath("//*[contains(text(), 'James')]")

for review in review_elements:
    print(review.text)