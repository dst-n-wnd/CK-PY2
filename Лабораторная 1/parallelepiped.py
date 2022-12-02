from typing import Union


class Parallelepiped:
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

    def square(self): -> Union[int, float]
        """
        Метод считает площадь параллелепипеда
        :return: площадь параллелепипеда

        Пример:
        >>> parallelepiped = Parallelepiped(3, 4, 5)
        >>> parallelepiped.square()
        """
        pass

    def perimeter(self): -> Union[int, float]
        """
        Метод считает периметр параллелепипеда
        :return: периметр параллелепипеда

        Пример:
        >>> parallelepiped = Parallelepiped(1, 2, 3)
        >>> parallelepiped.perimeter()
        """
        pass

    def volume(self): -> Union[int, float]
        """
        Метод считает объем параллелепипеда
        :return: объем параллелепипеда

        Пример:
        >>> parallelepiped = Parallelepiped(8, 8, 3)
        >>> parallelepiped.volume()
        """
        pass


