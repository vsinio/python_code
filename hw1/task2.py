'''Напишите программу для. проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''

print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z)) == (not x or not y or not z):
                print("Утверждение истинно")