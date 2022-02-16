from datetime import datetime


class Profile:
    def __init__(self):
        super().__init__()
        self._name = 'None'
        self._surname = 'None'
        self._department = 'None'
        self._year = 0
        self._person = ()

    def resume(self, name='None', surname='None', department='None', year=None):
        """Заповнення даних про персону"""
        # ***** Перевірка NAME *****
        if not isinstance(name, str):
            raise AttributeError('Не коректно ведене ІМЯ!')
        # **************************

        # ***** Перевірка SURNAME *****
        if not isinstance(surname, str):
            raise AttributeError('Не коректно ведене ПРІЗВИЩЕ!')
        # *****************************

        # ***** Перевірка DEPARTMENT *****
        if not isinstance(department, str):
            raise AttributeError('Не коректно ведена ПОСАДА!')
        # ********************************

        # ***** Перевірка YEAR *****
        if isinstance(year, str):
            try:
                year = int(year)
            except ValueError:
                raise ValueError('РІК потрібно вести числом!')
        if not isinstance(self._year, int):
            raise AttributeError('Не коректно ведений РІК!')
        elif not year <= datetime.now().year:
            raise AttributeError('РІК перевищує існуючий!')
        # **************************

        self._name = name
        self._surname = surname
        self._department = department
        self._year = year
        self._person = (self._name, self._surname, self._department, self._year)

    def get_person(self):
        return self._person

    def info(self):
        """Виведення інформації про персону"""
        print(f'''--- Info ---
[Імя]: {self._name}
[Прізвище]: {self._surname}
[Посада]: {self._department}
[Прийнятий]: {self._year}''')
