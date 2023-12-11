import doctest


class Iphone:
    def __init__(self, models_num: int, memory: int, size: str):
        """
           Создание и подготовка к работе объекта "айфон"
           :param models_num: номер модели
           :param memory: объем памяти
           :param size: размер телефона

           Примеры:
           >>> iphone = Iphone(13, 128, "simple")
           """
        if not isinstance(models_num, int):
            raise TypeError("Номер модели айфона должен быть целым числом")
        if models_num <= 0:
            raise ValueError("Номер модели айфона должен быть больше нуля")
        self.models_num = models_num
        if not isinstance(memory, int):
            raise TypeError("Объем памяти айфона должен быть целым числом")
        if memory <= 0:
            raise ValueError("Объем памяти айфона должен быть больше нуля")
        self.memory = memory
        if not isinstance(size, str):
            raise TypeError("Размер айфона может быть: Max и Simple")
        if size.upper() != "MAX" and size.upper() != "SIMPLE":
            raise ValueError("Размер айфона может быть только Max и Simple")
        self.size = size

    def amount_memory_to_updating(self) -> float:
        """
        Функция, которая проверяет, сколько свободной памяти необходимо
        для каждого обновления телефона

        :param self:
        :return: количество памяти
        Примеры:
        >>> iphone = Iphone(13, 128, "simple")
        >>> iphone.amount_memory_to_updating()
        12.8
        """
        mem_for_updating = float((self.memory/100)*10)
        return mem_for_updating

    def remaining_memory(self, volume: float) -> float:
        """
        Остаток памяти, после заполнения
        :param self:
        :param volume:
        :return: остаток памяти
        Примеры:
        >>> iphone = Iphone(13, 128, "simple")
        >>> iphone.remaining_memory(12.0)
        116.0
        """
        if not isinstance(volume, float):
            raise TypeError("Занять можно только число памяти ")
        if volume < 0:
            raise ValueError("Занимаемая память должна быть больше нуля")
        remainder = self.memory-volume
        if remainder < 0:
            raise ValueError("Памяти недостаточно")
        return remainder

    def integrity_check(self) -> bool:
        """
        Проверка на существования такой версии айфона
        :param self:
        :return: True или False
        Примеры:
        >>> iphone = Iphone(13, 128, "simple")
        >>> iphone.integrity_check()
        True
        """
        if self.models_num > 15 or self.models_num == 9:
            return False
        else:
            return True


class Notebook:
    def __init__(self, num_of_pages: int, pattern: str):
        """
        Создание и подготовка к работе объекта "Тетрадь"
        :param num_of_pages: количество страниц
        :param pattern: разлиновка тетради

        Примеры:
        >>> notebook = Notebook(15, "линия")
        """
        if not isinstance(num_of_pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if num_of_pages < 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self.num_of_pages = num_of_pages
        if not isinstance(pattern, str):
            raise TypeError("Узор страницы должен быть str")
        if pattern.upper() != "КЛЕТКА" and pattern.upper() != "ЛИНИЯ":
            raise ValueError("Узор страницы может быть либо 'клетка', либо 'линия'")

    def removing_sheets(self, num: int) -> int:
        """
        Функция возвращает колчиество оствшихся лситов после удаления
        :param num: вырванные листы
        :return: количество оставшихся листов
        >>> notebook = Notebook(15, "линия")
        >>> notebook.removing_sheets(10)
        """
        ...

    def total_nums(self, text_volume: int) -> int:
        """
        Функция возвращает сколько тетрадей, схожих с объектом необходимо
        использовать, чтобы разместить там текст данного объема
        :param text_volume: объем текста в страницах
        :return: количество тетрадей
        >>> notebook = Notebook(15, "линия")
        >>> notebook.total_nums(29)
        """
        ...


class Kettle:
    def __init__(self, volume: int, speed: int, life_time: float):
        """
        Создание и подготовка объекта "Чайник"
        :param volume: объем чайника
        :param speed: скорость закипания чайника
        :param life_time: срок службы чайника

        Примеры:
        >>> kettle = Kettle(3, 10, 5.5)
        """
        if not isinstance(volume, int):
            raise TypeError("Объем чайника задается целым числом")
        if volume < 0:
            raise ValueError("Объем чайника должен быть больше 0")
        self.volume = volume
        if not isinstance(speed, int):
            raise TypeError("Скорость закипания чайника задается целым числом")
        if speed < 0:
            raise ValueError("Скорость закипания чайника должна быть больше 0")
        self.speed = speed
        if not isinstance(life_time, float):
            raise TypeError("Срок службы чайника задается числом")
        if life_time < 0:
            raise ValueError("Срок службы чайника должен быть больше 0")
        self.life_time = life_time

    def pour_water(self, desired_volume: int) -> bool:
        """
        Функция возвращет True, если желаемый объем уместится в чайник и False,
        если не уместится
        :param desired_volume: желаемый объем воды, который надо уместить
        :return: можно ли уместить эту воду в чайнике
        >>> kettle = Kettle (3, 10, 5.5)
        >>> kettle.pour_water(1)
        """
        ...

    def required_speed(self, flooded_water: int, the_rest_of_time: int) -> bool:
        """
        Функция проверяет успеет или чайник закипеть за необходимое время
        :param flooded_water: залитый объем воды
        :param the_rest_of_time: остаток времени за который нужно успеть
        :return: успеет ли чайник закипеть за отведенное время
        >>> kettle = Kettle(3, 10, 5.5)
        >>> kettle.required_speed(2, 10)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
