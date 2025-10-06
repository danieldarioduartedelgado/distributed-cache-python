# Distributed Cache Project
Este proyecto implementa una cache distribuida usando Python y Redis. Basicamente esta disenado para:
- Almacenamiento y recuperación eficiente de datos.
- Manejo de consistencia distribuida.
- Soporte para expiración de claves y eliminación manual (invalidación de caché).
- Facilidad de escalabilidad a múltiples nodos o instancias.
- Simplicidad y mantenibilidad del codigo y pruebas unitarias.

## Instalación y configuración
Pasos para levantar el entorno localmente y trabajar con el sistema de caché distribuido.
## 1. Clonar el repositorio
git clone https://github.com/danieldarioduartedelgado/distributed-cache-python.git
cd distributed-cache-python
## 2. Crear entormo virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
## 3. Instalar dependencias
pip install -r requrirements.txt
## 4. Levantar Redis con Docker
Se debe tener Docker corriendo, luego ejecutar:
docker compose up -d 
Esto levanta un contenedor Redis escuchando en el puerto 6379

### Uso basico
Para comprobar el comportamiento del cache, se puede ejecutar el archivo main.py
python3 main.py
Este script hace lo siguiente:
a. Inserta claves en cache con o sin expiracion
b. Recupera valores
c. Elimina entradas o claves
d. Muestra el manejo de expiracion automatica

#### Pruebas
El proyecto incluye pruebas unitarias usando pytest
Para ejecutar las pruebas, con el entorno activo se ejecuta:
PYTHONPATH=. pytest
Se deberia mostrar una salida que indica que las pruebas pasaron exitosamente:
collected 4 items
tests/test_cache.py ....      [100%]

##### Stack tecnologico
Python 3.12+
Redis (Para implementar el cache en memoria)
Docker + Docker Compose
Pytest (testing)
redis-py(Clientes de Redis para Python)

###### Estructura del proyecto
distributed_cache_project/
    cache/
       distributed_cache.py    # Logica principal del sistema de cache
    tests/
        test_cache.py           # Pruebas unitarias
    main.py                     # Script de ejemplo / demo
    requirements.txt            # Dependencias del proyecto
    docker-compose.yml          # Configuracion de Redis con Docker
    README.md                   # Este archivo

###### Autor
Daniel D. Duarte
Oct 2025