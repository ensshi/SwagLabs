from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutCompletePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)  

    def get_complete_title(self):
        complete_title_locator = (By.XPATH, './/span[text()="Checkout: Complete!"]')
        wait_complete_title = self.wait.until(EC.visibility_of_element_located(complete_title_locator))
        complete_title = wait_complete_title.text
        return complete_title
    
    def menu_icon_click(self):
        menu_icon_locator = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        menu_icon_locator.click()

    def logout(self):
        logout_link_locator = (By.ID, 'logout_sidebar_link')
        wait_logout_link = self.wait.until(EC.element_to_be_clickable(logout_link_locator))
        wait_logout_link.click()