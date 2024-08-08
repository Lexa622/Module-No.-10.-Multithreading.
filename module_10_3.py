from random import randint
from time import sleep
from threading import Thread, Lock


class Bank(Thread):
    lock = Lock()
    balance = 0

    def __init__(self):
        Thread.__init__(self)

    def deposit(self):
        for _ in range(100):
            a = randint(50, 500)
            self.balance += a
            print(f"Пополнение: {a}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            a = randint(50, 500)
            print(f"Запрос на {a}")
            if a <= self.balance:
                self.balance -= a
                print(f"Снятие: {a}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')