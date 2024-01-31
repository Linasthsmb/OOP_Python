if __name__ == "__main__":
    # Write your solution here
    class Pets:
        def __init__(self, name: str, age: int, average_life_expectancy: int):
            """
                Создание и подготовка к работе объекта "питомец"
                :param name: имя питомца
                :param age: возраст питомца
                :param average_life_expectancy: средняя продолжительность жизни
            """
            if not isinstance(name, str):
                raise TypeError
            if not isinstance(age, int):
                raise TypeError
            if not isinstance(average_life_expectancy, int):
                raise TypeError
            if average_life_expectancy <= 0:
                raise ValueError
            if age < 0:
                raise ValueError
            self.name = name
            self.age = age
            self.average_life_expectancy = average_life_expectancy

        def __str__(self) -> str:
            """
            Возвращает текстовое представление об экземпляре класса питомец
            :return: строка с информацией об экземпляре
            """
            return f"Pet {self.name}. The age of pet {self.age}"

        def __repr__(self) -> str:
            """
            Возвращает строку, показывающую, как может быть инициализирован экземпялр класса питомец
            :return: валидная строка(python)
            """
            return f"{self.__class__.__name__}({self.name!r}, {self.age}, {self.average_life_expectancy})"

        def left_to_live(self) -> int:
            """
            Метод, показывающий сколько в среднем осталось жить питомцу
            :param self:
            :return: возвращает остаток жизни относительно средней продолжительности вида
            """
            if self.average_life_expectancy < self.age:
                raise ValueError("Program doesn't know")
            return self.average_life_expectancy - self.age

        @staticmethod
        def sound() -> str:
            """
            Метод, показывающий какие звуки будет издавать питомец
            :return: возвращает звук, характерный для питомца
            """
            return "Unknown sound"


    class Cat(Pets):
        AVERAGE_LIFE_EXPECTANCY = 20

        def __init__(self, name: str, age: int, color: str):
            """
                Создание и подготовка к работе объекта "кошка"
                :param name: имя кошки
                :param age: возраст кошки
                :param color: цвет кошки
            """
            super().__init__(name, age, Cat.AVERAGE_LIFE_EXPECTANCY)
            if not isinstance(color, str):
                raise TypeError
            self.color = color

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self.name!r}, {self.age}, {self.color!r})"

        @staticmethod
        def sound() -> str:
            """
            Метод, показывающий какие звуки будет издавать кошка
            :return: возвращает звук, характерный для кошки
            """
            return "Meow!"


    class Dog(Pets):
        AVERAGE_LIFE_EXPECTANCY = 25

        def __init__(self, name: str, age: int, size: str):
            """
                Создание и подготовка к работе объекта "собака"
                :param name: имя собаки
                :param age: возраст собаки
                :param size: размер собаки
            """
            super().__init__(name, age, Dog.AVERAGE_LIFE_EXPECTANCY)
            if not isinstance(size, str):
                raise TypeError
            self.size = size

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self.name!r}, {self.age}, {self.size!r})"

        @staticmethod
        def sound() -> str:
            """
            Метод, показывающий какие звуки будет издавать собака
            :return: возвращает звук, характерный для собаки
            """
            return "Bark!"
    pass
