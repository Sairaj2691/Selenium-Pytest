import pdb

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_revise_take_three():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    driver.get("https://www.redbus.in")
    find = driver.find_element(By.XPATH, "//input[@id='srcinput']")
    find.send_keys("Mumbai")
    driver.implicitly_wait(10)
    all_locations = driver.find_elements(By.XPATH, "//div[@aria-label='Search suggestions list']//div[contains(translate(normalize-space(.),'MUMBAI','mumbai'),'mumbai') ]/parent::div//div[@role='heading']")
    print("outside locations")
    for item in all_locations:
        # print("inside locations")
        location = item.text
        print(location)
    #pdb.set_trace()

