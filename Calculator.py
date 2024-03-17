def show_calc_info():
    print(f"Здарова петух, это калькулятор!\n")


def get_calc_actions():
    list_actions = ["+", "-", "*", "/", "//", "%", "**"]
    print("Введи первое число.")
    first_number = int(input("Ввод: "))

    print("Выбери действие.")
    action = input("Ввод: ")

    if action in list_actions:
        print("Введи второе число: ")

    else:
        print("ЕБЛАН, ТАКОГО ДЕЙСТВИЯ НЕТ В МАТЕМАТИКЕ!")

    second_number = int(input("Ввод: "))

    print(f"{first_number} {action} {second_number}")


def main():
    show_calc_info()
    get_calc_actions()


if __name__ == "__main__":
    main()
