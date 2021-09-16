class Cruz:
    def __init__(self, image_original, image_aux, row, col, gray) -> None:
        self.original = image_original
        self.aux = image_aux
        self.row = row
        self.col = col
        self.gray = gray
    
    def erode(self, min_row, max_row)  -> None:
        for i in range(1, self.row-1):
            for j in range(1, self.col-1):
                min = self.original[i][j-1]
                l = []
                l.append(min)
                l.append(self.original[i-1][j])
                l.append(self.original[i][j])
                l.append(self.original[i][j+1])
                l.append(self.original[i+1][j])
                for k in l:
                    if (k[0] < min[0]):
                        min = k
                self.aux[i][j] = min
        print("Retocado con exito")
        self._write_pgm("erosion")

    def dilatation(self, row, col) -> None: 
        pass

    def _write_pgm(self, operation) -> None:
        file = open("imgNueva_"+operation+".pgm", "wb")
        file.write(bytes("P5\n", 'utf-8'))
        file.write(bytes("# Creado por Nicolas Castillo (2021)\n", 'utf-8'))
        string = str(self.row) + " " + str(self.col) + "\n"
        file.write(bytes(string, 'utf-8'))
        string = str(self.gray) + "\n"
        file.write(bytes(string, 'utf-8'))
        for i in range(0, self.row):
            for j in self.aux[i]:
                file.write(j)
        print("Creado con exito")
        file.close()

