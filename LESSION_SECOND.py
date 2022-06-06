
    # первое
my_list = [ (7+8j), "abrocadabra", 2, 45.3, True, None, {11: 8, 98: 9}, [56,56]]
for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")

    # второе
num_list = list(input("Enter number without space: "))
for i in range(1, len(num_list), 2):
    num_list.insert(i - 1, num_list.pop(i))
print(num_list)

    #третья
month_list = int(input("Enter any month from 1 to 12: "))
month_dicr = {"весна": [3, 4, 5], "лето": [6, 7, 8],"осень": [9, 10, 11],"зима": [12, 2, 1]}
if month_list in sum(month_dicr.values(), []):
    for i in month_dicr.items():
        if month_list in i[1]:
            print(i[0])
            break

    #четвертая
word_list = input("Напишите несколько слов используя пробел: ").split()
for i, word in enumerate(word_list, 1):
    print(f"{i}) {word[:15]}")

    #пятая
my_list_1 = [7, 5, 3, 3, 2]
while True:
    number = input("Напишите одно натуральное число: ")
    if number.isdigit():
        my_list_1.append(float(number))
        my_list_1.sort(reverse=True)
        print(my_list_1)
    elif number == "q":
        break
