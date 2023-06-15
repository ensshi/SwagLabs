from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutOverviewPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)  

    def get_overview_title(self):
        overview_title_locator = (By.XPATH, './/span[text()="Checkout: Overview"]')
        wait_overview_title = self.wait.until(EC.visibility_of_element_located(overview_title_locator))
        overview_title = wait_overview_title.text
        return overview_title
    
    def get_item_names(self):
        items_locator = self.driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')
        item_names = [item.text for item in items_locator]
        return item_names
    
    def finish_button(self):
        finish_button_locator = self.driver.find_element(By.ID, 'finish')
        finish_button_locator.click()