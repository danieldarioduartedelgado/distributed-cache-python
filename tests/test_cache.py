# tests/test_cache.py

import time
import pytest
from cache.distributed_cache import DistributedCache

@pytest.fixture
def cache():
    return DistributedCache(namespace="test")

def test_set_and_get(cache):
    cache.set("clave1", "valor1")
    result = cache.get("clave1")
    assert result == "valor1"

def test_expiration(cache):
    cache.set("clave2", "valor2", ttl=2)
    time.sleep(3)
    result = cache.get("clave2")
    assert result is None

def test_delete(cache):
    cache.set("clave3", "valor3")
    cache.delete("clave3")
    result = cache.get("clave3")
    assert result is None

def test_overwrite_key(cache):
    cache.set("clave4", "valorInicial")
    cache.set("clave4", "valorActualizado")
    result = cache.get("clave4")
    assert result == "valorActualizado"
    
def test_ttl(cache):
    cache.set("clave3", "valor3", ttl=2)  # 2 segundos
    ttl_initial = cache.ttl("clave3")
    assert ttl_initial > 0 and ttl_initial <= 2  # TTL debe estar entre 0 y 2
    time.sleep(3)
    assert cache.get("clave3") is None  # Después del TTL debe expirar

def test_exists(cache):
    cache.set("clave4", "valor4")
    assert cache.exists("clave4") is True
    cache.delete("clave4")
    assert cache.exists("clave4") is False