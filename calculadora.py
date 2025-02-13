def suma(a, b):
    return a + b

def calculadora():
    print("Calculadora Básica")
    print("1. Suma")

    opcion = input("Elige una opción (1): ")
    
    if opcion in ('1'):
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == '1':
                print("Resultado:", suma(num1, num2))

        except ValueError:
            print("Error: Ingresa valores numéricos válidos")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    calculadora()