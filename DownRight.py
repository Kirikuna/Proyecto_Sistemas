from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import logging
class DownRight:
    def __init__(self, image_original, image_aux, row, col, gray, max_thread, image_name) -> None:
        logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
        self.original = image_original
        self.aux = image_aux
        self.row = row
        self.col = col
        self.gray = gray
        self._max_thread = max_thread
        self.image_name = image_name[:len(image_name) - 4]

    def execute(self, algorithm):
        name = ''
        with ThreadPoolExecutor(max_workers=self._max_thread) as executor:
            if algorithm == 1:
                for i in range(1, self.row):
                    executor.submit(self._erode, i)
                name = 'erosion'
            elif algorithm == 2:
                for i in range(1, self.row):
                    executor.submit(self._dilatation, i)
                name = 'dilatacion'
        self._write_pgm(name)

    def _erode(self, row) -> None:
        # logging.info(f'Ejecutando erosion {row}')
        for j in range(1, self.col - 1):
            l = []
            l.append(self.original[row][j])
            l.append(self.original[row + 1][j])
            l.append(self.original[row][j + 1])
            self.aux[row][j] = min(l)

    def _dilatation(self, row) -> None:
        # logging.info(f'Ejecutando dilatacion {row}')
        for j in range(1, self.col - 1):
            l = []
            l.append(self.original[row][j])
            l.append(self.original[row + 1][j])
            l.append(self.original[row][j + 1])
            self.aux[row][j] = max(l)

    def _write_pgm(self, operation) -> None:
        file = open(self.image_name + "LHorizontal" + operation + ".pgm", "wb")
        file.write(bytes("P5\n", 'utf-8'))
        file.write(bytes("# Creado por Andrés Wallberg (2021)\n", 'utf-8'))
        string = str(self.col) + " " + str(self.row) + "\n"
        file.write(bytes(string, 'utf-8'))
        string = str(self.gray) + "\n"
        file.write(bytes(string, 'utf-8'))
        for i in range(0, self.row):
            for j in self.aux[i]:
                file.write(j)
        print("Creado con exito")
        file.close()

