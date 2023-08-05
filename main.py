import random
import emoji
from service.slot_machine import create_slot_machine, check_winning_lines, spin
from constants.constants import *
from utility.user_input import *
from utility.helper import *

def main():
    balance = deposit()
    lines = get_pay_lines()
    while True:
        bet = get_bet_for_coin_slot()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    remember = remember_bet()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press enter to play (q to quit).")
        if ans == "q":
            break 
        if balance <= 0:
            print(f"No more money!")
            break
        if remember and total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
            break
        balance += spin(balance, lines, bet, total_bet, not remember)
        
    print(f"You left with ${balance}")
    
if __name__ == "__main__":
    main()