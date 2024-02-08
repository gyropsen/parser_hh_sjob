class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, _id_: int = None, profession: str = None, requirement: str = None, address: str = None, currency: str = None,
                 client_name: str = None, link_client: str = None, link: str = None, payment_from: int = None,
                 payment_to: int = None):

        # Инициализируем класс и верифицируем
        self._id_ = _id_
        self.profession = profession
        self.requirement = requirement
        self.address = address
        self.currency = currency
        self.client_name = client_name
        self.link_client = link_client
        self.link = link
        self.payment_from = payment_from
        self.payment_to = payment_to
        self.average_payment = 0
        self.verification()

        # Если верификация удалась, значит можно рассчитать среднюю зп
        self.change_average_payment()

    def change_average_payment(self):
        """
        Бывает, что у вакансии указана зп "по договоренности" или нет окончательной суммы,
        тогда проверяем значения payment... и считаем среднюю зп
        :return:
        """
        if self.payment_from == 0:
            self.average_payment = "По договоренности"
        elif self.payment_to == 0:
            self.average_payment = self.payment_from
        else:
            self.average_payment = (self.payment_to + self.payment_from) / 2

    def verification(self):
        """
        Верификация класса
        :return:
        """
        for key, value in self.__dict__.items():
            if value is None:
                raise ValueError(f"Не указана информация по вакансии: {key}")
        return True

    def __gt__(self, other):
        return self.average_payment > other.average_payment

    def __ge__(self, other):
        return self.average_payment >= other.average_payment

    def __lt__(self, other):
        return self.average_payment < other.average_payment

    def __le__(self, other):
        return self.average_payment <= other.average_payment

    def __eq__(self, other):
        return self.average_payment == other.average_payment


if __name__ == '__main__':
    vacancy = Vacancy()
