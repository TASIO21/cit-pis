import threading
import time
class Writer:
    def init(self, library, writer_id):
        self.library = library
        self.writer_id = writer_id
    def write(self):
        for _ in range(self.library.Z):
            self.library.write(self.writer_id)
            time.sleep(2)