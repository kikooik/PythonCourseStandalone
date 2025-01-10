r = []
while n := input():
    if n == "":
        break
    else:
        p = float(input())
    r.append((n, p))

best_runner = r[0]
for runner in r:
    if best_runner[1] < runner[1]:
        best_runner = best_runner
    elif best_runner[1] > runner[1]:
        best_runner = runner
        
print(f"Победитель: {best_runner[0]}")
print(f"Время: {best_runner[1]} минут")