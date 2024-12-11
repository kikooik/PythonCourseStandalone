numbers = [int(i) for i in input().split()]

n = int(input())


l = numbers[::n]

l.sort()
print(l)