########################################################################
##
## CS 101 Lab
## Program: #4
## Name: Kalvin Tran
## Email: ktcd9@umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''

    play = input('Do you want to play again? ==> ')
    if play != 'yes' or 'y':
        while True:
            print('You must enter Y/YES/N/NO to continue. Please try again')
            play = input('Do you want to play again? ==> ')
    if play == 'yes' or 'y':
        return True
    if play == 'no' or 'n':
        return False
    
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wage = int(input('How many chips do you want to wager? ==> '))
    while wage < 0 or wage > bank:
        if wage < 0:
            print('The wager amount must be greater than 0. Please enter again.')
        elif wage > bank:
            print(f'The wager amount cannot be greater than how much you have. {bank}')
        else:
            break
        wage = int(input('How many chips do you want to wager? ==> '))  
    
    return wage            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    reela = random.randint(1,9)
    reelb = random.randint(1,9)
    reelc = random.randint(1,9)

    return reela, reelb, reelc

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc:
        matches = 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        matches = 2
    else:
        matches = 0
    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    chips = int(input('How many chips do you want to start with? ==> '))
    while chips < 0 or chips > 100:
        if chips < 0:
            print('Too low a value, you can only choose 1 - 100 chips')
        if chips > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
        else:
            break
        chips = int(input('How many chips do you want to start with? ==> '))
    return chips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        payout = wager*10 -wager
    if matches == 2:
        payout = wager*3 - wager
    if matches == 0:
        payout = wager * -1
    return payout    


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
