from Profile import *


class DataBase:
    def __init__(self):
        self._database = []

    def show_database(self):
        """Вивід бази даних"""
        count = 1
        print('***** DATA BASE *****')
        if not self._database:
            print('--- ПУСТО ---')

        for length in range(len(self._database)):
            print(f'''--- Person №{count} ---
[Імя]: {self._database[length][0]}
[Прізвище]: {self._database[length][1]}
[Посада]: {self._database[length][2]}
[Прийнятий]: {self._database[length][3]}''')
            if length != len(self._database) - 1:
                print()
            count += 1
        print('**********************\n\n')

    def main_database(self):
        """Базовий набір персон"""
        people1 = Profile()
        people2 = Profile()
        people3 = Profile()
        people4 = Profile()
        people5 = Profile()

        people1.resume('Roma', 'Sarchuk', 'BOSS', 2006)
        people2.resume('Maks', 'Tretak', 'Drawing', 2013)
        people3.resume('Rostik', 'Voichuk', 'SoftDew', 2012)
        people4.resume('Vitalik', 'Matviishyn', 'WedDew', 2014)
        people5.resume('Andriana', 'Marcinovska', 'Marketing', 2010)

        persons = [people1.get_person(), people2.get_person(), people3.get_person(),
                   people4.get_person(), people5.get_person()]
        for i in range(len(persons)):
            self._database.append(persons[i])

    def get_database(self):
        return self._database

    def set_database(self, database):
        self._database = database

    def del_element(self, index):
        if not 0 <= index <= len(self._database)-1:
            raise AttributeError('Неправильний індекс!')
        else:
            del self._database[index]

    def add_profile(self, profile):
        """Додавання нового профіля"""
        self._database.append(profile)
