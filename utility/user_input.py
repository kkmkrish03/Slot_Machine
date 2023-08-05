import os
import sys
# Get the current directory (main_directory)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (the directory containing main_directory)
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)

# Now you can import the function from the parallel directory
from constants.constants import *
from utility.helper import *

def deposit():
    """Deposit money into the bank account"""
    while True:
        amount = input("What would you like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_pay_lines():
    """Get the number of pay lines to bet."""
    while True:
        lines = input("Enter the number of pay lines to bet on (1-" + str(MAX_SLOTS_FOR_PAY_LINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_SLOTS_FOR_PAY_LINE:
                break
            else:
                print("Enter a valid number of pay line.")
        else:
            print("Please enter a number.")
    return lines



def get_bet_for_coin_slot():
    """Get the user's bet for each line."""
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number.")
    return amount

def remember_bet():
    while True:
        remember = input("Would you like me to remember your bet for rest of the game? (y/N) ")
        if is_string_valid_boolean(remember):
            return is_string_equal_to_case_insensitive(remember)
        else:
            print(f"Sorry, not sure what that was. (y/N) ")
    return False