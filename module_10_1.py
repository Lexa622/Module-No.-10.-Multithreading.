from time import sleep
from datetime import datetime
from threading import Thread


def wite_words(word_count, file_name):  # word_count - количество слов, file_name - куда будут записываться слова
    file = open(file_name, "a", encoding="utf-8")   # открываем файл для записи
    for i in range(word_count):  # цикл количества записей
        file.write(f"Какое-то слово № {i + 1}\n")   # записываем пронумерованное слово с переносом
        sleep(0.1)  # задержка в десятую секунды
    file.close()    # закрываем файл
    print(f"Завершилась запись в файл {file_name}")    # вывдим в консоль запись


time_start = datetime.now()     # засекаем время
wite_words(10, "example1.txt")      # передаём данные в функцию
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
time_end = datetime.now()     # отсечка времени
time_res = time_end - time_start    # получаем время работы кода
print(f"Работа потоков {time_res}")    # выводим время в консоль
time_start = datetime.now()     # засекаем новое время
thr_first = Thread(target=wite_words, args=(10, "example5.txt"))    # создаём потоки
thr_second = Thread(target=wite_words, args=(30, "example6.txt"))
thr_third = Thread(target=wite_words, args=(200, "example7.txt"))
thr_fourth = Thread(target=wite_words, args=(100, "example8.txt"))
thr_first.start()   # запускаем потоки
thr_second.start()
thr_third.start()
thr_fourth.start()
thr_first.join()    # останавливаем выполнение программы до завершения работы потоков
thr_second.join()
thr_third.join()
thr_fourth.join()
time_end = datetime.now()   # отсечка времени
time_res = time_end - time_start    # получаем время работы потоков
print(f"Работа потоков {time_res}")     # выводим время в консоль
