from Profile import *


class Action:
    def __init__(self, database):
        self._database = database
        self._profile = Profile()
        action_user = '0'

    def __action_add(self):
        print('----- ADD -----')
        while True:
            try:
                name = str(input('Імя: '))
                surname = str(input('Прізвище: '))
                department = str(input('Посада: '))
                year = str(input('Прийнятий: '))
                self._profile.resume(name, surname, department, year)
                break
            except (AttributeError, ValueError) as er:
                print(er)
                print()
        self._database.add_profile(self._profile.get_person())
        print('---------------\n')

    def __help(self):
        number = 1
        data = self._database.get_database()
        for i in range(len(data)):
            print()
            print(f'№{number} :: {data[i]}')
            number += 1
        print()

    def __action_del(self):
        print('----- DEL -----')
        while True:
            print('Ведіть номер персони!')
            print('PS: ? -> HELP')
            action_user = str(input('>>> ')).lower()
            if action_user == '?' or action_user == 'help':
                self.__help()
                continue

            try:
                action_user = int(action_user)
            except ValueError:
                print('! Номер потрібно вести числом !')
            try:
                self._database.del_element(action_user-1)
            except ValueError:
                print('! Номер повинен відповідати персоні !')

            print('Done...')
            break
        print('---------------\n')

    def action(self):
        print('''|===== Оберіть дію =====|
    1) Додати персону
    2) Переглянути базу персон
    3) Видалити персону
    4) Вийти''')
        while True:
            action_user = str(input('>>> '))
            if action_user == '1' or action_user == '1)':       # Add
                self.__action_add()

            elif action_user == '2' or action_user == '2)':     # Show
                self._database.show_database()

            elif action_user == '3' or action_user == '3)':     # Del
                self.__action_del()

            elif action_user == '4' or action_user == '4)':     # Exit
                print('OK, goodbye...')
                return False

            else:
                print('! Ведіть числом ; Наприклад: 1 чи 1) !')
                continue
            return True
