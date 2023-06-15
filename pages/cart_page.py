from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)    

    def is_products_title_invisible(self):
        products_title_locator = (By.XPATH, './/span[text()="Products"]')
        self.wait.until(EC.invisibility_of_element(products_title_locator))

    def get_your_cart_title(self):
        your_cart_title_locator = (By.XPATH, './/span[text()="Your Cart"]')
        wait_your_cart_title = self.wait.until(EC.visibility_of_element_located(your_cart_title_locator))
        your_cart_title = wait_your_cart_title.text
        return your_cart_title
    
    def get_item_names(self):
        items_locator = self.driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')
        item_names = [item.text for item in items_locator]
        return item_names
    
    def checkout(self):
        checkout_locator = self.driver.find_element(By.ID, 'checkout')
        checkout_locator.click()

