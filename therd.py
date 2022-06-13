#первое задание
def first_func(var_1, var_2):
    try:
        var_1, var_2 = int(var_1), int(var_2)
        num_total = var_1 / var_2
        return round(num_total, 2)
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
            return "Нельзя делить на ноль!"
print(first_func(input("Введите делимое число: "), input("Введите делитель: ")))


#второе
def second_func(str_2, str_1, str_3, str_4, str_5, str_6):
    return f"имя - {str_1}; фамилия - {str_2}; дата рождения - {str_3}; " \
           f"город проживания - {str_4}; почта  - {str_5}; номер телефона - {str_6}"
print(second_func(str_1="Иван", str_2="Иванов", str_3="19.01.1998", str_4="Москва",
                  str_5="ivanov@yandex.ru", str_6="79190000000"))

#третье
my_func = lambda puk_1, puk_2, puk_3: (puk_1 + puk_2 + puk_3) - min(puk_1, puk_2, puk_3)
print(my_func(8,7,9))


#четвертое
def mega_func(x, y):
    try:
        total = x ** y
    except TypeError:
        return "Введи целое положительное"
    return total
print(mega_func(2, -2))


#пятое
def sum_num():
    s = 0
    while True:
        err = False
        in_list = input("введите числа через пробел, если хотите выйти введите '5' ").split()
        for pin in in_list:
            if pin.lower() == "5":
                return s
            else:
                try:
                    s += int(pin)
                except ValueError:
                    err = True
        if err:
            print("некорретная числа")
        print(f"сумма чисел = {s}")

print(sum_num())

#шестое
def int_func():
    for word in input ("Введите слова с пробелами в нижнем регистре на латинице):\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} только нижний регистр на латинице!")
int_func()