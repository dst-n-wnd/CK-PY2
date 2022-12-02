class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self.pages = pages

    def __str__(self):
        return f" Бумажная Книга '{self.name}'. Автор {self.author}. Страницы {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        if not isinstance(duration, float):
            raise TypeError("Длительность должна быть типа float")
        if duration < 0:
            raise ValueError("Длительность не может быть отрицательной")
        self.duration = duration

    def __str__(self):
        return f" Аудио Книга '{self.name}'. Автор {self.author}. Длительность {self.duration}"


print(PaperBook("Букварь", "Жуков", 100))
print(AudioBook("Идиот", "Достоевский", 700.23))
