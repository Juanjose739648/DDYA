def numero_pos_neg(num):
    if num > 0:
        print("Tu numero (",num,") es positivo")

    elif num < 0:
        print("Tu numero (",num,") es negativo")

    elif num == 0:
        print("Tu numero (",num,") es cero")


def numero_par_imp(num):
    if num % 2 == 0:
        print("Tu numero (",num,") es par")

    else:
        print("Tu numero (",num,") es impar")


def fibonacci(num):
    a = 0
    b = 1

    while a < num:
        a, b = b, a + b

    if a == num:
        print("El numero pertenece a la serie de Fibonacci")

    else:
        print("El numero no pertenece a la serie de Fibonacci")


def numero_primo(num):
    contador = 0
    divisor = 1

    while divisor <= num:
        if num % divisor == 0:
            contador = contador + 1

        divisor = divisor + 1

    if contador == 2:
        print("El numero es primo")

    else:
        print("El numero no es primo")


def sumar_intermedios(num1, num2):
    suma = 0

    if num1 < num2:
        numero = num1 + 1

        while numero < num2:
            suma = suma + numero
            numero = numero + 1

    else:
        numero = num2 + 1

        while numero < num1:
            suma = suma + numero
            numero = numero + 1

    print("La suma de los numeros intermedios es:",suma)


def cuadrado_cubo(num):
    if num % 2 == 0:
        resultado = num * num * num
        print("Como es par, elevado al cubo es:",resultado)

    else:
        resultado = num * num
        print("Como es impar, elevado al cuadrado es:",resultado)


def fecha_estudiante(codigo):
    dia = codigo[0]

    mes = ""

    if codigo[1] == "e":
        mes = "enero"

    elif codigo[1] == "f":
        mes = "febrero"

    elif codigo[1] == "m":
        mes = "marzo"

    elif codigo[1] == "a":
        mes = "abril"

    print("Mes de nacimiento:",mes)


def vocales_consonantes(mes):
    vocales = 0
    consonantes = 0

    # no pude hacer este profe


def posicion_alfabeto(letra):
    if letra == "a":
        print("La letra esta en la posicion 1")

    elif letra == "b":
        print("La letra esta en la posicion 2")

    # no pude hacer este profe


def main():
    num = int(input("Ingrese un numero: "))

    numero_par_imp(num)
    numero_pos_neg(num)
    fibonacci(num)
    numero_primo(num)
    cuadrado_cubo(num)

    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    sumar_intermedios(num1, num2)

    codigo = input("Ingrese la fecha y codigo del estudiante: ")

    fecha_estudiante(codigo)


main()
