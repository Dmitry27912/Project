# Продукты A
class AbstractProductA:
    def use(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def use(self):
        print("Using Product A1")

class ConcreteProductA2(AbstractProductA):
    def use(self):
        print("Using Product A2")

# Продукты B
class AbstractProductB:
    def use(self):
        pass

class ConcreteProductB1(AbstractProductB):
    def use(self):
        print("Using Product B1")

class ConcreteProductB2(AbstractProductB):
    def use(self):
        print("Using Product B2")

# Абстрактная фабрика
class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

# Конкретные фабрики
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

# Пример использования
factory1 = ConcreteFactory1()
product_a1 = factory1.create_product_a()
product_b1 = factory1.create_product_b()
product_a1.use()  # Output: Using Product A1
product_b1.use()  # Output: Using Product B1

factory2 = ConcreteFactory2()
product_a2 = factory2.create_product_a()
product_b2 = factory2.create_product_b()
product_a2.use()  # Output: Using Product A2
product_b2.use()  # Output: Using Product B2
