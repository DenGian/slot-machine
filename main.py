import random  # Used to get a random value

NO_NUMBER = "Please enter a number."

MAX_LINES = 3  # global constant that is not going to change - max lines to bet on is now set to 3 - more dynamic program
MAX_BET = 2000  # global constant that is not going to change - max amount to bet is now set to 200
MIN_BET = 1  # global constant that is not going to change - min amount to bet is now set to 10

ROWS = 3  # defining amount of rows
COLS = 3  # defining amount of cols

symbol_count = {  # defining different symbols and the count of set symbols
    "♠︎": 2,  # in this case "♠︎" = the symbol - symbol count = 2
    "♥︎": 4,
    "♦︎": 5,
    "♣︎︎": 6
}

symbol_value = {  # defining the value for each symbol
    "♠︎": 6,  # in this case "♠︎" has the value of x6 multiplier
    "♥︎": 4,
    "♦︎": 3,
    "♣︎︎": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):  # getting all lines
        symbol = columns[0][line]  # symbol to check in first column of the current row - all symbols need to be the same
        for column in columns:  # loop through every single column
            symbol_to_check = column[line]  # the symbol to check is the symbol of the current row
            if symbol != symbol_to_check:  # check if symbols are NOT the same
                break  # if they are NOT the same, break out - check the next line
        else:
            winnings += values[symbol] * bet  # if all symbols are the same, no break out and user won - multiplier symbol * bet of the user (bet of each line)
            winning_lines.append(line + 1)  # +1 because of index, otherwise if line 1 wins it would say line 0

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):  # generating outcome of slot machine symbols - 3 parameters passing through function
    all_symbols = []  # making list for all symbols
    for symbol, symbol_count in symbols.items():  # ".items" gives both key and value of set item
        for _ in range(symbol_count):  # "_" is an anonymous variable - when looping and the count doesn't matter - no unused variables anymore
            all_symbols.append(symbol)  # appending whatever the symbol is

    columns = []  # defining list that contains all the values inside of column
    for _ in range(cols):  # for each of the columns a value needs to be generated
        column = []  # column = empty list
        current_symbols = all_symbols[:]  # ":" = slice-operator - make a copy of the list
        for _ in range(rows):  # for each of the rows a value needs to be generated
            value = random.choice(all_symbols)  # select random values from all_symbols list
            current_symbols.remove(value)  # removes first instance of the list
            column.append(value)  # add value to the column list

        columns.append(column)  # add column to columns list

    return columns

def print_slot_machine(columns):  # transposing
    for row in range(len(columns[0])):  # looping through all rows - defining number of rows based on columns
        for i, column in enumerate(columns):  # for every single row looping through every column
            if i != len(columns) - 1:  # to make sure the | is only printed if there is another value
                print(column[row], end=" | ")  # print value that is at the first row of that column - "end=" default "\n"
            else:
                print(column[row], end="")  # printing value without |
        print()  # empty print statement brings program down to a new line

def  deposit():  # function deposit - responsible for user input
    while True:  # while loop that is set to true - continue to do function until break
        amount = input("What would you like to deposit? $")  # prompt that comes up for user input
        if amount.isdigit():  # checking if input is a number and is a positive amount - first checking necessary because converting to int next step
            amount = int(amount)  # converting input to int - string by default
            if amount > 0:  # checking if amount is greater than 0
                break  # if amount is greater than 0, the loop breaks
            else:  # if amount is NOT greater than 0
                print("Amount must be greater than 0.")  # prompt that shows up on the screen
        else:  # if there was no number given by user
            print(NO_NUMBER)  # prompt that shows up on screen if there was no input by user
    return amount

def get_number_of_lines():
    while True:  # while loop that is set to true - continue to do function until break
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "). ")  # prompt that comes up for user input - string concatenation
        if lines.isdigit():  # checking if input is a number and is a positive amount - first checking necessary because converting to int next step
            lines = int(lines)  # converting input to int - string by default
            if 1 <= lines <= MAX_LINES:  # checking if number of lines is between 1-3
                break  # if lines is between 1-3, the loop breaks
            else:  # if amount is NOT between 1-3
                print("Enter a valid number of lines.")  # prompt that shows up on the screen
        else:  # if there was NO input given by user
            print(NO_NUMBER)  # prompt that shows up on screen
    return lines

def get_bet():
    while True:  # while loop that is set to true - continue to do function until break
        amount = input("What would you like to bet on each line? $")  # prompt that comes up for user input
        if amount.isdigit():  # checking if input is a number and is a positive amount - first checking necessary because converting to int next step
            amount = int(amount)  # converting input to int - string by default
            if MIN_BET <= amount <= MAX_BET:  # checking if amount is between the MIN_BET and MAX_BET
                break  # if amount is between the MIN_BET and MAX_BET, the loop breaks
            else:  # if amount is NOT between the MIN_BET and MAX_BET
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")  # Using f-string - You can write any variable in {...} and it will automatically be converted to a string (if it can be converted)
        else:  # if there was no number given by user
            print(NO_NUMBER)  # prompt that shows up on screen for the user
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"you won on lines:", *winning_lines)  # "*" is in this case the splat operator - pass every line from winning_lines list to print function
    return winnings - total_bet

def main():  # function for rerunning the program
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()
