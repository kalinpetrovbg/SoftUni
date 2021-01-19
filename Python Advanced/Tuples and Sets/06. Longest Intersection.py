num = int(input())
set_1 = set()
set_2 = set()

for _ in range(num):
    num1, num2 = input().split("-")
    start1, stop1 = [int(x) for x in num1.split(",")]
    start2, stop2 = [int(x) for x in num2.split(",")]

    for x in range(start1, stop1 + 1):
        set_1.add(x)
    for y in range(start2, stop2 + 1):
        set_2.add(y)

print(set_1.intersection(set_2))
