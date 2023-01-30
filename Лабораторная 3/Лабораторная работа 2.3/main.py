class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self._pages = new_pages

    def __str__(self):
        return f" Бумажная Книга '{self.name}'. Автор {self.author}. Страницы {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if not isinstance(new_duration, float):
            raise TypeError("Длительность должна быть типа float")
        if new_duration < 0:
            raise ValueError("Длительность не может быть отрицательной")
        self._duration = new_duration

    def __str__(self):
        return f" Аудио Книга '{self.name}'. Автор {self.author}. Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


print(PaperBook("Букварь", "Жуков", 100))
print(AudioBook("Идиот", "Достоевский", 700.23))
print(repr(PaperBook("Букварь", "Жуков", 100)))
print(repr(AudioBook("Идиот", "Достоевский", 700.23)))
