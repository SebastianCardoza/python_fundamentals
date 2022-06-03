# basico
for i in range (151):
    print(i)

# Multiplo de cinco
for i in range(5,1001,5):
    print(i)

# Contar a lo Dojo
for i in range (1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Es un gran idiota
suma = 0
for i in range(500000):
    if i % 2 == 1:
        suma += i
print(suma)

# Cuenta regresiva de 4
for i in range(2018, 0, -4):
    print(i)

# Contador Flexible
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)