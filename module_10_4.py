from threading import Thread
from random import randint
from time import sleep
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        i = 0
        for guest in guests:
            i += 1
            for table in tables:
                if table.guest is None:
                    table.guest = Guest(guest.name)
                    table.guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            if i > len(tables):
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        tg = True
        j = 0
        while not self.queue.empty() or tg:
            for table in tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest.start()
                    if table.guest is None:
                        j += 1
                    if j >= len(tables):
                        tg = False


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
