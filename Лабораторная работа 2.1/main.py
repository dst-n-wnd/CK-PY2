from typing import Union
import doctest


class Conditioner:
    """
    Класс, описывающий кондиционер. При создании объекта, конктруктор данного класса принимает 2
    параметра: model и temp, которые задают модель и температуру соответственно.

    """
    def __init__(self, model: str, temp: Union[int, float]):
        if not isinstance(model, str):
            raise TypeError("Модель кондиционера должна быть типа str")
        self.model = model

        if not isinstance(temp, (int, float)):
            raise TypeError("Температура должна быть типа int или float")
        self.temp = temp

    def turn_on(self) -> None:
        """
        Метод включает кондиционер
        Пример:
        >>> conditioner = Conditioner("132fshj", 15)
        >>> conditioner.turn_on()
        """
        pass

    def turn_off(self) -> None:
        """
        Метод выключает кондиционер
        Пример:
        >>> conditioner = Conditioner("843920ghfkhs", 17)
        >>> conditioner.turn_on()
        >>> conditioner.turn_off()
        """
        pass


class MicrowaveOven:
    """
    Класс, описывающий микроволновку. Конструктор принимает 3 параметра: color, time и temp.
    color - цвет печи
    time - время разогрева
    temp - температура разогрева
    """
    def __init__(self, color: str, time: Union[int, float], temp: Union[int, float]):
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

        self.time = None
        self.set_time(time)

        self.temp = None
        self.set_temp(temp)

    def set_time(self, time: Union[int, float]) -> None:
        """
        Метод устанавливает время разогрева для микроволновки
        :param time: устанавливаемое время
        Пример:
        >>> oven = MicrowaveOven('black', 100, 200)
        >>> oven.set_time(125.5)
        """
        if not isinstance(time, (int, float)):
            raise TypeError("Время должно быть типа int или float")
        if time < 0:
            raise ValueError("Время не может быть отрицательным")

        pass

    def set_temp(self, temp: Union[int, float]) -> None:
        """
        Метод устанавливает температуру для микроволновки
        :param temp: устанавливаемая температура
        Пример:
        >>> oven = MicrowaveOven('white', 0, 0)
        >>> oven.set_temp(100)
        """

        if not isinstance(temp, (int, float)):
            raise TypeError("Температура должна быть типа int или float ")

        pass


class Parallelepiped:
    """
    Класс, описывающий параллелепипед. Конструктор принимает в себя 3 параметра:
    length - длина
    width - ширина
    high - высота
    """
    def __init__(self, length: Union[int, float], width: Union[int, float], high: Union[int, float]):
        if not isinstance(length, (int, float)):
            raise TypeError("Длина куба должна быть положительной")
        if length < 0:
            raise ValueError("Длина куба не может быть отрицательной")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина куба должна быть положительной")
        if width < 0:
            raise ValueError("Ширина куба не может быть отрицательной")
        self.width = width

        if not isinstance(high, (int, float)):
            raise TypeError("Высота куба должна быть положительной")
        if high < 0:
            raise ValueError("Высота куба не может быть отрицательной")
        self.high = high

    def square(self) -> Union[int, float]:
        """
        Метод считает площадь параллелепипеда
        :return: площадь параллелепипеда
        Пример:
        >>> parallelepiped = Parallelepiped(3, 4, 5)
        >>> parallelepiped.square()
        """
        pass

    def perimeter(self) -> Union[int, float]:
        """
        Метод считает периметр параллелепипеда
        :return: периметр параллелепипеда
        Пример:
        >>> parallelepiped = Parallelepiped(1, 2, 3)
        >>> parallelepiped.perimeter()
        """
        pass

    def volume(self) -> Union[int, float]:
        """
        Метод считает объем параллелепипеда
        :return: объем параллелепипеда
        Пример:
        >>> parallelepiped = Parallelepiped(8, 8, 3)
        >>> parallelepiped.volume()
        """
        pass


if __name__ == "__main__":
    doctest.testmod()
