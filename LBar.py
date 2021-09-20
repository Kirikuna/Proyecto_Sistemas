from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import logging

class LBar:
    def __init__(self, image_original, image_aux, row, col, gray, max_thread) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
        self.original = image_original
        self.aux = image_aux
        self.row = row
        self.col = col
        self.gray = gray
        self.mutex = Lock()
        self._max_thread = max_thread

    def execute(self, algorithm):
        name = ''
        if algorithm == 1:
            with ThreadPoolExecutor(max_workers=self._max_thread) as executor:
                for i in range(1, self.row):
                    executor.submit(self._erosion, i)
            name = 'erosion'
        elif algorithm == 2:
            with ThreadPoolExecutor(max_workers=self._max_thread) as executor:
                for i in range(1, self.row):
                    executor.submit(self._dilatation, i)
            name = 'dilatacion'
        self._write_pgm(name)
    
    def _erosion(self, i):
        for j in range(0, self.col - 1):
            pixel_estudio_min = self.original[i][j]
            l = []
            l.append(pixel_estudio_min)
            l.append(self.original[i][j+1])
            l.append(self.original[i+1][j])
            self.aux[i][j] = min(l)
        

    def _dilatation(self, i):
        for j in range(0, self.col - 1):
            pixel_estudio_max = self.original[i][j]
            l = []
            l.append(pixel_estudio_max)
            l.append(self.original[i][j+1])
            l.append(self.original[i+1][j])
            self.aux[i][j] = max(l)

    def _write_pgm(self, operation) -> None:
        file = open("imgNueva_Lbar_"+operation+".pgm", "wb")
        file.write(bytes("P5\n", 'utf-8'))
        file.write(bytes("# Creado por Hugo Castro (2021)\n", 'utf-8'))
        string = str(self.col) + " " + str(self.row) + "\n"
        file.write(bytes(string, 'utf-8'))
        string = str(self.gray) + "\n"
        file.write(bytes(string, 'utf-8'))
        for i in range(0, self.row):
            for j in self.aux[i]:
                file.write(j)
        print("Creado con exito")
        file.close()