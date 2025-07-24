"""
Доработайте класс `Vehicle`
"""
from abc import ABC
from homework_05.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight = 10000, fuel = 5000, fuel_consumption = 200):
        self.started = False
        self.weight  = weight
        self.fuel    = fuel   
        self.fuel_consumption = fuel_consumption
        
    def start(self): 
      # При вызове этого метода необходимо проверить состояние `started`. И если не `started`, то нужно проверить, что топлива больше нуля, 
      # и обновить состояние `started`, иначе нужно выкинуть исключение `exceptions.LowFuelError`
      if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError
    
    def move(self, distance): 
        # проверяет, что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), 
        # и изменяет количество оставшегося топлива, иначе выкидывает исключение `exceptions.NotEnoughFuel`
        fuel_required = distance * self.fuel_consumption
        if fuel_required > self.fuel:
            raise NotEnoughFuel([self.fuel, fuel_required])
        else:
            self.fuel -= fuel_required

         