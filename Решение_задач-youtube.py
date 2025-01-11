#====================== Project Euler ========================




# 1 - Задача:

# from time import perf_counter

# start_time = perf_counter()

# sum = 0

# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i

# print(f"{sum}")


# end_time = perf_counter()

# print(f"Время выполнения Программы :    {end_time - start_time:.4f}")


# Курс  по генераторам: 

#Правильный ответ:      233168
# Списковые включения :      0.00025500
# Выражения генераторов :    0.00020120
# Filter                     0.00049460
# Set без распаковки  :      0.00031680
# Set с распоковкой   :      0.00028800 
# Union Set           :      0.00033420

# from time import perf_counter
# from sys import getsizeof


# start = perf_counter()

# Решение на базе спискового включкения 
# print(sum(l := [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))
# print(getsizeof(l))     #4216 - байт


 
# Решение  на базе обьекта-генератора
# print(sum(a := (i for i in range(1000) if i % 3 ==0 or i % 5 ==0)))
# result = getsizeof(a)
# print(f"Памяти сьеденно:       {result}") #208 - байт



#  Функция filter
# print(sum(filter(lambda x: x % 3 == 0 or x % 5 ==0,  range(1000))))   # <class 'filter'>


# Множества 
# print(sum(set(range(3, 1000, 3)).union(set(range(5, 1000, 5)))))

 







# end  = perf_counter()

# print(f"\nВремя ВЫПОЛНЕНИЯ ПРОГРАММЫ:   {end - start:.8f}")






# Задача: 2


# from get_time_deco import get_time_deco

# @get_time_deco 
# def main():


#     a_1, a_2 = 1, 2
#     sum = 2
#     while(a_2 < 4_000_000):
#         a_1, a_2 = a_2, a_1 + a_2
#         if a_2 % 2 == 0:
#             sum += a_2

#     print(f"СУММА ЧЁТНЫХ ЧИСЕЛ СОСТОВЛЯЕТ:      {sum}")

# if __name__ == "__main__":
#     main()























































# Свой проект по модулям:
# from sys import getsizeof
# from time import perf_counter
# start_num = perf_counter()

# my_num = []

# for n in range(1, 10):
#     if n % 2 == 0:
#         my_num.append(n)

# print(f"Все четные числа:       {my_num}")

# weight_num = getsizeof(my_num)

# print(f"Вес:        {weight_num}-байта")

# end_num = perf_counter()

# print(f"Время Выполнения:       {end_num - start_num:.8f}")








