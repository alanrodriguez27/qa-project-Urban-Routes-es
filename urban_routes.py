import data
import helpers  # Importar el archivo con los métodos de apoyo
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions

class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button_field = (By.XPATH, '//button[text()="Pedir un taxi"]')
    comfort_tariff_field = (By.XPATH, "//*[@class='tcard-title' and text()='Comfort']")
    phone_button_field_1 = (By.XPATH, '//button[text()="Pedir un taxi"]')
    phone_number_field_2 = (By.ID, 'phone')
    next_button_locator = (By.XPATH, "//*[@class='button full' and text()='Siguiente']")
    code_phone = (By.ID, "code")
    button_confirm_locator = (By.XPATH, "//*[@class='button full' and text()='Confirmo']")
    payment_method_button_field = (By.XPATH, "//*[@class='pp-text' and text()='Metodo de pago']")
    credit_card_field = (By.XPATH, "//*[@class='pp-title' and text()='Add card']")
    card_number = (By.ID, 'number')
    cvv_field = (By.XPATH, '//div[@class = "section active unusual"]//input[@id ="code"]')
    submit_card_button = (By.ID, 'submit-card')
    message_field = (By.ID, 'comment')
    slider_field = (By.XPATH, "//*[@class='slider round']")
    increment_button_field = (By.XPATH, "//*[@class='counter-plus']")
    button_order_field = (By.XPATH, "//*[@class='smart-button']")
    blanket_button = (By.ID, 'blanket')
    modal_order_taxi = (By.CLASS_NAME, 'smart-button')
    trip_information = (By.XPATH, '//div[contains(text(),"El conductor llegará en")]')
    option_flash_button = (By.XPATH, '//div[text()="Flash"]')



    def __init__(self, driver):
        self.driver = driver


# Prueba uno - ruta
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

# Prueba 2 - taxi

    def check_option_flash_button_is_enabled(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.option_flash_button))
        return self.driver.find_element(*self.option_flash_button).is_enabled()
    def click_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.taxi_button_field))
        self.driver.find_element(*self.taxi_button_field).click()


    def click_comfort_tariff(self):
        comfort_tariff = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.comfort_tariff_field))
        comfort_tariff.click()

# Prueba 3 - phone
    def click_phone(self):
        phone_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.phone_button_field_1))
        phone_button.click()

    def fill_phone_number(self, phone_number):
        wait = WebDriverWait(self.driver, 10)
        phone_number_field = wait.until(ec.visibility_of_element_located(self.phone_number_field_2))
        phone_number_field.clear()
        phone_number_field.send_keys(phone_number)
        next_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.next_button_locator))
        next_button.click()
        code = helpers.retrieve_phone_code(self.driver)
        code_field = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(self.code_phone))
        code_field.clear()
        code_field.send_keys(code)
        button_confirm = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.button_confirm_locator))
        button_confirm.click()

    def get_phone_number(self):
        phone_number_field_locator = (By.XPATH, "//*[@id='phone']")
        phone_number_field = self.driver.find_element(*phone_number_field_locator)
        return phone_number_field.get_attribute('value')


# Prueba 4 - metodo de pago
    def click_payment_method_card_button(self):
        payment_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.payment_method_button_field))
        payment_button.click()
        card_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.credit_card_field))
        card_button.click()

    def fill_credit_number_card(self, card):
        wait = WebDriverWait(self.driver, 10)
        card_number_field = wait.until(ec.visibility_of_element_located(self.credit_card_field))
        card_number_field.clear()
        card_number_field.send_keys(card)
        card_number_field.send_keys(Keys.TAB)

    def fill_credit_cvv_card(self, cvv):
        wait = WebDriverWait(self.driver, 10)
        cvv_number_field = wait.until(ec.visibility_of_element_located(self.cvv_field))
        cvv_number_field.clear()
        cvv_number_field.send_keys(cvv)
        cvv_number_field.send_keys(Keys.TAB)

# Prueba 5 - mensaje para el conductor
    def send_message(self, message):
        wait = WebDriverWait(self.driver, 10)
        message_field = wait.until(ec.visibility_of_element_located(self.message_field))
        message_field.clear()
        message_field.send_keys(message)

# Prueba 6 - pedir una manta
    def click_blanket_scarves(self):
        slider = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.slider_field))
        slider.click()

# Prueba 7 - Pedir helado
    def click_order_icecream(self):
        increment_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.increment_button_field))
        for _ in range(data.ice_cream):
            increment_button.click()

# Aparece modal de busqueda de taxi

    def check_order_taxi_is_enabled(self):
        return self.driver.find_element(*self.modal_order_taxi).is_enabled()

    def click_modal_order_taxi(self):
        button_order = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.button_order_field))
        button_order.click()

    def check_text_order_taxi(self):
        return self.driver.find_element(*self.modal_order_taxi).text

    def select_modal_order_taxi(self):
        self.check_order_taxi_is_enabled()
        self.click_modal_order_taxi()
        self.check_text_order_taxi()












