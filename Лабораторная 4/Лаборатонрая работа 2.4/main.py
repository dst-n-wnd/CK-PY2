import doctest
from typing import Union


class Car:
    """
    Базовый класс автомобиля, от которго наследуются дочерние классы
    легкого и грузового автомобилей.
    """
    def __init__(self, engine_power: Union[int, float], max_speed: Union[int, float], brand: str):
        """
        В конструкторе данного класса задаются следующие параметры
        :param engine_power: мощность двигателя
        :param max_speed: максимальная скорость автомобиля
        :param brand: марка автомобиля

        Каждое поле проверяется на корректность указанного типа на входе, а также
        поля enigne_power и max_speed проверяются на корректность введенного значения.
        """
        if not isinstance(engine_power, (int,float)):
            raise TypeError("Количество колес должно быть типа int")
        if engine_power < 0:
            raise ValueError("Количество колес не может быть отрицательным")
        self.engine_power = engine_power

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Цвет должен быть типа str")

        if max_speed < 0:
            raise ValueError("Макисмальная скорость не может быть отрицательной")
        self.max_speed = max_speed

        if not isinstance(brand, str):
            raise TypeError("Марка должна быть типа str")
        self.brand = brand

    def __str__(self) -> str:
        """
        Данный метод возвращает строковое представление, в котором содержится вся необходимая информация
        об объекте.
        :return: строка с параметрами автомобиля
        """
        return f"Автомобиль. Мощность двигателя: {self.engine_power}, Максимальная сокрость: {self.max_speed}, Марка: {self. brand}"

    def __repr__(self) -> str:
        """
        Также возвращается строковое представление со всеми данными об объекте,
        но в другом формате с именем переменной класса.
        :return: строка с именем переменной класса и данными об автомобиле
        """
        return f"{self.__class__.__name__}(Марка: {self.brand}, Мощность двигателя: {self.engine_power}, Максимальная скорость: {self.max_speed})"

    def is_engine_stared(self) -> bool:
        """
        Метод, который проверяет, заведен ли двигатель в автомобиле(Наследуется всеми дочерними классами
        в данной иерархии)
        :return: возвращает True, если двигатель заведен. В противном случае False.

        Пример:
        >>> car_1 = Car(100, 220, 'Lada')
        >>> car_1.is_engine_stared()
        """
        pass

    def maneuvering(self) -> None:
        """
        Абстрактный метод, у которого отсутствует реализация в родительском классе. Создан для
        реализации в дочерних классах.

        :return: в данном классе ничего не возвращает
        """
        pass


class PassengerCar(Car):
    def __init__(self, engine_power, max_speed: Union[int, float], brand: str, number_of_seats: int):
        """
        Унаследованный и перегруженный конструктор класса PassengerCar

        :param engine_power: мощность двигателя в лошадиных силах
        :param max_speed: максимальная скорость
        :param brand: марка автомобиля
        :param number_of_seats: количество пассажирских мест

        Поля данного конструктора также были проверены через условия. В случаяе некорректно
        введенных данных, вызываются ошибки типов TypeError и ValueError
        """
        super().__init__(engine_power, max_speed, brand)
        if not isinstance(number_of_seats, int):
            raise TypeError("Количество мест должно быть типа int")
        if number_of_seats < 0:
            raise ValueError("Количество мест не может быть отрицательным")
        self.number_of_seats = number_of_seats

    def __str__(self) -> str:
        """
        Унаследованный от родительского класса и переопределенный метод __str__

        :return: возвращает строковое представление с данными о легковом автомобиле
        """
        return f"Легковой автомобиль. Марка: {self.brand}, Мощность двигателя(в л.с): {self.engine_power}, Максимальная скорость: {self.max_speed}, " \
               f"Количество мест: {self.number_of_seats}"

    def maneuvering(self) -> str:
        """
        Переопределнный метод, который выводит сообщение о маневренности легкового автомобиля

        :return: строка с сообщением о маневренности

        """
        return "Высокая маневренность"


class Truck(Car):
    def __init__(self, engine_power: Union[int, float], max_speed: Union[int, float],
                 brand: str, load_capacity: Union[int, float]):
        """
        Унаследованный и перегруженный конструктор класса Truck

        :param engine_power: мощность двигателя в лошадиных силах
        :param max_speed: максимальная скорость грузовика
        :param brand: марка
        :param load_capacity: грузоподъемность

        Поля данного конструктора были проверены через условия. В случаяе некорректно
        введенных данных, вызываются ошибки типов TypeError и ValueError
        """
        super().__init__(engine_power, max_speed, brand)
        if not isinstance(load_capacity, (int, float)):
            raise TypeError("Грузоподъемность должна быть типа int или float")
        if load_capacity < 0:
            raise ValueError("Грузоподъемность не может быть отрицательной")
        self.load_capacity = load_capacity

    def __str__(self) -> str:
        """
        Унаследованный от родительского класса и переопределнный метод __str__
        :return: возвращает строковое представление с данными о грузовом автомобиле
        """
        return f"Грузовой автомобиль. Марка: {self.brand}, Мощность двигателя(в л.с): {self.engine_power}, " \
               f"Максимальная скорость: {self.max_speed}, Грузоподъемность(в кг): {self.load_capacity}"

    def maneuvering(self) -> str:
        """
        Переопределнный метод, который выводит сообщение о маневренности грузового автомобиля

        :return: строка с сообщением о маневренности

        """
        return "Низкая маневренность"


if __name__ == "__main__":
    car = Car(110, 240, 'Chevrolette')
    print(car)
    pass_car = PassengerCar(220, 300, 'Mersedez-Benz', 4)
    print(pass_car)
    truck = Truck(300, 150, 'Газель', 5000)
    print(truck)

    print(car.__repr__())
    print(pass_car.__repr__())
    print(truck.__repr__())
    print(pass_car.maneuvering())
    print(truck.maneuvering())

    doctest.testmod()
