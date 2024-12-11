numbers = [int(i) for i in input().split()]

n = int(input())

numbers = numbers[n:-n]

numbers.sort()
print("Максимум:", numbers[-1])
print("Минимум:", numbers[0])