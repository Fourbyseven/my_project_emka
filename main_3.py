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



