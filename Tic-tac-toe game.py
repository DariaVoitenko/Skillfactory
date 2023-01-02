def greet():
    print("%" * 25)
    print("Добро пожаловать в игру")
    print('    "КРЕСТИКИ-НОЛИКИ"  ')
    print("%" * 25)
    print("Правила ввода X Y")
    print("X - номер строки\nY - номер столбца")
    print("-" * 25)


def show():
    print("~" * 15)
    print(" | 0 | 1 | 2 |")
    print("~" * 15)
    for i, j in enumerate(field):
        print(f'{i}| {" | ".join(j)} |')
        print("~" * 15)


# show()


def ask():
    while True:
        coords = input("   Впишите свои координаты:").split()
        if len(coords) != 2:
            print("   Введите две координаты")
            continue
        x, y = coords
        if not(x.isdigit()) and not(y.isdigit()) or (x.isalpha()) or (y.isalpha()):
            print("   Введите числовые показатели!")
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("   Введенные числа выходят за пределы координат")
            continue
        if field[x][y] != " ":
            print("   Клетка уже занята!")
            continue
        return x, y


def check_win():
    win_coords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for crd in win_coords:
        list_ = []
        for c in crd:
            list_.append(field[c[0]][c[1]])
        if list_ == ["X", "X", "X"]:
            print("   Победил крестик!")
            return True
        if list_ == ["0", "0", "0"]:
            print("   Победил нолик")
            return True
    return False


greet()


field = [[" "] * 3 for _ in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("   Ходит крестик")
    else:
        print("   Ходит нолик")
    x, y = ask()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if check_win():
        break
    if count == 9:
        print("   Победила дружба")
        break
