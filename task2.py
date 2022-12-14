# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('enter x: '))
y = int(input('enter y: '))
z = int(input('enter z: '))
if (not (x or y or z) == (not x and not y and not z)):
    print('true')
else:
    print('false')
