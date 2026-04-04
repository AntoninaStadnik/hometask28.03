# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального
import random

class Car:
    def __init__(self, model: str, car_mileage: int, gas_level:int, fuel_consumption:int, is_it_working:bool ):
        self.model = model
        self.car_mileage = car_mileage
        self.gas_level = gas_level
        self.fuel_consumption = fuel_consumption
        self.is_it_working = is_it_working

    def show_info(self):
        print(f"Model: {self.model}")
        print(f"Mileage: {self.car_mileage}")
        print(f"Gas level: {self.gas_level}")
        print(f"Fuel consumption: {self.fuel_consumption}")
        print(f"Is working: {self.is_it_working}")

    def ask_model(self):
        print(f"Model: {self.model}")

    #  проїхати певну відстань, має змінитись пробіг та рівень
    # пального, якщо автомобіль справний та достатньо
    # пального
    def ride_distance(self, distance: int):
        if not self.is_it_working:
            print("Car is not working")
            return

        needed_fuel = (distance * self.fuel_consumption) / 100

        if needed_fuel > self.gas_level:
            print("Not enough fuel")
            return

        self.car_mileage += distance
        self.gas_level -= needed_fuel

        print(f"You drove {distance} km")

    # З ймовірністю 40% автомобіль може зламатись
    #  ремонт
    #  поповнення пального
    def check_breakdown(self):
        if random.random() < 0.4:
            self.is_it_working = False
            print("Car has broken down!")

Car1 = Car("Audi", 300, 50, 10, True)
Car1.ride_distance(10)
Car1.show_info()