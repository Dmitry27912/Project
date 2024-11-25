class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def do_something(self):
        print("Doing something...")


# Пример использования
singleton = Singleton()
singleton.do_something()
