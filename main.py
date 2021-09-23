from cruzD import CruzD
from cruz import Cruz
from hBar import HBar
from LBar import LBar
from DownRight import DownRight
from UpDown import UpDown

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

def createPGM(filename, comment, row, col, gray, m_img):
    file = open(filename, "wb")
    file.write(bytes("P5\n", 'utf-8'))
    file.write(bytes(comment, 'utf-8'))
    string = str(col) + " " + str(row) + "\n"
    file.write(bytes(string, 'utf-8'))
    string = str(gray) + "\n"
    file.write(bytes(string, 'utf-8'))
    for i in m_img:
        for j in i:
            file.write(j)
    print("Creado con exito")
    file.close()

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
    while op3 !=1 and op3 != 2 and op3 != 3 and op3 != 4 and op3 != 5 and op3 != 6:
        print('ELEMENTO ESTRUCTURANTE')
        print('1- Cruz')
        print('2- Cruz diagonal')
        print('3- Barra horizontal')
        print('4- Tipo L')
        print('5- Barra vertical')
        print('6- Tipo L horizontal')
        op3 = int(input('Opción: '))
        print()

        if op3 !=1 and op3 != 2 and op3 != 3 and op3 != 4 and op3 != 5 and op3 != 6:
            print('Opción no válida') 

    structuring = None
    comment = ''
    if op3 == 1:
        structuring = Cruz(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)
        comment = '# Creado por Nicolas Castillo (2021)\n'

    elif op3 == 2:
        structuring = CruzD(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)
        comment = '# Creado por Nicolas Castillo (2021)\n'

    elif op3 == 3:
        structuring = HBar(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)
        comment = '# Creado por Manuel Valenzuela (2021)\n'
    
    elif op3 == 4:
        structuring = LBar(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)
        comment = '# Creado por Hugo Castro (2021)\n'
    
    elif op3 == 5:
        structuring = UpDown(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)
        comment = '# Creado por Andrés Wallberg (2021)\n'
    
    elif op3 == 6:
        structuring = DownRight(image_original, image_aux, row, col, gray, op1, image_name)
        structuring.execute(op2)
        comment = '# Creado por Andrés Wallberg (2021)\n'

    createPGM(structuring.file_name, comment, row, col, gray, structuring.aux)




    