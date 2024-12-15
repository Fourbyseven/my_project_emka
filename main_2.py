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


# n = int(input("Введите количество чисел Фибоначчи, которые хотите увидеть: "))

# if n <= 0:
#     print("Пожалуйста, введите положительное число.")
# else:

#     fibonacci = [0, 1]
    

#     if n == 1:
#         fibonacci = [0]
    

#     for i in range(2, n):
#         next_number = fibonacci[-1] + fibonacci[-2]
#         fibonacci.append(next_number)
    

#     print(f"Первые {n} чисел Фибоначчи: {fibonacci}")

#Фибоначчи



#10

# translations = {
#     "cat": "кот",
#     "dog":  "собака",
#     "house": "дом",
# }

# while True:
#     print("\n Выберите действие:    ")
#     print("1 - Запросить перевод")
#     print("2 - Добавить новое слово")
#     print("3 - Выйти из программы")
#     choice = input("Ваш выбор  (1/2/3): ")

#     if choice == "1":
#         word = input("Введите слово для перевода:   ").strip().lower()
#         translations = translations.get(word)
#         if translations:
#             print(f"Перевод слова '{word}':     {translations}")
#         else:
#             print(f"Слово '{word}' не найдено в словаре.")

#     elif choice == "2":
#         new_word = input("Введитек новое слово на английском:   ").strip().lower()
#         if new_word in translations:
#             print(f"Слово '{new_word}' уже есть в словаре с переводом:  {translations[new_word]}")

#         else:
#             new_translation = input("Введите перевод этого слова:   ").strip().lower()
#             translations[new_word] = new_translation
#             print(f"Слово '{new_word}' с переводом '{new_translation}' добавлено в словарь")

#     elif choice == "3":
#         print("Выход из программы. До всидания")
#         break

#     else:
#         print("Неверный выбор. Попробуйте снова.")







