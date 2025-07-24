"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, max_cargo, weight=10000, fuel=5000, fuel_consumption=200):
        self.cargo = 0 
        self.max_cargo = max_cargo
        super().__init__(weight, fuel, fuel_consumption)

    def load_cargo(self, cargo):        
        if cargo + self.cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload([cargo + self.cargo, self.max_cargo])
        
    def remove_all_cargo(self):
        cargo_current = self.cargo
        self.cargo = 0
        return cargo_current
