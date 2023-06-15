from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)    

    def is_login_button_invisible(self):
        login_button = (By.ID, 'login-button')
        self.wait.until(EC.invisibility_of_element_located(login_button))

    def get_products_title(self):
        products_title_locator = (By.XPATH, './/span[text()="Products"]')
        wait_products_title = self.wait.until(EC.visibility_of_element_located(products_title_locator))

        products_title = wait_products_title.text
        return products_title

    def add_to_cart(self, id):
        add_to_cart = self.driver.find_element(By.ID, id)
        add_to_cart.click()

    def click_cart_link(self):
        cart_link_locator = self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
        cart_link_locator.click()

 

