from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_driver = "/Applications/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_button_main = driver.find_element_by_id("cookie")
time_out = time.time() + 5
terminate = time.time() + 300
while True:
    cookie_button_main.click()
    prices = []
    names = []
    #Checking if 5 seconds is over
    if time.time() > time_out:
        #Getting all the values with the bold headings
        all_prices = driver.find_elements_by_css_selector("#store b")
        #Getting prices and names
        for item in all_prices:
            try:
                prices.append(int(item.text.split('-')[1].replace(",", "")))
                names.append((item.text.split('-')[0]).split()[0])
            except IndexError:
                pass
