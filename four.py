#первое
from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty character.")

salary()

#второе

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)

#третье
multiples = [el for el in range(2,241) if el % 20 == 0 or el % 21 ==0]
print(multiples)

#четвертое
my_list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq = [el for el in my_list_1 if my_list_1.count(el) == 1]
print(uniq)

#пятое
from  functools import reduce

def my_list_3(el_1, el_2):
    return el_1 * el_2
multiples_1 = [el for el in range(100, 1001, 2)]
print(multiples_1)


#шестое
from  itertools import count, cycle

puk_1 = count(7)
puk_2 = cycle ("PUK")
for _ in range(3):
    print("(puk_1, puk_2) = ({},{})".format(next(puk_1), next(puk_2)))


 #седьмое
def fact_gen(cucumber):
     my_num = 1
     for i in range(cucumber + 1):
         yield f'{i}! = {my_num}'
         my_num *= i + 1

for el in fact_gen(int(input('факториал номер:  '))):
    print(el)