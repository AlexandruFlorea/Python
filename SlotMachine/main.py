import random


MAX_LINES = 3
MIN_BET = 1
MAX_BET = 1000

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
}

last_bet = 0
last_bet_lines = 0
balance = 0
last_deposit = 0

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copy of the list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # only removes the first instance of the value, so we don't pick it again
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')

        print()  # this just moves to the next line


def deposit():
    global balance
    while True:
        amount = input('How much would you like to deposit: $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number instead.')

    balance += amount

    print(f'last deposit inside deposit function: {last_deposit}')
    print(f'balance inside deposit function: {balance}')

    return amount


def get_number_of_lines():
    global last_bet_lines
    while True:
        lines = input(f'How many lines would you like to bet on (1-{str(MAX_LINES)})? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                last_bet_lines = lines
                break
            else:
                print('Enter a valid number of lines.')
        else:
            print('Enter a number instead.')

    return lines


def get_bet():
    global last_bet
    while True:
        amount = input('How much would you like to bet on each line: $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Total bet amount must be between ${MIN_BET} and ${MAX_BET}.')
        else:
            print('Please enter a number instead.')

    last_bet = amount

    return amount


def spin(balance):
    global last_deposit
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is ${balance}. ')
            answer = input('Enter "y" to recharge. ')
            if answer.lower() == 'y':
                balance += deposit()
                print(f'balance inside spin: {balance}')
        else:
            break

    print(f'You are betting ${bet} on {lines} lines. Total bet = ${total_bet}.')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}, on lines: ', *winning_lines)

    return balance + winnings - total_bet


def main():
    global balance
    print(f'global balance: {balance}')
    print(f'global last_bet: {last_bet}')
    print(f'global last_bet_lines: {last_bet_lines}')
    spin_count = 0
    balance += deposit()
    while True:
        print(f'global balance: {balance}')
        print(f'global last_bet: {last_bet}')
        print(f'global last_bet_lines: {last_bet_lines}')
        print(f'Current balance is ${balance}')
        if spin_count > 0:
            answer = input('Press Enter to play, S to play the same amount or Q to quit.')
            if answer == 'q':
                break
            elif answer == 's':
                pass
        else:
            answer = input('Press Enter to play or Q to quit.')
            if answer == 'q':
                break

        balance += spin(balance)
        spin_count += 1

    print(f'You left with ${balance}.')


main()
