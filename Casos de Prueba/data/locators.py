from selenium.webdriver.common.by import By

class loginLocators:
    email_input = (By.ID, "emailLogin")
    password_input = (By.ID, "passwordLogin")
    login_button = (By.XPATH, "//button[contains(text(), 'Iniciar Sesión')]")

class registroLocators:
    escibir_nombreR = (By.XPATH, "//*[@id='nombre']")
    escibir_apellidoR = (By.XPATH, "//*[@id='apellido']")
    escribir_edadR = (By.XPATH, "//*[@id='edad']")
    select_genero = (By.XPATH, "//*[@id='genero']")
    select_ocupacion = (By.XPATH, "//*[@id='ocupacion']")
    escibir_emailR = (By.XPATH, "//*[@id='emailRegistro']")
    escribir_contraseñaR = (By.XPATH, "//*[@id='passwordRegistro']")
    escribir_confirmar_contraseñaR = (By.XPATH, "//*[@id='confirmPassword']")
    boton_registro = (By.XPATH, "//button[contains(text(), 'Registrar')]")
    
class nosotrosLocators:
    link_contactos = (By.XPATH, "//a[contains(text(),'Contacto')]")


class contactoLocators:
    ingresar_nombreContacto = (By.ID, "nombreContacto")
    ingresar_emailContacto = (By.ID, "emailContacto")
    ingresar_mensajeContacto = (By.ID, "mensajeContacto")    
    boton_enviarMensaje = (By.XPATH, "//button[contains(text(), 'Enviar Mensaje')]")




