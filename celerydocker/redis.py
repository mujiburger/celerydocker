import json
import time
from traceback import format_exc

from redis import StrictRedis
from redis.exceptions import (ConnectionError,
                              TimeoutError)


class RedisException(Exception):
    pass


class Redis:
    configs = {
        "job2": {"host": "redis",
                 "port": 6379,
                 "db": 0},
        "job3": {"host": "redis",
                 "port": 6379,
                 "db": 1},
    }

    def __init__(self, namespace):
        self.namespace = namespace
        self.conf = self.configs[namespace]
        self.setup_redis()

    def setup_redis(self):
        self.r = StrictRedis(host=self.conf["host"],
                             port=self.conf["port"],
                             db=self.conf["db"],
                             decode_responses=True,
                             socket_timeout=1)

    def keys(self):
        try:
            ret = self.retry(self.r.keys)
        except Exception as e:
            raise RedisException("redis threw error while loading keys:", e)
        if ret:
            return ret
        else:
            return []

    def exists(self, key):
        try:
            ret = self.retry(self.r.exists, key)
        except Exception as e:
            raise RedisException("redis says nope to your key %s:" % (key), e)
        if ret:
            return True
        else:
            return False

    def get(self, key):
        try:
            ret = self.retry(self.r.get, key)
        except Exception as e:
            raise RedisException("redis says nope to your key %s:" % (key), e)
        if ret:
            return json.loads(ret)
        else:
            return None

    def expire(self, key, ttl):
        try:
            return self.retry(self.r.expire, key, ttl)
        except Exception as e:
            raise RedisException("""redis says that something went
                terribly wrong when you told it to expire key: %s
                in: %s... it also said """ % (key, ttl), e)

    def set(self, key, value):
        try:
            return self.retry(self.r.set, key, json.dumps(value))
        except Exception as e:
            raise RedisException("""redis says that something went
                terribly wrong when you told it to store the value: %s
                with the key: %s... it also said """ % (value, key), e)

    def lpush(self, key, value):
        try:
            return self.retry(self.r.lpush, key, value)
        except Exception as e:
            raise RedisException("""redis says that something went
                terribly wrong when you told it to lpush the value: %s
                with the key: %s... it also said """ % (value, key), e)

    def lrange(self, key, start=0, end=-1):
        try:
            ret = self.retry(self.r.lrange, key, start, end)
        except Exception as e:
            raise RedisException("redis says nope to your key %s:" % (key), e)
        if ret:
            return ret
        else:
            return None

    def incr(self, key, count=1):
        try:
            return self.retry(self.r.incr, key, count)
        except Exception as e:
            raise RedisException("""redis says that something went
                terribly wrong when you told it to incr the key:
                %s... it also said """ % (
                key), e)

    def hgetall(self, key):
        try:
            ret = self.retry(self.r.hgetall, key)
        except Exception as e:
            raise RedisException("redis says nope to your key %s:" % (key), e)
        if ret:
            return ret
        else:
            return None

    def hget(self, name, key):
        try:
            ret = self.retry(self.r.hget, name, key)
        except Exception as e:
            raise RedisException("redis says nope to your key %s:" % (key), e)
        if ret:
            return ret
        else:
            return None

    def hset(self, name, key, value):
        try:
            return self.retry(self.r.hset, name, key, json.dumps(value))
        except Exception as e:
            raise RedisException("""redis says that something went
                terribly wrong when you told it to hset the value: %s
                with the key: %s... to the name: %s it also said """ % (
                value, key, name), e)

    def hincrby(self, name, key, amount=1):
        try:
            return self.retry(self.r.hincrby, name, key, amount)
        except Exception as e:
            raise RedisException("""redis says that something went
                terribly wrong when you told it to hincrby the hash value named
                : %s with the key: %s... by %i it also said """ % (
                name, key, amount), e)

    def size(self):
        try:
            return self.retry(self.r.dbsize)
        except Exception as e:
            raise e

    def delete(self, key):
        try:
            return self.retry(self.r.delete, key)
        except Exception as e:
            raise RedisException("redis says nope to your key %s:" % (key), e)

    def retry(self, function, *args):
        count = 0
        while True:
            try:
                ret = function(*args)
                break
            except (ConnectionError, TimeoutError):
                print(format_exc())

                sleep_time = count
                if sleep_time > 30:
                    sleep_time = 30

                time.sleep(sleep_time)
                count += 1
                self.setup_redis()
                continue
        return ret
