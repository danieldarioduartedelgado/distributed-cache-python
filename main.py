# main.py

import time
from cache.distributed_cache import DistributedCache

def main():
    print("Prueba del sistema de caché distribuido\n")

    # Se inicializa la caché con un "namespace" dado
    cache = DistributedCache(namespace="juego")

    # Se ingresa una clave/valor al cache, por ejemplo jugador-puntos con un tiempo de vida de 5 seg
    print("Se setea una entrada: clave='jugador1', valor={'score': 900}, TTL=5s")
    cache.set("jugador1", {"score": 900}, ttl=5)

    print("     Obteniendo valor inmediatamente...")
    value = cache.get("jugador1")
    print(f"    Valor obtenido: {value}")

    print("\n   Esperando 1 segundo para mostrar el tiempo que falta para expirar...")
    time.sleep(1)
    print("     Tiempo para expirar:", cache.ttl("jugador1"))

    print("\n   Esperando 6 segundos para que expire...")
    time.sleep(6)

    print("     Intentando obtener valor nuevamente...")
    expired_value = cache.get("jugador1")
    print(f"    Valor después de expirar: {expired_value}")

    # Se ingresa una clave/valor al cache, pero sin tiempo de vida, se expirara manualmente
    print("\nSeteando otro valor sin expiración: clave='jugador2', valor={'score': 1200} ")
    cache.set("jugador2", {"score": 1200})
    print("     Obtenido:", cache.get("jugador2"))

    print("     Invalidando clave 'jugador2'...")
    cache.delete("jugador2")

    print("     Obteniendo después de invalidar...")
    print("     Valor:", cache.get("jugador2"))


if __name__ == "__main__":
    main()