from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int) -> None:
        if year < 1886:  # Первое автомобильное средство было создано в 1886 году
            raise ValueError("Year must be 1886 or later.")
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        """Запускает двигатель автомобиля."""
        pass

    @abstractmethod
    def stop_engine(self) -> None:
        """Останавливает двигатель автомобиля."""
        pass

    @abstractmethod
    def honk_horn(self) -> str:
        """Издает звуковой сигнал автомобиля.

        Пример:
        >>> vehicle = Car('Toyota', 'Corolla', 2020)
        >>> vehicle.honk_horn()
        'Beep! Beep!'
        """
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int) -> None:
        super().__init__(make, model, year)
        self.number_of_doors = 4

    def start_engine(self) -> None:
        """Запускает двигатель машины."""
        pass

    def stop_engine(self) -> None:
        """Останавливает двигатель машины."""
        pass

    def honk_horn(self) -> str:
        """Издает звуковой сигнал машины."""
        return "Beep! Beep!"


class Bicycle(ABC):
    def __init__(self, brand: str, gear_count: int) -> None:
        if gear_count < 1:
            raise ValueError("Gear count must be at least 1.")
        self.brand = brand
        self.gear_count = gear_count

    @abstractmethod
    def pedal(self) -> None:
        """Начинает крутить педали велосипеда."""
        pass

    @abstractmethod
    def brake(self) -> None:
        """Тормозит велосипед."""
        pass

    @abstractmethod
    def ring_bell(self) -> str:
        """Звонит в звонок велосипеда.

        Пример:
        >>> bicycle = MountainBike('Trek', 18)
        >>> bicycle.ring_bell()
        'Ring! Ring!'
        """
        pass


class MountainBike(Bicycle):
    def __init__(self, brand: str, gear_count: int) -> None:
        super().__init__(brand, gear_count)
        self.suspension_type = "full"

    def pedal(self) -> None:
        """Начинает крутить педали горного велосипеда."""
        pass

    def brake(self) -> None:
        """Тормозит горный велосипед."""
        pass

    def ring_bell(self) -> str:
        """Звонит в звонок горного велосипеда."""
        return "Ring! Ring!"


class ElectronicDevice(ABC):
    def __init__(self, brand: str, power: int) -> None:
        if power <= 0:
            raise ValueError("Power must be a positive value.")
        self.brand = brand
        self.power = power

    @abstractmethod
    def turn_on(self) -> None:
        """Включает электронное устройство."""
        pass

    @abstractmethod
    def turn_off(self) -> None:
        """Выключает электронное устройство."""
        pass

    @abstractmethod
    def get_status(self) -> str:
        """Возвращает текущее состояние устройства.

        Пример:
        >>> device = Laptop('Dell', 65)
        >>> device.get_status()
        'Device is off.'
        """
        pass


class Laptop(ElectronicDevice):
    def __init__(self, brand: str, power: int) -> None:
        super().__init__(brand, power)
        self.is_on = False

    def turn_on(self) -> None:
        """Включает ноутбук."""
        self.is_on = True

    def turn_off(self) -> None:
        """Выключает ноутбук."""
        self.is_on = False

    def get_status(self) -> str:
        """Возвращает текущее состояние ноутбука."""
        return "Device is on." if self.is_on else "Device is off."
