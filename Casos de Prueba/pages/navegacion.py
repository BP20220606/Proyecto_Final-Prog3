import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMenuNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_menu_navigation(self):
        # Páginas disponibles en el menú
        pages = ["index.html", "html.html", "css.html", "javascript.html", "login.html", "registro.html", "contacto.html", "nosotros.html"]

        # Iterar sobre cada página en el menú
        for page in pages:
            # Obtener la URL completa de la página actual
            page_url = f"file:///C:/Users/braul/OneDrive/Escritorio/ProgWebMaster/{page}"

            # Navegar a la página
            self.driver.get(page_url)

            # Esperar a que se cargue la página
            WebDriverWait(self.driver, 10).until(EC.url_to_be(page_url))

            # Verificar que la URL actual sea igual a la URL de la página
            self.assertEqual(self.driver.current_url, page_url)

            screenshot_name = f"results/{page.replace('.html', '')}.png"
            self.driver.save_screenshot(screenshot_name)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
