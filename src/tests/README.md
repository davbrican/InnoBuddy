Para ejecutar los tests de integración, se debe ejecutar el comando:
```
python3 -m pytest src/tests/test_commands.py
```

Para ejecutar los tests unitarios de los servicios, se debe ejecutar el comando:
```
python3 -m pytest src/tests/test_localizaciones_service.py src/tests/test_rating_service.py src/tests/test_user_service.py
```

Para ejecutar los tests de carga de datos, se debe ejecutar el comando:
```
python3 -m unittest -f tests.test_load_data
```
A continuación, para visualizar los resultados de los tests de carga de datos, debe abrir en el navegador la página:
```
http://localhost:8089/
```
seleccionar el número de usuarios y el spawn rate, y presionar el botón "Start swarming".
