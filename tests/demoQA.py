import pytest
from selenium import webdriver
import pdb
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class TestDemoQA:
    @pytest.mark.demoqa
    def test_demoqa(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.get("https://demoqa.com/")
        driver.maximize_window()
        #pdb.set_trace()
        element=driver.find_element(By.XPATH, "(//div[contains(@class,'avatar')]//*[name()='svg'])[1]")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        form=driver.find_element(By.XPATH, "//div[contains(text(),'Forms')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", form)
        form.click()
        practfor=driver.find_element(By.XPATH, "//span[@class='text' and contains(text(),'Practice Form')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", practfor)
        practfor.click()
        pdb.set_trace()
        firstname=driver.find_element(By.ID, "//input[@placeholder='First Name']")
        firstname.send_keys("kapil")
        lastname = driver.find_element(By.ID, "//input[@placeholder='Last Name']")
        lastname.send_keys("Sharma")

        Email = driver.find_element(By.ID, "//input[@id='userEmail']")
        Email.send_keys("kapil.sharma@gmail.com")
        gender = driver.find_element(By.ID, "//input[@name='gender' and @value='Male' ]")
        gender.click()
        mobile=driver.find_element(By.ID, "//input[@id='userNumber']")
        mobile.send_keys("9876543210")
        date=driver.find_element(By.ID, "//input[@id='dateOfBirthInput']")
        date.send_keys("10 Feb 2026")
        tickallcheckbox=driver.find_elements(By.XPATH, "//label[@id='hobbies-checkbox-1-label']")
        for checkbox in tickallcheckbox:
            checkbox.click()
        address=driver.find_element(By.ID, "//textarea[@placeholder='Current Address']")
        address.send_keys("Noida, Uttar Pradesh")
        state=driver.find_element(By.ID, "//div[@id='state']//div[contains(@class,'placeholder')]")
        state.click()






