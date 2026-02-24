class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """
    
    def capitilize(self, string: str) -> str:
        """
        Делает первую букву заглавной, а остальные строчными.
        Пример: `capitilize("skypro")` -> `"Skypro"`
        """
        if not string:
            return string
        return string[0].upper() + string[1:].lower()
    
    def trim(self, string: str) -> str:
        """
        Удаляет пробелы в начале строки.
        Пример: `trim("   sk ypro")` -> `"sk ypro"`
        """
        whitespace = ' '
        while string.startswith(whitespace):
            string = string[1:]
        return string
    
    def to_list(self, string: str, delimiter: str = ",") -> list:
        """
        Преобразует строку в список, используя разделитель.
        Пример: `to_list("a,b,c,d")` -> `["a", "b", "c", "d"]`
        """
        if not string:
            return []
        return string.split(delimiter)
    
    def contains(self, string: str, symbol: str) -> bool:
        """
        Проверяет, содержит ли строка заданный символ.
        Пример: `contains("SkyPro", "S")` -> `True`
        """
        return symbol in string
    
    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все вхождения заданного символа из строки.
        Пример: `delete_symbol("SkyPro", "k")` -> `"SyPro"`
        """
        return string.replace(symbol, "")