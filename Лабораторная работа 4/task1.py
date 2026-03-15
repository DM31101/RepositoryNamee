class Clothing:
    """Базовый класс, описывающий одежду."""

    def __init__(self, brand: str, material: str, price: float) -> None:
        """Инициализация базовых атрибутов и инкапсулированного поля износа."""
        self.brand: str = brand
        self.material: str = material
        self.price: float = price
        self._wear_level: int = 0

    def wear(self) -> str:
        """Метод эксплуатации изделия."""
        self._wear_level += 10
        return f"Вы надели {self.brand}. Текущий износ: {self._wear_level}%."

    def clean(self) -> str:
        """Базовый метод очистки."""
        return "Изделие очищено стандартным способом."

    def __str__(self) -> str:
        """Строковое представление объекта."""
        return f"Одежда {self.brand}"

    def __repr__(self) -> str:
        """Техническое представление объекта."""
        return f"Clothing(brand='{self.brand}', price={self.price})"


class Jeans(Clothing):
    """Дочерний класс, описывающий джинсы."""

    def __init__(self, brand: str, material: str, price: float, size: int) -> None:
        """Расширение конструктора атрибутом размера."""
        super().__init__(brand, material, price)
        self.size: int = size

    def clean(self) -> str:
        """
        Перегрузка метода очистки.
        Обоснование: Джинсовая ткань требует стирки при низкой температуре
        и в вывернутом состоянии для сохранения структуры денима.
        """
        return f"Джинсы {self.brand} размера {self.size} постираны в деликатном режиме."

    def __str__(self) -> str:
        """Перегруженное строковое представление."""
        return f"Джинсы {self.brand}, размер {self.size}"

    def __repr__(self) -> str:
        """Перегруженное техническое представление."""
        return f"Jeans(brand='{self.brand}', size={self.size})"


if __name__ == "__main__":
    my_jeans = Jeans("Levis", "Denim", 5000.0, 32)

    print(my_jeans.wear())
    print(my_jeans.clean())
    print(str(my_jeans))
    print(repr(my_jeans))