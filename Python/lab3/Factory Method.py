# Продукты
class Product:
    def use(self):
        pass

class ConcreteProductA(Product):
    def use(self):
        print("Using Product A")

class ConcreteProductB(Product):
    def use(self):
        print("Using Product B")

# Создатель
class Creator:
    def factory_method(self):
        raise NotImplementedError("You should implement this method!")

    def some_operation(self):
        product = self.factory_method()
        product.use()

# Конкретные создатели
class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()

# Пример использования
creator_a = ConcreteCreatorA()
creator_a.some_operation()  # Output: Using Product A

creator_b = ConcreteCreatorB()
creator_b.some_operation()  # Output: Using Product B
