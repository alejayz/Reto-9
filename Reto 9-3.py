#Función recursiva para la función potencia
def PotenciaRecursiva(n:int, x:int) -> int:
    if x == 0:
        return 1
    elif x == 1:
        return n
    else:
        return n * PotenciaRecursiva(n, x-1)
    
if __name__ == '__main__':
    n = int(input("ingrese el número base: "))
    x = int(input("ingrese el exponente: "))
    Pot = PotenciaRecursiva(n, x)
    print("la potencia de " + str(n) + " elevado " + str(x) + " es: " + str(Pot))