from casino import Casino


def start_game():
    casino = Casino()
    play = True
    while play:
        try:
            number = int(input('Enter number: '))
            if number not in casino.numbers:
                print('Please enter a number between 1 and 30.')
                continue
            bet = int(input('Enter bet: '))
            if bet <= 0:
                print('Wrong bet. Please enter right bet.')
                continue
            if bet > casino.start_balance:
                print('Wrong bet. Pleas enter the bet <= then your balance')
                continue
            casino.play_casino(number, bet)
        except ValueError:
            print('Wrong data type! Please enter ints for number and bet.')

        if casino.start_balance <= 0:
            print('Game over!')
            break

        answer = input('Would you like to play more? (y/n): ')
        if answer == 'n':
            break
        elif answer == 'y':
            continue
        else:
            print('wrong answer!!!')
            break


if __name__ == "__main__":
    start_game()
