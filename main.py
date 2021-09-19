import cruz
import logging
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

if __name__ == "__main__":
    file = open("imgNueva.pgm", "rb")
    image = file.readline().decode()
    if image[0] != 'P' or image[1] != '5':
        print("Fichero equivocado")
        file.close()
        exit()
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

    #out = open("matriz.txt", "w")
    #out.write(str(image_original))
    #out.close()
    #print(image_original)
    structuring = cruz.Cruz(image_original, image_aux, row, col, gray)
    structuring.erode(1, row)

    file.close()