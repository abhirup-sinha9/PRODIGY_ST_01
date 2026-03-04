import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "YOUR_BROWSERSTACK_USERNAME"
ACCESS_KEY = "YOUR_BROWSERSTACK_ACCESS_KEY"

BROWSERSTACK_URL = "https://{}:{}@hub-cloud.browserstack.com/wd/hub".format(ABHIRUP, ACCESS_KEY)

class SwagLabsTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()

        # BrowserStack capabilities
        options.set_capability("browserName", "Chrome")
        options.set_capability("browserVersion", "latest")

        options.set_capability("bstack:options", {
            "os": "Windows",
            "osVersion": "11",
            "projectName": "Swag Labs Cross Browser Testing",
            "buildName": "Build 1",
            "sessionName": "Login & Add To Cart Test"
        })

        self.driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            options=options
        )

        self.wait = WebDriverWait(self.driver, 15)

    def test_login_and_add_to_cart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com")

        print("Opening Swag Labs Website")

        # Wait and Login
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        print("Login Successful")

        # Wait until inventory page loads
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

        # Click Add to Cart
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_button.click()
        print("Clicked Add to Cart")

        # Verify cart badge updated
        cart_badge = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        self.assertEqual(cart_badge.text, "1")
        print("Cart Updated Successfully")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
