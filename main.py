# Код написан 01.11.2023
# Автор: Кучук Милан Михайлович
print("\t\tПрограмма Кучук")
print("Распеределение очков навыков в дереве\n")

points = 30
force = 0
health = 0
brain = 0
agility = 0
choice = ""
while choice != 0:
    print(
        """
        Выюор действий
        0 - Выход
        1 - Выбор очков
        2 - Убрать очки
        3 - Сброс всех очков
        """
        )
    print("Кол-во поинтов - ", points)
    print("force - ", force)
    print("health - ", health)
    print("brain - ", brain)
    print("agility - ", agility)
    choice = int(input("Что вы хотите сделать?\n"))
    if choice == 0:
        print("Вы вышли в меню")
    elif choice == 1:
        free = int(input("Сколько поинтов вы хотите потратить?"))
        while free > points:
            print("У вас всего лишь ", points, " свободных поинтов")
            free = int(input("Сколько поинтов вы хотите потратить?"))
        print(
        """
        0 - Выход
        1 - force
        2 - health
        3 - brain
        4 - agility
        """
        )
        choice2 = int(input("Куда хотите потратить очки?"))
        if choice2 == 0:
            print("Вы вышли в меню")
        elif choice2 == 1:
            force += free
            points -= free
        elif choice2 == 2:
            health += free
            points -= free
        elif choice2 == 3:
            brain += free
            points -= free
        elif choice2 == 4:
            agility += free
            points -= free
        else:
            print("Вы вышли в меню")
    elif choice == 2:
        print(
        """
        0 - Выход
        1 - force
        2 - health
        3 - brain
        4 - agility
        """
        )
        choice2 = int(input("Где вы хотите забрать поинты?"))
        if choice2 == 0:
            print("Вы вышли в меню")
        elif choice2 == 1:
            while free <= force:
                free = int(input("Сколько поинтов вы хотите забрать?"))
                force -= free
                points += free
                break
        elif choice2 == 2:
            while free <= health:
                free = int(input("Сколько поинтов вы хотите забрать?"))
                health -= free
                points += free
                break
        elif choice2 == 3:
            while free <= brain:
                free = int(input("Сколько поинтов вы хотите забрать?"))
                brain -= free
                points += free
                break
        elif choice2 == 4:
            while free <= agility:
                free = int(input("Сколько поинтов вы хотите забрать?"))
                agility -= free
                points += free
                break
        else:
            print("Вы вышли в меню")
    elif choice == 3:
        points = 30
        force = 0
        health = 0
        brain = 0
        agility = 0
    else:
        print("Вы сделали что-то не так, попробуйте снова")
