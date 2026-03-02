import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage   # ✅ works now


@pytest.fixture
def driver():
    print("\nLaunching browser...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    print("Closing browser...")
    driver.quit()


# POSITIVE TEST
def test_valid_login(driver):
    print("\nTEST: Valid Login")

    login_page = LoginPage(driver)
    login_page.load()

    login_page.login("standard_user", "secret_sauce")

    if "inventory.html" in driver.current_url:
        print("PASS: Login successful")
    else:
        print("FAIL: Login failed")

    assert "inventory.html" in driver.current_url
