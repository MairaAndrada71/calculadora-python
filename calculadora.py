def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b

def main():
    print("Calculadora en Python")
    print("Opciones disponibles: sumar, restar, multiplicar, dividir")
    
    operacion = input("Elige una operación: ").lower()

    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Por favor, ingresa solo números válidos.")
        return

    if operacion == "sumar":
        print("Resultado:", sumar(a, b))
    elif operacion == "restar":
        print("Resultado:", restar(a, b))
    elif operacion == "multiplicar":
        print("Resultado:", multiplicar(a, b))
    elif operacion == "dividir":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()
