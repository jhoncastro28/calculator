def suma(a, b):
    return a + b
def resta(a, b):
    return a - b

def calculadora():
    print("Calculadora Básica")
    print("1. Suma")
    print("2. Resta")
    
    opcion = input("Elige una opción (1/2): ")
    
    if opcion in ('1', '2'):
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion == '1':
                print("Resultado:", suma(num1, num2))
            if opcion == '2':
                print("Resultado:", resta(num1, num2))
        except ValueError:
            print("Error: Ingresa valores numéricos válidos")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    calculadora()