
def multiplicacion (n1,n2):
    return n1*n2

def suma(n1, n2):
    return n1 + n2
def dividir(num,div):
    return num/div 
def menu_principal():
    try:
        operacion = int(input("Ingrese el numero de operacion "))
        valor1 = int(input("Ingrese el primer valor "))
        valor2 = int(input("Ingrese el segundo valor "))
    except ValueError:
        print("No se ingreso un numero")
        return

    match operacion:
        case 1:
            resultado = sumar(valor1, valor2)
        case 2:
            resultado = restar(valor1, valor2)
        case 3:
            resultado = multiplicar(valor1, valor2)
        case 4:
            try:
                resultado= (dividir(valor1,valor2))
            except ZeroDivisionError:
                print("Trataste de dividir entre cero ")
            resultado = dividir(valor1, valor2)
        case 5:
            resultado = potencia(valor1, valor2)
        case 6:
            resultado = raiz(valor1, valor2)
        case 7:
            resultado = logaritmo(valor1, valor2)
        case _:
            resultado = "Operacion invalida"

    print(resultado)
