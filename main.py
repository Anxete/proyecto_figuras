from lib import cuadrado, triangulo
print("proyecto figuras")
print(cuadrado.get_identificador())
lado = 4
print(f"El area de un {cuadrado.get_identificador()} de lado {lado} es: {cuadrado.get_area(lado)} y el perímetro es {cuadrado.get_perimetro()}")

base = 4
altura = 2
print(triangulo.get_identificador())
print(f"El area de un {triangulo.get_identificador()} de base {base} es: {triangulo.get_area(base, altura)} y el perímetro es {cuadrado.get_perimetro(base, base, base)}")