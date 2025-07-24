"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.engine import Engine

class Car(Vehicle):
    engine = None

    def set_engine(self, Engine):
        self.engine = Engine