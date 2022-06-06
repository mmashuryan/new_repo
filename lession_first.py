#первый пункт
name = input("Write your name: ")
print(f"{name} - this is my favorite name!")

my_age = input("Enter your age: ")
mother_age = input("Enter your mom age: ")
print(f"I remembered that you are {my_age} years old and your mom is {mother_age} years old")



#второй пункт
time = int(input("Enter the time in seconds : "))
hours = time // 3600
minutes = time // 60  - hours * 60
second = time % 60
print(f"{hours:02}:{minutes:02}:{second:02}")

#третий
num = input("Enter any number: ")
num_1 = num + num
num_2 = num + num + num
print(f"{num} + {num_1} + {num_2} = {int(num) + int(num_1) + int(num_2)}")

#четвертый
num = int(input("Enter positive intenger: "))
max_num = 0
num_origin = num
while num_origin > 0:
    digit = num_origin % 10
    if digit > max_num:
        max_num = digit
        if max_num == 9:
            break
    num_origin = num_origin // 10
print(f"The largest dinit in a number {num_origin} is {max_num}")


# пятая
revenue = float(input("Введите сумму выручки в у.е. "))
costs = float(input("Введите итог по издержкам в у.е."))
total = revenue - costs
if total > 0:
     print(f"Ура! Вы получили прибыль в {total} у.е.")
     print(f"Рентабельность выручки {100 * (total / costs):.1f}%")
     num_of_pers = int(input("Сколько сотрудников у вас работает в компании?"))
     print(f"Если разделить выручку на всех сотрудников, то каждый получит {total / num_of_pers:2f} у.е.")
elif total < 0:
    print(f" К сожалению, ваш убыток составил {-total} у.е.")
else:
    print(f"плохой результат - хороший опыт")

#   шестое
    while True:
        days = 1
        start = float(input("Стартовый результат: "))
        finish = float(input("Финальный результат: "))
        if start <= 0 or finish < 0:
            print("Результаты не могут быть меньше нуля. Стартовый результат != 0.")
        else:
            while start < finish:
                start += start * 0.1
                days = days + 1
            print(f"Спортсмен добьется результат за {days} дней")
            break
            
