# Proyecto Automation Test Urban Routes 
## Alan Rodriguez
## sprint 8

## Descripción del proyecto

En este proyecto se realizan pruebas automatizadas, con la ayuda Selenium y Python. con el objetivo de probar las funciones de usuario en Urban Routes.
Dentro del código encontramos ocho pruebas
Los links del servidor y datos de pruebas se encuentran en el archivo data.py, las funciones se encuentran en urban_routes.py, y por ultimó las pruebas se encuentran el archivo main.py.

## Requisitos
Para la correcta ejecución de las pruebas se es necesario instalar: Python, Pytest , Selenium, WebDriver Manager 

## Instalacion 
pip install selenium
pip install webdriver-manager
pip install pytest

## Ejecucion de pruebas
pytest main.py 

## Descripción de tecnologías y técnicas utilizadas
Dentro de las tecnologías fue Python como lenguaje de programación y para la realización de las pruebas se utlizó Pytest (PyTest es un marco de trabajo que permite realizar pruebas unitarias para un software en Python.)
Las pruebas a relizar fueron mediante el metodo POM, con la ayuda de localizadores de cada elemento a utilizar en las pruebas, tambien se utilizo init para la construccion de la clase UrbanRoutes y sus funciones de atributos

Casos de Prueba
test_set_route: Verifica que se puedan establecer correctamente las direcciones de origen y destino.
test_select_comfort_rate: Verifica la selección de la tarifa Comfort.
test_entrance_phone_number: Valida que se pueda ingresar un número de teléfono.
test_payment_button: Comprueba que se pueda agregar un método de pago y verifica su correcta selección.
test_message_to_driver: Comprueba que se pueda enviar un mensaje al conductor y que se muestre correctamente.
test_select_blanket_scarves: Asegura que la opción de solicitar mantas y pañuelos esté habilitada.
test_select_ice_cream: (Agregar este método en el código) Verifica que se pueda seleccionar una cantidad específica de helados.
test_order_a_taxi: Verifica que se pueda abrir el modal para pedir un taxi y que la opción esté habilitada, así como que el texto correspondiente se muestre correctamente.
