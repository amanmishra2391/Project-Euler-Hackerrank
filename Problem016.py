for _ in range(int(input())):
    power = int(input())
    value = str(2**power)
    List = list(map(int,value))
    print(sum(List))
