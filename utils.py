import random

blackjackCards = [1, 2, 3, 4, 5, 6, 7, 8,
                  9, 10, 'Jack', 'Queen', 'King', 'Ace']


def pickACard(list):
    return list.append(random.choice(blackjackCards))


def addToTotal(item, total):
    if item == 'Jack' or item == 'Queen' or item == 'King':
        total += 10
    elif item == 'Ace':
        if total + 11 > 21:
            total += 1
        else:
            total += 11
    else:
        total += item
    return total


def printCards(list):
    buildString = ''
    for item in list:
        if type(item) == int:
            buildString += f' {str(item)}'
        else:
            buildString += f' {item}'
    print(buildString)
