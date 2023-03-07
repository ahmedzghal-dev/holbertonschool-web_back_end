#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
import uuid
from functools import wraps
from typing import Callable, Union


def count_calls(method: Callable) -> Callable:
    """count_calls
    decorator that takes a single method
    Callable argument and returns a Callable.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Incrementing values"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator to store the history of
    inputs and outputs for a particular function"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        in_list_name = "{}:inputs".format(method.__qualname__)
        out_list_name = "{}:outputs".format(method.__qualname__)

        self._redis.rpush(in_list_name, str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(out_list_name, output)
        return output
    return wrapper


class Cache:
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

    def get(self, key: str, fn=None) -> str:
        """take a key string argument and
        an optional Callable argument"""
        if (self._redis.exists(key)):
            value = self._redis.get(key)
            if fn is None:
                return value

            return fn(value)
        return None

    def get_str(self, key: str) -> str:
        """parametrize Cache.get with
        the correct conversion function."""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """parametrize Cache.get with
        the correct conversion function."""
        return self.get(key, int)
