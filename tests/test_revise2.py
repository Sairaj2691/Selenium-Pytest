import pytest
import pdb
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class WEBPAGE_ACTIVITIES():
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.booking.com')

    def find_and_perform(self, xpath, operation, keys=""):
        element = self.driver.find_element(By.XPATH, xpath)
        if operation == "click":
            element.click()
        elif operation == "send_keys":
            element.send_keys(keys)
        else:
            print(f"{operation} invalid operation sent")


    @pytest.mark.regression
    def test_website_launch(self):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


        # time.sleep(10)
        # pdb.set_trace()
        # close_popup = driver.find_element(By.XPATH, '//button[@aria-label="Dismiss sign-in info."]')
        # close_popup.click()
        # find_and_perform
        self.find_and_perform('//button[@aria-label="Dismiss sign-in info."]', "click")


task = WEBPAGE_ACTIVITIES()


task.test_website_launch()
