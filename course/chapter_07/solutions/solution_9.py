grade = []

while n := input():
    if n == "":
        break
    else:
        grade.append(int(n))
        
grade.sort()
print("Минимальная оценка:", grade[0])
print("Максимальная оценка:", grade[-1])
print("Отсортированные оценки:", grade)