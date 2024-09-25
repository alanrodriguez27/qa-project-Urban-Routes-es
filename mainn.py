import data
from urban_routes import UrbanRoutesPage # Importar el archivo que contiene la clase UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException



class TestUrbanRoutes ():

    driver = None

    @classmethod

    def setup_class(cls):
        options = Options()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    # Prueba 1

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, 'from')))
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        # Prueba 2 Seleccionar la tarifa Comfort


    def test_select_comfort_rate(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_taxi_button()
        routes_page.click_comfort_tariff()
        comfort_tariff_element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div.tcard.active > div.tcard-title")))
        assert "Comfort" in comfort_tariff_element.text, "La tarifa de comfort no se ha seleccionado"

        # Prueba 3 Rellenar el número de teléfono

    def test_entrance_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        routes_page.put_phone_number(phone_number)
        assert routes_page.get_phone_number() == phone_number


        # Prueba 4 Agregar Método de pago

    def test_payment_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_numb = data.card_number
        code_numb = data.card_code
        routes_page.set_add_payment_method(card_numb, code_numb)
        assert routes_page.check_select_card_button() == True
        assert 'Card' in routes_page.check_text_payment_button()

        # Prueba 5 Escribir un mensaje para el conductor

    def test_message_to_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_test = data.message_for_driver
        routes_page.send_message(message_test)
        comment_field_locator = (By.XPATH, "//*[@id='comment']")
        comment_field = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(comment_field_locator))
        actual_message = comment_field.get_attribute('value')
        assert actual_message == message_test, f"El mensaje no se escribió correctamente."

        # Prueba 6 Pedir una manta y pañuelos
    def test_select_blanket_scarves(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_scarves()
        assert routes_page.check_blanket_scarves_is_enabled() == True

        # Prueba 7 Pedir 2 helados

    def test_order_icecream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_icecream()
        counter_element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//*[@class='counter-value']")))
        counter = counter_element.text
        counter_number = int(counter)
        assert counter_number == data.ice_cream, f"La cantidad no coincide"

        # Prueba 8 Aparece el modal para buscar un taxi

    def test_order_a_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_modal_order_taxi()
        assert routes_page.check_order_taxi_is_enabled() == True
        assert 'Call a taxi' in routes_page.check_text_order_taxi()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()