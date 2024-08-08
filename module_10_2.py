from time import sleep
from threading import Thread, Lock


class Knight(Thread):
    lock = Lock()  # Создаем lock для синхронизации.

    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        with Knight.lock:
            print(f"{self.name}, на нас напали!")
        while enemies > 0:
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            days += 1
            with Knight.lock:
                print(f"{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.")
            sleep(1)
        with Knight.lock:
            print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
