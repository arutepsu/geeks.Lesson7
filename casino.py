from random import randint
from decouple import config


class Casino:
    def __init__(self):
        self.__start_balance = config('MY_MONEY', default=0, cast=int)
        self.__numbers = list(range(1, 31))

    @property
    def numbers(self):
        return self.__numbers

    @property
    def start_balance(self):
        return self.__start_balance

    @start_balance.setter
    def start_balance(self, value):
        self.__start_balance = value

    def play_casino(self, number, bet):
        rand_int = randint(1, 30)
        print(f'The number was: {rand_int}')
        if rand_int == number:
            self.start_balance += bet
            print(f'You won! Your current balance is: {self.start_balance}')
        else:
            self.start_balance -= bet
            print(f'You lose! Your current balance is: {self.start_balance}')



if __name__ == '__main__':
    Casino = Casino()
    Casino.play_casino(2, 300)
