#De los retos anteriores seleciones 3 funciones y escribalas con argumentos no definidos (*args).
#1
def Prestamo(*args) -> float:
    interes = i / 100
    return c * (1 + interes) ** n

if __name__ == "__main__":
    c = float(input("ingrese valor de préstamo en pesos: "))
    i = float(input("ingrese valor de interés en %: "))
    n = int(input("ingrese número de meses: "))
    ValorPrestamo = Prestamo(c, i, n)
    print("el valor del préstamo por " + str(n) + " meses es de: " + str(ValorPrestamo))
    
#2
import math
def AreaFigura(*args) -> float:
    ARectangulo = a * b
    ACirculos = (math.pi * (r)**2) * 2  # el área se duplica dado que son dos círculos
    return ARectangulo + ACirculos

if __name__ == "__main__":
    a = float(input("ingrese ancho del rectángulo: "))
    b = float(input("ingrese largo del rectángulo: "))
    r = float(input("ingrese el radio del círculo: ")) 
    Area = AreaFigura(a, b, r)
    print("el área de la figura es: " + str(Area))
    
    
#3
import math 
def AreaFigura(*args) -> float:
    ArSupEsfera = 4 * math.pi * (r1**2)
    Hipot = (h**2 + r2**2)**0.5  # formula de la hipotenusa para hallar área superficial
    ArSupCono = (math.pi * r2 * Hipot) + (math.pi * (r2**2))
    return ArSupEsfera + ArSupCono 

if __name__ == "__main__":
    r1 = float(input("ingrese el radio de la esfera: ")) # radio en cm
    r2 = float(input("ingrese el radio del cono: ")) # radio en cm
    h = float(input("ingrese la altura del cono: ")) # altura en cm
    #Volumen = VolumenFigura(r1, r2, h)
    #print("el volumen de la figura es: " + str(Volumen))
    AreaSuperficial= AreaFigura(r1, r2, h)
    print("el área superficial de la figura es: " + str(AreaSuperficial))