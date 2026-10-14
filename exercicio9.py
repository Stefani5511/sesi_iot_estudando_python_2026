x = int(input("Digite o primeiro lado do triângulo: "))
y = int(input("Digite o segundo lado do triângulo: "))
z = int(input("Digite o terceiro lado do triângulo: "))

if x + y <= z or x + z <= y or y + z <= x:
    print("Os lados não formam um triângulo")
elif x == y and y == z:
    print("O triângulo é equilátero")
elif x == y or x == z or y == z:
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno") 