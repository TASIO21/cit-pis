import threading
import time
class Reader:
    def __init__(self, library, reader_id):
        self.library = library
        self.reader_id = reader_id
    def read(self):
        for _ in range(self.library.Z):
            self.library.read(self.reader_id)
            time.sleep(1)