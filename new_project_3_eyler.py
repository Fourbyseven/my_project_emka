#   3   6 7 8 9 1 11 12 13 14 15 16 17 18 19 20


# 2 : 1 2
# 3 : 1 3
# 4 : 1 2 4
# 5 : 1 5
# 6 : 1 2 3 6
# 7 : 1 7
# 8 : 1 2 4 8
# 9 : 1 3 9
# 10 : 1 2 5 10
# 11 : 1 11
# 12 : 1 2 3 4 6 12
# 13 : 1 13
# 14 : 1 2 7 14
# 15 : 1 3 5 15
# 16 : 1 2 4 8 16
# 17 : 1 17
# 18 : 1 2 3 6 9 18
# 19 : 1 19
# 20 : 1 2 4 5 10 20

# i = 215125

lst = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def print_dividers(n: int) -> None:
    for i in range(1, n+1):
        print(i, end=" : ")
        for j in range(1, i +1):
            if i % j == 0:
                print(j , end=" ")
        print()            

def solution(n:  int) -> int: # Анотация типов !
    i = n
    while True:
        for j in lst:
            if i % j != 0:
                break
            if j == n:
                return i
        i +=n
        if i % 1_000_000 ==0:
            print(f"{i = }")
            # print(f"i = {i}")             


if __name__ == "__main__":
    print(f"Результат:  {solution(20)}")
    # print_dividers(40)
    # print(", ".join("11 12 13 14 15 16 17 18 19 20".split(" ")))
























