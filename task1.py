# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Chair:
    def init(self, max_weight: float, legs_count: int):
        """
        Создание и подготовка к работе объекта "Стул"

        :param max_weight: Максимально допустимая нагрузка на стул (кг)
        :param legs_count: Количество ножек у стула

        Примеры:
        >>> chair = Chair(120, 4)
        """
        if not isinstance(max_weight, (int, float)):
            raise TypeError("Максимальная нагрузка должна быть числом")
        if max_weight <= 0:
            raise ValueError("Максимальная нагрузка должна быть положительной")

        if not isinstance(legs_count, int):
            raise TypeError("Количество ножек должно быть целым числом")
        if legs_count < 3:
            raise ValueError("У стула должно быть минимум 3 ножки")

        self.max_weight = max_weight
        self.legs_count = legs_count

    def can_sit(self, weight: float) -> bool:
        """
        Проверка, можно ли сесть на стул с заданным весом.

        :param weight: Вес человека
        :return: True, если вес допустим, иначе False

        Примеры:
        >>> chair = Chair(120, 4)
        >>> chair.can_sit(80)
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть числом")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным")
        ...

    def break_leg(self) -> None:
        """
        Поломка одной ножки стула.

        :raise ValueError: Если ножек меньше 3

        Примеры:
        >>> chair = Chair(120, 4)
        >>> chair.break_leg()
        """
        ...

    def is_stable(self) -> bool:
        """
        Проверка устойчивости стула.

        :return: True, если стул устойчив

        Примеры:
        >>> chair = Chair(120, 4)
        >>> chair.is_stable()
        """
        ...

    class Fork:
        def init(self, prongs_count: int, material: str):
            """
            Создание и подготовка к работе объекта "Вилка"

            :param prongs_count: Количество зубцов вилки
            :param material: Материал вилки

            Примеры:
            >>> fork = Fork(4, "steel")
            """
            if not isinstance(prongs_count, int):
                raise TypeError("Количество зубцов должно быть целым числом")
            if prongs_count <= 0:
                raise ValueError("Количество зубцов должно быть положительным")

            if not isinstance(material, str):
                raise TypeError("Материал должен быть строкой")

            self.prongs_count = prongs_count
            self.material = material

        def stab_food(self, force: float) -> bool:
            """
            Прокалывание пищи вилкой.

            :param force: Сила нажатия
            :return: Удалось ли проколоть пищу

            Примеры:
            >>> fork = Fork(4, "steel")
            >>> fork.stab_food(5.0)
            """
            if not isinstance(force, (int, float)):
                raise TypeError("Сила должна быть числом")
            if force <= 0:
                raise ValueError("Сила должна быть положительной")
            ...

        def clean_fork(self) -> None:
            """
            Очистка вилки после использования.

            Примеры:
            >>> fork = Fork(4, "steel")
            >>> fork.clean_fork()
            """
            ...

        def is_safe(self) -> bool:
            """
            Проверка безопасности вилки.

            :return: True, если вилка безопасна для использования

            Примеры:
            >>> fork = Fork(4, "steel")
            >>> fork.is_safe()
            """
            ...

        class VacuumCleaner:
            def init(self, power: float, dust_capacity: float):
                """
                Создание и подготовка к работе объекта "Пылесос"

                :param power: Мощность пылесоса (Вт)
                :param dust_capacity: Максимальный объем пылесборника (л)

                Примеры:
                >>> vacuum = VacuumCleaner(1600, 3.5)
                """
                if not isinstance(power, (int, float)):
                    raise TypeError("Мощность должна быть числом")
                if power <= 0:
                    raise ValueError("Мощность должна быть положительной")

                if not isinstance(dust_capacity, (int, float)):
                    raise TypeError("Объем пылесборника должен быть числом")
                if dust_capacity <= 0:
                    raise ValueError("Объем пылесборника должен быть положительным")

                self.power = power
                self.dust_capacity = dust_capacity
                self.current_dust = 0.0

            def turn_on(self) -> None:
                """
                Включение пылесоса.

                Примеры:
                >>> vacuum = VacuumCleaner(1600, 3.5)
                >>> vacuum.turn_on()
                """
                ...

            def clean(self, dust: float) -> None:
                """
                Уборка пыли пылесосом.

                :param dust: Объем собираемой пыли (л)

                :raise ValueError: Если объем пыли превышает свободное место в пылесборнике

                Примеры:
                >>> vacuum = VacuumCleaner(1600, 3.5)
                >>> vacuum.clean(1.0)
                """
                if not isinstance(dust, (int, float)):
                    raise TypeError("Объем пыли должен быть числом")
                if dust < 0:
                    raise ValueError("Объем пыли не может быть отрицательным")
                ...

            def empty_dust_container(self) -> None:
                """
                Очистка пылесборника.

                Примеры:
                >>> vacuum = VacuumCleaner(1600, 3.5)
                >>> vacuum.empty_dust_container()
                """
                ...
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
