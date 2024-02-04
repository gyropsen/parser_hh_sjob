class Vacancy:
    def __init__(self, _id_=None, profession=None, address=None, currency=None,
                 client_name=None, link=None, payment_from=None, payment_to=None):
        self._id_ = _id_
        self.profession = profession
        self.address = address
        self.currency = currency
        self.client_name = client_name
        self.link = link
        self.payment_from = payment_from
        self.payment_to = payment_to
        self.verification()

    def verification(self):
        for key, value in self.__dict__.items():
            if value is None:
                raise ValueError(f"Не указана информация по вакансии: {key}")


if __name__ == '__main__':
    vacancy = Vacancy()
