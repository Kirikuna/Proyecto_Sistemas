from x import X
from cruz import Cruz
from hBar import HBar
from LBar import LBar

def open_img(filename):
    file = open(filename, "rb")
    image = file.readline().decode()
    if image[0] != 'P' or image[1] != '5':
        print("Fichero equivocado")
        file.close()
        exit(0)
    file.readline()
    dimension = file.readline().decode().split()
    col = int(dimension[0]) 
    row = int(dimension[1])
    gray = int(file.readline().decode())

    print(row, " ", col, "\n", gray)
    image_original = []
    image_aux = []

    for i in range(0, row):
        image_original.append([])
        image_aux.append([])
        for j in range(0, col):
            c = file.read(1)
            image_original[i].append(c)
            image_aux[i].append(c)
    file.close()
    return image_original, image_aux, row, col, gray
   
if __name__ == '__main__':
    image_name = input("Nombre/url de imagen: ")
    try:
        image_original, image_aux, row, col, gray = open_img(image_name)
    except FileNotFoundError:
        print("No existe el archivo")
        exit()

    op1 = 0
    while op1 !=1 and op1 != 2:
        print('PROCESAMIENTO DE IMÁGENES PGM')
        print('1- Secuencial')
        print('2- Paralelo')
        op1 = int(input('Opción: '))
        print()
        
        if op1 !=1 and op1 != 2:
            print('Opción no válida') 

    if op1 == 2:
        op1 = 8

    op2 = 0
    while op2 !=1 and op2 != 2:
        print('TIPO DE ALGORITMO')
        print('1- Erosión')
        print('2- Dilatación')
        op2 = int(input('Opción: '))
        print()

        if op2 !=1 and op2 != 2:
            print('Opción no válida') 

    op3 = 0
    while op3 !=1 and op3 != 2 and op3 != 3 and op3 != 4:
        print('ELEMENTO ESTRUCTURANTE')
        print('1- Cruz')
        print('2- Cruz diagonal')
        print('3- Barra horizontal')
        print('4- Tipo L')
        op3 = int(input('Opción: '))
        print()

        if op3 !=1 and op3 != 2 and op3 != 3 and op3 != 4:
            print('Opción no válida') 

    if op3 == 1:
        structuring = Cruz(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)

    elif op3 == 2:
        structuring = X(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)

    elif op3 == 3:
        structuring = HBar(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)
    
    elif op3 == 4:
        structuring = LBar(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)



    