import time
import threading


class single_model(object):

    instance = None
    lock = threading.RLock()

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        print("第一步先调用这里")
        print(cls.lock)
        if cls.instance:
            return cls.instance
        with cls.lock:
            if not cls.instance:
                time.sleep(0.2)
                cls.instance = object.__new__(cls)
            return cls.instance

    # with上下文 test
    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        return self


def getInstance():
    return single_model('name is params')


with getInstance() as sigIns:
    print('with demo!')