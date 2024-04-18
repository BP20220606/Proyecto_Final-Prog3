from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import UnexpectedAlertPresentException



# Crea una instancia del navegador web
driver = webdriver.Chrome()

# Abre la página de registro
url = "file:///C:/Users/braul/OneDrive/Escritorio/ProgWebMaster/registro.html"
driver.get(url)

# Introduce datos para un registro fallido
driver.find_element("id", "nombre").send_keys("")
driver.find_element("id", "apellido").send_keys("")
driver.find_element("id", "edad").send_keys("25")
Select(driver.find_element("id", "genero")).select_by_value("")
Select(driver.find_element("id", "ocupacion")).select_by_value("")
driver.find_element("id", "emailRegistro").send_keys("correo@dominio.com")
driver.find_element("id", "passwordRegistro").send_keys("contraseña")
driver.find_element("id", "confirmPassword").send_keys("contraseña")
driver.find_element("xpath", "//button[contains(text(), 'Registrar')]").click()

try:
    # Espera un momento para que la alerta se muestre
    time.sleep(2)
    # Acepta la alerta
    # Toma una captura de pantalla
    driver.save_screenshot("results/registro_fallido.png")
    driver.switch_to.alert.accept()
except UnexpectedAlertPresentException:
    # Si se produce la excepción de alerta inesperada, simplemente continúa
    pass


