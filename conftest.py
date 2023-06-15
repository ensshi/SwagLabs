import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture
def driver():
    #setup
    service = Service(executable_path=ChromeDriverManager().install()) 
    driver = webdriver.Chrome(service=service)
    yield driver
    #teardown
    time.sleep(5)
    driver.quit() 