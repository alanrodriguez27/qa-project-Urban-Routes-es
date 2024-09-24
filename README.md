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
test_set_route: Verifica que las direcciones de origen y destino se configuren correctamente.
test_set_comfort_tariff: Asegura que se seleccione la tarifa de confort.
test_phone_number: Verifica la entrada de un número de teléfono.
test_credit_card: Confirma que la información de la tarjeta de crédito se llena correctamente.
test_message_driver: Comprueba que el mensaje al conductor se envíe correctamente.
test_order_blanket_scarves: Asegura que se seleccionen mantas en el pedido.
test_order_ice_cream: Verifica que se ordene la cantidad correcta de helados.
test_order_taxi: Comprueba que la opción de pedir un taxi esté habilitada.

