import threading
import time
from library import LibrarySystem
from readers import Reader
from writers import Writer

def main():
    Z = 5  # Количество книг
    X = 5  # Количество писателей
    Y = 4  # Количество читателей

    library = LibrarySystem(Z, Y)

    threads = []

    # Создание и запуск потоков для писателей
    for i in range(X):
        writer = threading.Thread(target=library.write, args=(i,))
        threads.append(writer)

    # Создание и запуск потоков для читателей
    for i in range(Y):
        reader = threading.Thread(target=library.read, args=(i,))
        threads.append(reader)

    # Запуск всех потоков
    for t in threads:
        t.start()

    # Ожидание завершения всех потоков
    for t in threads:
        t.join()

    print(f"Все книги были написаны: {library.books_written_count}/{Z}")
    for i in range(Y):
        print(f"Читатель {i} прочитал {library.readers[i]} книг")
    print(f"Всего: {library.books_read_count}/{Z * Y}")

if __name__ == "__main__":
    main()