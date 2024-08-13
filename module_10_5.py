from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    file = open(name, "r")
    while True:
        string_f = file.readline()
        all_data += string_f
        if string_f == "":
            break
    file.close()


filenames = [f'file {number}.txt' for number in range(1, 5)]

# Линейный вызов
time_start_l = datetime.now()     # засекаем время
for filename in filenames:
    read_info(filename)
time_end_l = datetime.now()     # отсечка времени
print(f"Время выполнения {time_end_l - time_start_l} (Линейный вызов)")    # выводим время в консоль

# Многопроцессный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        time_start = datetime.now()  # засекаем время
        pool.map(read_info, filenames)
    time_end = datetime.now()     # отсечка времени
    print(f"Время выполнения {time_end - time_start} (Многопроцессный вызов)")    # выводим время в консоль
