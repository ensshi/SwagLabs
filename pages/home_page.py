from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def go_to(self):
         self.driver.get('https://www.saucedemo.com/')
         self.driver.maximize_window()

    def login(self, username, password):
        username_field_locator = (By.ID, 'user-name')
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, 'password')
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.ID, 'login-button')
        login_button.click()

    def get_login_logo(self):
        login_logo_locator = (By.CSS_SELECTOR, '.login_logo')
        wait_login_logo = self.wait.until(EC.visibility_of_element_located(login_logo_locator))
        login_logo = wait_login_logo.text
        return login_logo 

    