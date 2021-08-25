def decor(f):
    def slash():
        print("////////////////////////////////////////////////////")
        f()
        print("////////////////////////////////////////////////////")
    return slash
def npi():
    d2 = int(input("POR FAVOR INTRODUCE EL NÚMERO DE DECIMALES QUE VA A TENER PI \."))
    if d2 == 1:
        PI = 3.1
        return PI
    elif d2 == 2:
        PI = 3.14
        return PI
    elif d2 == 3:
        PI = 3.141
        return PI
    elif d2 == 4:
        PI = 3.1415
        return PI
    elif d2 == 5:
        PI = 3.14159
        return PI
    elif d2 == 6:
        PI = 3.141592
    elif d2 == 7:
        PI = 3.1415926
        return PI
    elif d2 == 8:
        PI = 3.14159265
        return PI
@decor
def print_bienvenidos():
    print("BIENVENIDO AL PROGRAMA CALCULADORA_PENDULOSIMPLE!!!")
x = print_bienvenidos()
input()
print("ESTE PROGRAMA SIRVE PARA CALCULAR EL MOVIMIENTO DE UN PÉNDULO")
print("RECUERDA QUE LA ECUACIÓN ES T=(2*PI*(l)^(1/2))/((g)^(1/2))")
input()
print("PON TUS DECIMALES CON UN PUNTO")
input()
print("ESTE PROGRAMA TIENE LA CAPACIDAD PARA CALCULAR PI CON HASTA 8 DE SUS DECIMALES")
input()
d1 = input("POR FAVOR INTRODUCE LA VARIABLE QUE QUIERES QUE SE CALCULE: T, l o g \.")
if d1 == "g":
    l = float(input("POR FAVOR INTRODUCE EL VALOR DE l (RECUERDA QUE SE DEBE INTRODUCIR EN METROS) \."))
    T = float(input("POR FAVOR INTRODUCE EL VALOR DE T \."))
    PI = npi()
    g = (((2*PI)**2)*l)/(T**2)
    print(g)
    if 8.86<g>8.88:
        if g == 8.87:
            print("TU PÉNDULO ESTÁ EN VENUS")
        else:
            print("TU PÉNDULO ESTÁ EN UN PLANETA PARECIDO A VENUS")
    elif 9.8<g>9.82:
        if g == 9.81:
            print("TU PÉNDULO ESTÁ EN LA TIERRA :)")
        else:
            print("TU PÉNDULO ESTÁ EN UN PLANETA PARECIDO A LA TIERRA")
    elif 3.7<g>3.72:
        if g == 3.71:
            print("TU PÉNDULO ESTÁ EN MARTE")
        elif g == 3.7:
            print("TU PÉNDULO ESTÁ EN MERCURIO")
        elif 3.7<g>3.72:
            print("TU PÉNDULO ESTÁ EN UN PLANETA PARECIDO A MARTE Y A MERCURIO")
    elif 24.78<g>24.80:
        if g == 24.79:
            print("TU PÉNDULO ESTÁ EN JÚPITER")
        else:
            print("TU PÉNDULO ESTÁ EN UN PLANETA PARECIDO A JÚPITER")
    elif 9<g>9.1:
        if g == 9.1:
            print("TU PÉNDULO ESTÁ EN SATURNO")
        else:
            print("TU PÉNDULO ESTÁ EN UN PLANETA PARECIDO A SATURNO")
    elif 7.7<g>7.9:
        if g == 7.8:
            print("TU PÉNDULO ESTÁ EN URANO")
        else:
            print("TU PÉNDULO ESTÁ EN UN PLANETA PARECIDO A URANO")
    elif 1.61<g>1.63:
        if g == 1.62:
            print("TU PÉNDULO ESTÁ EN LA LUNA")
        else:
            print("TU PÉNDULO ESTÁ EN UN CUERPO CELESTE PARECIDO A LA LUNA")
elif d1 == "l":
    g = float(input("POR FAVOR INTRODUCE EL VALOR DE g \."))
    T = float(input("POR FAVOR INTRODUCE EL VALOR DE T \."))
    PI = npi()
    l = ((T**2)*g)/((2*PI)**2)
    print(l)
elif d1 == "T":
    g = float(input("POR FAVOR INTRODUCE EL VALOR DE g \."))
    l = float(input("POR FAVOR INTRODUCE EL VALOR DE l (RECUERDA QUE SE DEBE INTRODUCIR EN METROS) \."))
    PI = npi()
    T = (2*PI*(l)**(1/2))/((g)**(1/2))
    print(T)
input()
def y(f):
    def decora():
        print("/////////////////////////////////////////////////")
        f()
        print("/////////////////////////////////////////////////")
    return decora
@y
def print_final():
    print("MUCHAS GRACIAS POR USAR ESTE PROYECTO CIENTÍFICO")
print_final()
input()