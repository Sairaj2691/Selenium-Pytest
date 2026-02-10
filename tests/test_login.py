from selenium.webdriver.common.by import By
import pytest
import pdb


@pytest.mark.smoke
@pytest.mark.parametrize("login", [("admin", "admin123"), ("admin", "admin123")], indirect=True)
def test_dashboard_visible(login):
    driver = login
    # pdb.set_trace()
    #print(f'trying with username: {username} and password: {password}')
    header = driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
    assert header.is_displayed()