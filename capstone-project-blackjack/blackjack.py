import os
from utils import pickACard, addToTotal, printCards


while True:
    # Start the program by declaring two lists of cards and two totals
    userCards = []
    computerCards = []
    userTotal = 0
    computerTotal = 0

    # Drawing two cards for the user and the computer
    pickACard(userCards)
    userTotal = addToTotal(userCards[0], userTotal)
    pickACard(userCards)
    userTotal = addToTotal(userCards[1], userTotal)

    pickACard(computerCards)
    computerTotal = addToTotal(computerCards[0], computerTotal)
    pickACard(computerCards)
    computerTotal = addToTotal(computerCards[1], computerTotal)

    # declaring a print function that can be used everywhere

    def printAllCards():
        global userCards
        global computerCards
        print('Your Cards')
        printCards(userCards)
        print('AI Cards')
        printCards(computerCards)

    def simulateComputersTurn():
        global userCards
        global computerCards
        global computerTotal
        global userTotal
        if computerTotal < userTotal:
            if computerTotal > 15:
                printAllCards()
                print('Victory')
            else:
                while computerTotal < 15:
                    pickACard(computerCards)
                    computerTotal = addToTotal(
                        computerCards[len(computerCards) - 1], computerTotal)
                if computerTotal > userTotal:
                    if computerTotal > 21:
                        printAllCards()
                        print('Victory')
                    else:
                        printAllCards()
                        print('Loss')
                else:
                    printAllCards()
                    print('Victory')

        elif computerTotal > userTotal:
            if computerTotal > 21:
                printAllCards()
                print('Victory')
            else:
                printAllCards()
                print('Loss')
        else:
            printAllCards()
            print('Draw')

    # Show user his cards and one of computer cards
    print(
        f'New Game Started\nYour Cards\n{userCards[0]} {userCards[1]}\nComputers Cards\n{computerCards[0]} X')

    # Check if user or computer have blackJack
    if userTotal == 21:
        if computerTotal == 21:
            print('Draw')
            break
        else:
            print('Victory')
            break
    elif computerTotal == 21:
        print('Loss')
        break

    # Ask user if they want another card repeatedly until they say no
    while True:
        userInput = input(
            'Do you want another card? Enter Y for yes or N for no. ')
        if userInput == 'Y':
            pickACard(userCards)
            userTotal = addToTotal(userCards[len(userCards)-1], userTotal)
            printCards(userCards)
            if userTotal > 21:
                printAllCards()
                print('Loss')
                break
        elif userInput == 'N':
            break

    # Simulate computer picking cards
    simulateComputersTurn()

    playAgain = input(
        'Do you want to play again? Enter Y for yes or N for no. ')

    if playAgain != 'Y':
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
