# cache/distributed_cache.py

import redis
import json

class DistributedCache:
    """
    Esta clase implementa una caché distribuida basada en Redis con soporte para:
        - Operaciones básicas: set, get, delete, exists, ttl.
        - Expiración automática (TTL).
        - Namespaces lógicos: permiten aislar datos de distintos módulos o servicios,
        evitando colisiones de claves dentro de un entorno compartido de Redis.
    Args:
        namespace (str): Prefijo logico para las claves.
        host (str): Direccion del servidor Redis.
        port (int): Puerto del servidor Redis.
        db (int): Numero de base de datos Redis.
    """
    def __init__(self, namespace="default", host='localhost', port=6379, db=0):
        """
        Inicializa el cliente Redis y configura un namespace lógico.
        """
        self.namespace = namespace
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def _format_key(self, key):
        """
        Formatea la clave agregando el namespace como prefijo lógico.   
        Por ejemplo, con namespace="juego" y key="jugador_1", la clave final será:
        "juego:jugador_1"
        """
        return f"{self.namespace}:{key}"

    def set(self, key, value, ttl=None):
        """
        Almacena un valor en caché con un TTL opcional (en segundos).
        El valor se convierte a JSON para permitir objetos complejos.
        """
        full_key = self._format_key(key)
        value_str = json.dumps(value)

        if ttl:
            self.client.setex(full_key, ttl, value_str)
        else:
            self.client.set(full_key, value_str)

    def get(self, key):
        """
        Recupera un valor desde la caché.
        Si no existe o ha expirado, retorna None.
        """
        full_key = self._format_key(key)
        value = self.client.get(full_key)
        if value is None:
            return None
        return json.loads(value)

    def delete(self, key):
        """
        Elmina manualmente una clave del caché.
        """
        full_key = self._format_key(key)
        self.client.delete(full_key)

    def exists(self, key):
        """
        Verifica si una clave existe en la caché.
        """
        full_key = self._format_key(key)
        return self.client.exists(full_key) == 1

    def ttl(self, key):
        """
        Retorna el TTL restante (en segundos) de una clave.
        Si la clave no existe o no tiene TTL, puede retornar -1 o -2.
        """
        full_key = self._format_key(key)
        return self.client.ttl(full_key)