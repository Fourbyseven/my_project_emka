
from time import perf_counter

def get_time_deco(func):
    def wrap_it():
        start_time  = perf_counter()
        func()
        end_time = perf_counter()
        print(f"\nВРЕМЯ ВЫПОЛНЕНИЯ ПРОГРАММЫ:     {end_time - start_time:.4f}")

    return wrap_it



