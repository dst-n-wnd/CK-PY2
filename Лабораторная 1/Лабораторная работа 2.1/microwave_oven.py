from typing import Union


class MicrowaveOven:
    def __init__(self, color: str, time: Union[int, float], temp: Union[int, float]):
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

        self.time = None
        self.set_time(time)

        self.temp = None
        self.set_temp(temp)

    def set_time(self, time: Union[int, float]):
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

    def set_temp(self, temp: Union[int, float]):
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

