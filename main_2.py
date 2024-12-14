#1

# number = int(input("Введите первое число:       "))
# number_2 = int(input("Введите второе число:         "))
# операция = input("Ввдеит на что хотите сложить(+, -, *, /):           ")

# if операция == "+":
#     num = number + number_2

# elif операция == "-":
#     num = number - number_2

# elif операция == "*":
#     num = number * number_2
    
# elif операция == "/":
#     num = number / number_2

# print(f"Ваша число:     {num}")


    
#2


# Рассмотреть
# year = int(input("Введите год: "))


# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} является високосным годом.")
# else:
#     print(f"{year} не является високосным годом.")







# 3

# my_num = [3, 21, 52, 72, 12, 76, 31]
# my_min_num = min(my_num)
# my_max_num = max(my_num)
# res = f"Минимальное целое число:        {my_min_num},\n \rМаксимальное число:     {my_max_num}"

# print(res)


#4

### Рассмотреть
# user_input = input("Введите строку: ")

# sorted_string = ''.join(sorted(user_input))

# print("Символы строки в алфавитном порядке:", sorted_string)



#5



# my_product = {"phone":  "300$",
#               "laptop": "500$",
#               "tv":     "1000$"}

# my_input = input(f"Введите ваш товар (например, phone, laptop, tv):      ").lower()
# # .lower() - нижний регистр,  пример(а, б, в)
# # .upper() - верхний регситр, пример(А, Б, В)

# if my_input in my_product:
#     print(f"Ваш товар '{my_input}':     {my_product[my_input]}")

# else:
#     print("Товар не найден")


#6

# my_list_int = [10, 4, 21, 64, 12, 42, 14]


# total_sum  = sum(my_list_int)

# count = len(my_list_int)

# average = total_sum / count

# print("Среднее арефметическое: ", average)



#7

# my_input = input("Введите числа через пробел:       ")

# my_num = list(map(int, my_input.split()))

# my_list = list(set(my_num))
# print("Все уникальные числа:       ", my_list)



#8

# my_input = input("Введите строку:       ")

# my_str = my_input.lower().replace(" ", "")

# if my_str == my_str[::-1]:
#     print("Ваша строка палиндром")
# else:
#     print("Ваша строка не полиндром")

# Палиндром - это слово, фраза, число или любая посследовательность символов, которые читаються одинаково слева направо и справо налево 
# Например:
#как, мадам, тот


#9










#10