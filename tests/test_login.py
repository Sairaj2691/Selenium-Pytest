from selenium.webdriver.common.by import By
import pytest


@pytest.mark.smoke
def test_dashboard_visible(login):
    driver = login
    header = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
    assert header.is_displayed()