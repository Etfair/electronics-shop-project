from src.item import Item


class Phone(Item):
    """
    Создаём новый класс, наследуемый от Item
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Возвращает название, цену, количество товара и количество сим-карт
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim):
        """
        сеттер для проверки количества сим-карт и условий для ValueError
        """
        if sim > 0:
            self.__number_of_sim = sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
