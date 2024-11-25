from abc import ABC, abstractmethod

class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass

class Moveable(ABC):
    @abstractmethod
    def move(self, new_x, new_y):
        pass

class GameObject:
    _id_counter = 0 

    def __init__(self, name, x, y):
        self._id = GameObject._id_counter
        GameObject._id_counter += 1
        self._name = name
        self._x = x
        self._y = y

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

class Unit(GameObject):
    def __init__(self, name, x, y, hp):
        super().__init__(name, x, y)
        self._hp = hp  
        self._is_alive = True

    def is_alive(self):
        return self._is_alive

    def get_hp(self):
        return self._hp

    def receive_damage(self, damage):
        self._hp -= damage
        if self._hp <= 0:
            self._is_alive = False

class Archer(Unit, Attacker, Moveable):
    def __init__(self, name, x, y, hp, attack_damage):
        super().__init__(name, x, y, hp)
        self.attack_damage = attack_damage

    def attack(self, unit):
        if self.is_alive():
            unit.receive_damage(self.attack_damage)

    def move(self, new_x, new_y):
        if self.is_alive():
            self._x = new_x
            self._y = new_y

class Building(GameObject):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)

class Fort(Building, Attacker):
    def __init__(self, name, x, y, attack_damage):
        super().__init__(name, x, y)
        self.attack_damage = attack_damage

    def attack(self, unit):
        unit.receive_damage(self.attack_damage)

class MobileHouse(Building, Moveable):
    def move(self, new_x, new_y):
        self._x = new_x
        self._y = new_y

if __name__ == "__main__":
    archer = Archer("Archer1", 0, 0, 100, 10)
    target_unit = Unit("TargetUnit", 1, 1, 50)

    print(f"{archer.get_name()} attacks {target_unit.get_name()}")
    archer.attack(target_unit)
    print(f"{target_unit.get_name()} HP after attack: {target_unit.get_hp()}")
