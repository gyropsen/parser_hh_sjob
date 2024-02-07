class Vacancy:
    def __init__(self, _id_: int = None, profession: str = None, address: str = None, currency: str = None,
                 client_name: str = None, link: str = None, payment_from: int = None, payment_to: int = None):
        self._id_ = _id_
        self.profession = profession
        self.address = address
        self.currency = currency
        self.client_name = client_name
        self.link = link

        self.payment_from = int(payment_from)
        self.payment_to = int(payment_to) if payment_to else self.payment_from
        self.average_payment = self.payment_to + self.payment_from / 2

        self.verification()

    def verification(self):
        for key, value in self.__dict__.items():
            if value is None:
                raise ValueError(f"Не указана информация по вакансии: {key}")

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
