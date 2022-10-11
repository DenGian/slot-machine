import rondom

MAX_LINES = 3 # global constant that is not going to change - max lines to bet on is now set to 3 - more dynamic program
MAX_BET = 200 # global constant that is not going to change - max amount to bet is now set to 200
MIN_BET = 10 # global constant that is not going to change - min amount to bet is now set to 10

def deposit(): # function deposit - responsible for user input
    while True: # while loop that is set to true - continue to do function until break
        amount = input("What would you like to deposit? $") # prompt that comes up for user input
        if amount.isdigit(): # checking if input is a number and is a positive amount - first checking necessary because converting to int next step
            amount = int(amount) # converting input to int - string by default
            if amount > 0: # checking if amount is greater than 0
                break # if amount is greater than 0, the loop breaks
            else: # if amount is NOT greater than 0
                print("Amount must be greater than 0.") # prompt that shows up on the screen
        else: # if there was no number given by user
            print("Please enter a number.") # prompt that shows up on screen if there was no input by user
    return amount

def get_number_of_lines():
    while True: # while loop that is set to true - continue to do function until break
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") # prompt that comes up for user input - string concatenation
        if lines.isdigit(): # checking if input is a number and is a positive amount - first checking necessary because converting to int next step
            lines = int(lines) # converting input to int - string by default
            if 1 <= lines <= MAX_LINES: # checking if number of lines is between 1-3
                break # if lines is between 1-3, the loop breaks
            else: # if amount is NOT between 1-3
                print("Enter a valid number of lines.") # prompt that shows up on the screen
        else: # if there was NO input given by user
            print("Please enter a number.") # prompt that shows up on screen
    return lines

def get_bet():
    while True: # while loop that is set to true - continue to do function until break
        amount = input("What would you like to bet on each line? $") # prompt that comes up for user input
        if amount.isdigit(): # checking if input is a number and is a positive amount - first checking necessary because converting to int next step
            amount = int(amount) # converting input to int - string by default
            if MIN_BET <= amount <= MAX_BET: # checking if amount is between the MIN_BET and MAX_BET
                break # if amount is between the MIN_BET and MAX_BET, the loop breaks
            else: # if amount is NOT between the MIN_BET and MAX_BET
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") # Using f-string - You can write any variable in {...} and it will automatically be converted to a string (if it can be converted)
        else: # if there was no number given by user
            print("Please enter a number.") # prompt that shows up on screen for the user
    return amount

def main(): # function for rerunning the program
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

main()