                    #Мини проекты python 
#1. Калькулятор

# while True:
#     input_1 = int(input("Введите первое число:     "))
#     input_2 = int(input("Введите второе число:      "))
#     input_orerations = input("Введите операцию(+, -, *, /) или 'q' для выхода:          ")

#     if input_orerations == 'q':
#         print("Выход из программы")
#         break

#     if input_orerations == '+':
#         result = input_1 + input_2
#     elif input_orerations == '-':
#         result = input_1 - input_2
#     elif input_orerations == '*':
#         result = input_1 * input_2
#     elif input_orerations == '/':
#         if input_2 == 0:
#             print("Ошибка:  Деления на ноль невозможно.")
#             continue
#         result = input_1 / input_2
#     else:
#         print("Неверная операйция попобуйтеснова.")
#         continue


#     print(f"Результат:        {result}")




#2. Генератор Случайных паролей 
# import random
# import string

# def generate_password(lenght):
#     if lenght < 4:
#         print("Пароль не корректный он должен быть из чисел хотя-бы 4")
#         return None
    
#     all_characters = string.ascii_letters, string.digits, string.punctuation

#     password = [
#         random.choice(string.ascii_lowercase),
#         random.choice(string.ascii_uppercase),
#         random.choice(string.digits),
#         random.choice(string.punctuation)
#     ]
#     password += random.choices(all_characters, k=lenght -4)

#     random.shuffle(password)

#     return ''.join(password)

# lenght = int(input("Введите пароль:     "))
# password = generate_password(lenght)

# if password:
#     print(f"Сгенерируемый пароль:       {password}")




#3. Конвертер температуры


# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def fahrenheit_to_celcius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# while True:
#     print("\n Конвертер температуры")
#     print("1. Цельсий -> Фаренгейт")
#     print("2. Фаренгейт -> Цельсий")
#     print("3. Выход")

#     choice = input("Выберите действие (1/2/3):  ")

#     if choice == '1':
#         celcius = float(input("Введите температуру в градусах Цельсия:  "))
#         fahrenheit = celsius_to_fahrenheit(celcius)
#         print(f"{celcius}*C = {fahrenheit:.2f}*F")
#     elif choice == '2':
#         fahrenheit = float(input("Введите температуру в градусах Фаренгейта:        "))
#         celcius = fahrenheit_to_celcius(fahrenheit)
#         print(f"{fahrenheit}*F = {celcius:.2f}*C")
#     elif choice == '3':
#         print("Выход из программы. До свидания!")
#         break
#     else:
#         print("Неккоректный выбор, попробуйтк снова.")



# 4 Угадай число

# from random import randint # Импортируем из random функцию randint - которая сделает рандомные целые числа

# secret_number = randint(1,100) # В этом переменном будет храниться радномное число 
# print("Угадай число от 1, 100") # Делаем условия для пользователя 

# user_number = 0 # Подготавливаем переменную для цикла с которым мы будем писать числа для угадания
# try_count = 0   # Подготавливаем переменную для цикла  который будет как поссдедовательность идти типо 1-попытка, 2-попытка. 

# while user_number != secret_number: # Цикл если user_number != secret_number, короче говоря если у этих обоих  циклах числа не будут похожи друг на друга то цикл будет продолжаться как True
#     try:
#         try_count += 1 # Добавляем 1, через каждую когда цикл будет вращаться try_count  будет добавлен + 1
#         user_number = int(input(f"{try_count}-я попытка:    ")) # input для пользователя с помощью это input пользоваетель будет гадать число, try_count это попытка после каждой неудачной угадки это будет расти
#         if user_number < 1 or user_number> 100:
#             print("Число должен быть в диапозоне от 1 до 100. Попробуй еше раз.")
#             continue
        
#         if user_number > secret_number: # Если  user_number > secret_number то к пользователю будет выведенно много за что и пользователь может  примерно угадать
#             print("Много")
        
#         elif user_number < secret_number: # Если  user_number > secret_number то к пользователю будет выведенно мало за что и пользователь может  примерно угадать
#             print("Мало")
        
#         else:
#             print(f"Ура вы угадали число:       {secret_number}") # Финал если пользовател угадал число то будет выведен этот print
#     except ValueError:
#         print("Пожайлуста, вводите только числа, А не слова")





#5 Счетчик слов 



# while True:
#     str_input = input("Введите ваше слово (q-выход):      ")
#     if str_input == 'q':
#         print("досвидания")
#         break
#     num_chars = len(str_input)
#     num_words = len(str_input.split())

#     print(f"Количество символов:       {num_chars}")
#     print(f"Количество слов:        {num_words}")



#6)     Таблица Умнажения

# while True:
#     number = int(input("Введите число для таблицы умнажения:        "))
#     print(f"Ваше число для умнажения:       {number}")

#     for n in range(1, 11):
#         result = number * n
#         print(f"{number} x {n} = {result}")




#7) Четные и нечетные числа:

# while True: 
#     numbers = list(map(int, input("Введите числа через пробел:  ").split()))
#     even_numbers = []
#     odd_numbers = []

#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)

#     print(F"Четные числа:       {even_numbers}")
#     print(f"НЕчетные числа:     {odd_numbers}")

#     my_выход = input("Хотите ли продолжить да/нет:      ")
#     if my_выход == 'да':
#         continue
#     else:
#         print("Досвидания:  ")
#         break


# четные числа  -  even numbers
# нечетные числа -  odd numbers




# 8 Простые числа :


# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#         return True

# start = int(input("Введите начало диапозона:    "))
# end = int(input("Введите конец диапозона:   "))

# prime_numbers = []
# for num in range(start, end + 1):
#     if is_prime(num):
#         prime_numbers.append(num)
# print(f"Простые числа в диапозоне от {start} до end:    {prime_numbers}")


# 9 Обратный порядок слов


# while True:

#         my_input = input("Введите вашу предложения  (q-выход):     ")
#         if my_input == 'q':
#             print("Досвидания ")
#             break
#         my_num = "".join(my_input.split()[::-1])
#         print(f"Строка в обратном порядке:    {my_num}")






#10 Фибоначчи

# while True:
#     try:
#         limit = input("Введите максимальное число для последовательности Фибоначчи (q-выход)")
#         if limit.lower() == 'q':
#             print("До свидания !")
#             break

#         limit = int(limit)
#         if limit < 0:
#             print("Введите положительносе число.")
#             continue

#         fibonacci_sequence = [0, 1]
#         while True:
#             next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#             if next_number > limit:
#                 break
#             fibonacci_sequence.append(next_number)

#             print(f"Посследовательность Фибоначчи до {limit}: {fibonacci_sequence}")
#     except ValueError:
#             print("Введите корректное целое число.")    



# Последовательность Фибоначчи — это числовая последовательность, где каждое число является суммой двух предыдущих. Она начинается с двух первых чисел, которые обычно равны 0 и 1 (хотя иногда используют начало с 1 и 1).






