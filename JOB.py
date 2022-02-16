# from Profile import *
from DataBase import *
from Action import *


def main():
    database = DataBase()
    database.main_database()
    action = Action(database)
    run = True
    while run:
        run = action.action()


if __name__ == '__main__':
    main()
