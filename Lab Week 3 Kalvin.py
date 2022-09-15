

print('Welcome to the Flarsheim Guesser!\n')

print('Please think of a number between and including 1 and 100.\n')

def console(): #new function
    '''remainder of 3'''
    ran3 = int(input('What is the remainder when your number is divided by 3 ?')) #ask for integer input
    while ran3 != 0 or 1 or 2:
        if ran3 > 2:
            print('The value entered must be less than 3')
            ran3 = int(input('What is the remainder when your number is divided by 3 ?')) #asks again if value greater than 2
        elif ran3 < 0:
            print('The value entered msut be 0 or greater')
            ran3 = int(input('What is the remainder when your number is divided by 3 ?'))#asks again if value greater than 0
        else:
            break
        '''remainder of 5'''
    ran5 = int(input('What is the remainder when your number is divided by 5 ?'))
    while ran5 != 0 or 1 or 2 or 3 or 4:
        if ran5 > 4:
            print('The value entered must be less than 5')
            ran5 = int(input('What is the remainder when your number is divided by 5 ?'))#asks again if value greater than 5
        elif ran5 < 0:
            print('The value entered msut be 0 or greater')
            ran5 = int(input('What is the remainder when your number is divided by 5 ?'))#asks again if value greater than 0
        else:
            break
        '''remainder of 7'''
    ran7 = int(input('What is the remainder when your number is divided by 7 ?'))
    while ran7 != 0 or 1 or 2 or 3 or 4 or 5 or 6:
        if ran7 > 6:
            print('The value entered must be less than 7')
            ran7 = int(input('What is the remainder when your number is divided by 7 ?'))#asks again if value greater than 7
        elif ran7 < 0:
            print('The value entered msut be 0 or greater')
            ran7 = int(input('What is the remainder when your number is divided by 7 ?'))#asks again if value greater than 0
        else:
            break

    for i in range(1, 101): #determines the number from the given input values of remainder
        if i % 3 == ran3 and i % 5 == ran5 and i % 7 == ran7:
            print(f'Your number was {i}')
            print('How amazing was that?')
    play = input('Do you want to play again? Y to continue, N to quit ==>') #asks if user wants to play again
    while play != 'y' or 'Y' or 'n' or 'N':
        if play == 'y' or 'Y':
            console()
        if play == 'n' or 'N':
            break
        break

console() #prints/runs the function
