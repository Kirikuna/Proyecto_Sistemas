from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import logging
class Cruz:
    def __init__(self, image_original, image_aux, row, col, gray) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
        self.original = image_original
        self.aux = image_aux
        self.row = row
        self.col = col
        self.gray = gray
        self.mutex = Lock()
        self._max_thread = 8
    
    def execute(self, algorithm):
        name = ''
        if algorithm == 1:
            with ThreadPoolExecutor(max_workers=self._max_thread) as executor:
                for i in range(1, self.row-1):
                    executor.submit(self._erode, i)
            name = 'erosion'
        elif algorithm == 2:
            with ThreadPoolExecutor(max_workers=self._max_thread) as executor:
                for i in range(1, self.row-1):
                    executor.submit(self._dilatation, i)
            name = 'dilatacion'
        self._write_pgm(name)
        
    
    def _erode(self, row)  -> None:
        logging.info(f'Ejecutando erosion {row}')
        for j in range(1, self.col-1):
            min = self.original[row][j-1]
            l = []
            l.append(min)
            l.append(self.original[row-1][j])
            l.append(self.original[row][j])
            l.append(self.original[row][j+1])
            l.append(self.original[row+1][j])
            for k in l:
                if (k[0] < min[0]):
                    min = k
            self.mutex.acquire(1)
            self.aux[row][j] = min
            self.mutex.release()

    def _dilatation(self, row) -> None: 
        logging.info(f'Ejecutando dilatacion {row}')
        for j in range(1, self.col-1):
            max = self.original[row][j-1]
            l = []
            l.append(max)
            l.append(self.original[row-1][j])
            l.append(self.original[row][j])
            l.append(self.original[row][j+1])
            l.append(self.original[row+1][j])
            for k in l:
                if (k[0] > max[0]):
                    max = k
            self.mutex.acquire(1)
            self.aux[row][j] = max
            self.mutex.release()

    def _write_pgm(self, operation) -> None:
        file = open("imgNueva_"+operation+".pgm", "wb")
        file.write(bytes("P5\n", 'utf-8'))
        file.write(bytes("# Creado por Nicolas Castillo (2021)\n", 'utf-8'))
        string = str(self.col) + " " + str(self.row) + "\n"
        file.write(bytes(string, 'utf-8'))
        string = str(self.gray) + "\n"
        file.write(bytes(string, 'utf-8'))
        for i in range(0, self.row):
            for j in self.aux[i]:
                file.write(j)
        print("Creado con exito")
        file.close()

