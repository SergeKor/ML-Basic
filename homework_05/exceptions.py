from datetime import datetime

class LowFuelError(Exception):
    def __init__(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        str_message = f"Критически низкий уровень топлива = {message}"
        message += timestamp + ': ' + str_message
        super().__init__(message)
    
    
class NotEnoughFuel(Exception):
    def __init__(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        str_message = f"Недостаточный уровень топлива = {message[0]}. Необходимо {message[1]}"
        message = timestamp + ': ' + str_message
        super().__init__(message)

class CargoOverload(Exception):
    def __init__(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        str_message = f"Перегруз = {message[0]} при допустимом весе = {message[1]}"
        message = timestamp + ': ' + str_message
        super().__init__(message)

