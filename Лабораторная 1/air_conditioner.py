from typing import Union


class Conditioner:
    def __init__(self, model: str, temp: Union[int, float]):
        if not isinstance(model, str):
            raise TypeError("Модель кондиционера должна быть типа str")
        self.model = model

        if not isinstance(temp, (int, float)):
            raise TypeError("Температура должна быть типа int или float")
        self.temp = temp

    def turn_on(self): -> None
        """
        Метод включает кондиционер

        Пример:
        >>> conditioner = Conditioner("132fshj", 15)
        >>> conditioner.turn_on()
        """
        pass

    def turn_off(self): -> None
        """
        Метод выключает кондиционер

        Пример:
        >>> conditioner = Conditioner("843920ghfkhs", 17)
        >>> conditioner.turn_on()
        >>> conditioner.turn_off()
        """
        pass
