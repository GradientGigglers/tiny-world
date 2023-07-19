import redis


class RedisSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if not RedisSingleton._instance:
            RedisSingleton()
        return RedisSingleton._instance

    def __init__(self):
        if RedisSingleton._instance:
            raise Exception("RedisSingleton instance already exists")
        else:
            self._redis_connection = redis.Redis(host='redis', port=6379, db=0)
            RedisSingleton._instance = self

    def get_connection(self):
        return self._redis_connection
