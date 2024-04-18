from pages.base_page import BasePage
from data.locators import loginLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class Login(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/braul/OneDrive/Escritorio/ProgWebMaster/login.html"
        self.locator = loginLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)


    def iniciar_sesion_exitoso(self, email, password):
        self.driver.find_element(*self.locator.email_input).send_keys(email)
        self.driver.find_element(*self.locator.password_input).send_keys(password)
        self.driver.find_element(*self.locator.login_button).click()

        time.sleep(2)
       

        self.driver.save_screenshot("results/login_exitoso.png")

    def iniciar_sesion_fallido(self, email, password):
        self.driver.find_element(*self.locator.email_input).send_keys(email)
        self.driver.find_element(*self.locator.password_input).send_keys(password)
        self.driver.find_element(*self.locator.login_button).click()

        time.sleep(2)

        self.driver.save_screenshot("results/login_fallido.png")