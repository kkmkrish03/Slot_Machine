# This file contains the functions for generating the slot machine and checking for winnings.

import random
import emoji
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
from utility.user_input import *
from utility.helper import *


def create_slot_machine(rows, cols, symbols):
    # Create an empty list for each row and column
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_smbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_smbols)
            current_smbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def check_winning_lines(columns, lines, bet, values):
    # Check for winning lines
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

def spin(balance, lines, bet, total_bet, getVal):
    if getVal:
        lines = get_pay_lines()
        while True:
            bet = get_bet_for_coin_slot()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
            else:
                break
    
    print(f"Yo are betting ${bet} on {lines} line(s). Total bet is equal to: ${total_bet}")
    
    slots = create_slot_machine(PAYLINES, REELS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning_lines(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winnings > 0:
        print(f"You won on lines: ", *winning_lines)
        print(f"Congratulations....! {emoji.emojize(':sparkles:', language='en')} {emoji.emojize(':party_popper:', language='en')}" )
    return winnings - total_bet
