# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує

class Passenger():
    def __init__(self, name: str, destination: str):
        self._name = name
        self._destination = destination


# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали

class Transport():
    def __init__(self, speed: float):
        self._speed = speed

    def move(self, destination: str, distance: float):
        time = distance / self._speed
        print(f"Moving to {destination}. Time: {time}")
        return time


# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()

class Bus(Transport):
    def __init__(self, speed: float, passengers: list[Passenger], capacity: int):

        super().__init__(speed)
        self._passengers = passengers
        self._capacity = capacity

    def board_passenger(self, passenger):
        if len(self._passengers) >= self._capacity:
            print("No free place")

        else:
            self._passengers.append(passenger)

    def move(self, destination, distance):
        leaving = []

        for passenger in self._passengers:
            if passenger._destination == destination:
                leaving.append(passenger)

        print(f"Passengers leaving: {len(leaving)}")

        self._passengers = [p for p in self._passengers if p._destination != destination]

        return super().move(destination, distance)


p1 = Passenger("Anna", "Kyiv")
bus = Bus(speed=60, passengers=[], capacity=2)
bus.board_passenger(p1)
bus.move("Kyiv", 120)


