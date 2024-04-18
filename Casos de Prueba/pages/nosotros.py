from pages.base_page import BasePage
from data.locators import nosotrosLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Nosotros(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/braul/OneDrive/Escritorio/ProgWebMaster/nosotros.html"
        self.locator = nosotrosLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)
        self.driver.save_screenshot("results/nosotros.png")


    def acceder_contacto(self):
        self.driver.find_element(*self.locator.link_contactos).click()
        self.driver.save_screenshot("results/nosotros_contacto.png")
