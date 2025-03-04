import threading
import time

class LibrarySystem:
    def __init__(self, Z, Y):
        self.Z = Z  # Количество книг
        self.Y = Y  # Количество читателей
        self.lock = threading.Lock()  # Блокировка для писателей
        self.readers_lock = threading.Lock()  # Блокировка для учёта читателей
        self.books_lock = threading.Lock()  # Блокировка для управления доступом к книгам

        self.readers = [0] * Y  # Счётчики прочитанных книг каждым читателем
        self.books_written = [False] * Z  # Какие книги написаны
        self.books_in_reading = [False] * Z  # Какие книги читаются сейчас
        self.books_written_count = 0  # Количество написанных книг
        self.books_read_count = 0  # Количество прочитанных книг

    def read(self, reader_id):
        read_books = 0  # Счётчик прочитанных книг для текущего читателя
        while True:
            with self.books_lock:
                for i in range(self.Z):
                    if self.books_written[i] and not self.books_in_reading[i]:  # Выбираем доступную книгу
                        self.books_in_reading[i] = True  # Помечаем книгу как читаемую
                        break
                else:
                    continue  # Если нет доступных книг, пробуем снова

            print(f"Читатель {reader_id} читает книгу {i + 1}")
            time.sleep(1)  # Имитация чтения
            print(f"Читатель {reader_id} закончил книгу {i + 1}")

            with self.books_lock:
                self.books_read_count += 1  # Увеличиваем общее количество прочитанных книг
                self.readers[reader_id] += 1  # Увеличиваем счётчик прочитанных книг для текущего читателя
                self.books_in_reading[i] = False  # Освобождаем книгу

            read_books += 1
            if read_books >= self.Z:  # Читатель может прочитать все книги
                break  # Прерываем цикл, если все книги прочитаны

    def write(self, writer_id):
        # Метод для писателей
        with self.lock:
            # Писатель пишет свою книгу
            book_id = writer_id  # Так как у нас одинаковое количество писателей и книг, каждый писатель пишет свою книгу
            if not self.books_written[book_id]:  # Если книга ещё не написана
                print(f"Писатель {writer_id} пишет книгу {book_id + 1}")
                time.sleep(2)  # Имитация написания книги
                self.books_written[book_id] = True  # Отметим книгу как написанную
                self.books_written_count += 1  # Увеличиваем количество написанных книг
                print(f"Писатель {writer_id} завершил книгу {book_id + 1}")