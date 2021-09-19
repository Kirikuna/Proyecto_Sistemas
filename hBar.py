class HBar:
    def __init__(self, image_original, image_aux, row, col, gray) -> None:
        self.original = image_original
        self.aux = image_aux
        self.row = row
        self.col = col
        self.gray = gray
    
    def erosion(self):
        for i in range(0, self.row ):
            for j in range(0, self.col - 1):
                min = self.original[i][j]
                l = []
                l.append(min)
                l.append(self.original[i][j+1])
                for k in l:
                    if k[0] < min[0]:
                        min = k
                self.aux[i][j] = min
        print("Retocado con exito")
        self._write_pgm("erosion")

    def dilatation(self):
        for i in range(0, self.row ):
            for j in range(0, self.col - 1):
                high = self.original[i][j]
                l = []
                l.append(high)
                l.append(self.original[i][j+1])
                for k in l:
                    if k[0] > high[0]:
                        high = k
                self.aux[i][j] = high
        print("Retocado con exito")
        self._write_pgm("dilatacion")

    def _write_pgm(self, operation) -> None:
        file = open("imgNueva_hbar_"+operation+".pgm", "wb")
        file.write(bytes("P5\n", 'utf-8'))
        file.write(bytes("# Creado por Manuel Valenzuela (2021)\n", 'utf-8'))
        string = str(self.col) + " " + str(self.row) + "\n"
        file.write(bytes(string, 'utf-8'))
        string = str(self.gray) + "\n"
        file.write(bytes(string, 'utf-8'))
        for i in range(0, self.row):
            for j in self.aux[i]:
                file.write(j)
        print("Creado con exito")
        file.close()
