things = []

while n := input():
    if n == "":
        break
    else:
        things.append(n)
        
if "Палатка" not in things:
    print("Вы не взяли палатку!")
    
print(len(things))