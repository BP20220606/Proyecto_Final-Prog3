from pages.base_page import BasePage
from data.locators import contactoLocators
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class Contacto(BasePage):
    def __init__(self, driver, wait):
        self.url = "file:///C:/Users/braul/OneDrive/Escritorio/ProgWebMaster/contacto.html"
        self.locator = contactoLocators
        super().__init__(driver, wait)

    def go_to_page(self):
        super().go_to_page(self.url)

    def enviar_mensaje_exitoso(self, nombre, email, mensaje):

        self.driver.find_element(*self.locator.ingresar_nombreContacto).send_keys(nombre)
        self.driver.find_element(*self.locator.ingresar_emailContacto).send_keys(email)
        self.driver.find_element(*self.locator.ingresar_mensajeContacto).send_keys(mensaje)
        self.driver.find_element(*self.locator.boton_enviarMensaje).click()

        self.driver.save_screenshot("results/mensaje_exito.png")

    def enviar_mensaje_fallido(self, nombre, email, mensaje):
        self.driver.find_element(*self.locator.boton_enviarMensaje).click()

        self.driver.save_screenshot("results/mensaje_fallido.png")