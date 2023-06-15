from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutInformationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)    

    def get_checkout_title(self):
        checkout_title_locator = (By.XPATH, './/span[text()="Checkout: Your Information"]')
        wait_checkout_title = self.wait.until(EC.visibility_of_element_located(checkout_title_locator))
        checkout_title = wait_checkout_title.text
        return checkout_title
    
    def form_fill(self, first_name, last_name, zip_code):
        first_name_field = (By.XPATH, '//input[@data-test="firstName"]')
        wait_first_name_field = self.wait.until(EC.element_to_be_clickable(first_name_field))
        wait_first_name_field.click()
        wait_first_name_field.clear()
        wait_first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.XPATH, '//input[@id="last-name"]')
        last_name_field.click()
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        zip_code_field = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]')
        zip_code_field.click()
        zip_code_field.clear()
        zip_code_field.send_keys(zip_code)

    def continue_button(self):
        continue_button = self.driver.find_element(By.XPATH, '//input[@id="continue"]')
        continue_button.click()