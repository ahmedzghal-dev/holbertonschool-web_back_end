#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid


class Cache():
    """Cache class"""
    def __init__(self):
        """store an instance of the Redis
        client as a private variable"""
        self._redis = redis.Redis()
        self._redis.fulshdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key
        (e.g. using uuid)"""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
