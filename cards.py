import random

Rank = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Suit = ['S','D','C','H']
high = False
pair = False
three = False
four = False
two_pair = False
full_house = False
straight = False
flush = False
royal = False

class card:
    def __init__(self,Rank,Suit):
        self.Rank = Rank
        self.Suit = Suit

drawn = []


def generateCard():
    gen = card(random.choice(Rank), random.choice(Suit))
    return gen

#def check():

def printCardList(card):
    output = ""
    i = 0
    while i < 5:

        output = output + str(card[i].Rank) + card[i].Suit + ", "
        i = i + 1

    print(output)


def checkFlush():
    k = 0 
    j = 1
    while j < 5:
        
        if drawn[k].Suit != drawn[j].Suit:
            return False
        j = j + 1
        
    
    return True

def checkRoyalStraightFlush():
    k = 0 
    j = 1 
    sort_card = sorted(drawn, key=lambda x: x.Rank, reverse= False)
    while j < 5:
        if sort_card[j].Rank - sort_card[k].Rank != 1 and sort_card[j].Rank - sort_card[k].Rank != 9:
            #
            return False
        k = k + 1
        j = j + 1

    k = 0 
    j = 1
    while j < 5:
        
        if drawn[k].Suit != drawn[j].Suit:
            return False
        j = j + 1

    
    if sort_card[1].Rank - sort_card[0].Rank == 9:
        return True
    else:
        return False

def checkStraight():
    k = 0 
    j = 1 
    sort_card = sorted(drawn, key=lambda x: x.Rank, reverse= False)
    while j < 5:
        if sort_card[j].Rank - sort_card[k].Rank != 1 and sort_card[j].Rank - sort_card[k].Rank != 9:
            #
            return False
        k = k + 1
        j = j + 1
    
    return True
    
def checkStraightFlush():
    if checkFlush() and checkStraight():
        return True
    else:
        return False
    

def checkFullHouse():
    countx = 0
    county = 0
    sort_card = sorted(drawn, key=lambda x: x.Rank, reverse=False)
    k = 0 
    j = 1 
    #
    while k < len(sort_card) - 1:  # Ensure k and j stay within bounds
        if sort_card[k].Rank == sort_card[j].Rank:
            countx = countx + 1     
            
        else:
            k = k + 1
            j = k + 1 
            break
        k = k + 1
        j = k + 1  # j is always k + 1


    while k < len(sort_card) - 1:  # Reset or adjust for second loop
        if sort_card[k].Rank == sort_card[j].Rank:
            county = county + 1     
            
        else:
            k = k + 1
            j = k + 1 
            break
        k = k + 1
        j = k + 1  # j is always k + 1

    

    # Assuming intent was: one group of 3 (countx = 2 matches) and one of 2 (county = 1 match)
    if (countx == 2 and county == 1) or (countx == 1 and county == 2):
        return True
    return False


def checkTwoPair():
    countx = 0
    county = 0
    sort_card = sorted(drawn, key=lambda x: x.Rank, reverse=False)
    k = 0 
    j = 1 
    #
    while k < len(sort_card) - 1:  # Ensure k and j stay within bounds
        if sort_card[k].Rank == sort_card[j].Rank:
            countx = countx + 1    

        elif k == 0 and sort_card[k].Rank != sort_card[j].Rank: #for the first loop if things are different
             pass

            
        elif k != 0 and sort_card[k].Rank != sort_card[j].Rank:
            k = k + 1
            j = k + 1 
            break
        k = k + 1
        j = k + 1  # j is always k + 1


    while k < len(sort_card) - 1:  # Reset or adjust for second loop
        if sort_card[k].Rank == sort_card[j].Rank:
            county = county + 1     
            
        else:
            k = k + 1
            j = k + 1 
            break
        k = k + 1
        j = k + 1  # j is always k + 1

    

    # Assuming intent was: one group of 3 (countx = 2 matches) and one of 2 (county = 1 match)
    if (countx == 1 and county == 1):
        return True
    return False
    
def checkFourOfaKind():
    count = 0
    sort_card = sorted(drawn, key=lambda x: x.Rank, reverse= False)
    k = 0 
    j = 1 
    #
    while k < 5 and j < 5:
        if sort_card[k].Rank == sort_card[j].Rank:
                    count = count + 1        
        k = k + 1
        j = j + 1

    if count == 3:
        return True

    
    return False

def checkThreeOfaKind():
    sort_card = sorted(drawn, key=lambda x: x.Rank, reverse=False)
    # Check each set of three consecutive cards
    for k in range(3):  # 0 to 2, since 5 - 3 = 2
        if (sort_card[k].Rank == sort_card[k + 1].Rank == sort_card[k + 2].Rank):
            return True
    return False

        
    return False

def checkPair():
    count = 0
    sort_card = sorted(drawn, key=lambda x: x.Rank, reverse= False)
    k = 0 
    j = 1 
    #
    while k < 5 and j < 5:
        if sort_card[k].Rank == sort_card[j].Rank:
                    count = count + 1        
        k = k + 1
        j = j + 1

    if count == 1:
        return True


    
                    




def draw():
    output = ""
    i = 0
    while i < 5:
        card = generateCard()
        while card  in drawn:
            card = generateCard()
        drawn.append(card)
        
        
        i = i + 1

    check()

    for card in drawn:
        if (card.Rank == 1):
            card.Rank = 'A'
        if (card.Rank == 11):
            card.Rank = 'J'
        if (card.Rank == 12):
            card.Rank = 'Q'
        if (card.Rank == 13):
            card.Rank = 'K'
        output = output + str(card.Rank) + card.Suit + ", "
        
    print(output)
    

def check():
    royal = checkRoyalStraightFlush()
    straight_flush = checkStraightFlush()
    flush = checkFlush()
    straight = checkStraight()
    full_house = checkFullHouse()
    four = checkFourOfaKind()
    two_pair = checkTwoPair()
    three = checkThreeOfaKind()
    pair = checkPair()
    high = False

    if royal:
        print("Royal Straight Flush!")
        return False

    if straight_flush:
        print("Straight flush!")
        return False
    if four:
        print("Four of A Kind!")
        return False
    if full_house:
        print("Full House!")

    if straight:
        print("Straight!")
        return False

    if flush:
        print("Flush!")
        return False
    if three:
        print("three of a kind!")
        return False
    
    if two_pair:
        print("two pair!")
        return False
    
    if pair:
        print("Pair!")
        return False
    
    else:
        high = True
        print("High Card of : ")
        high_card = max(drawn, key=lambda obj: obj.Rank)
        if (high_card.Rank == 1):
            high_card.Rank = 'A'
        if (high_card.Rank == 11):
            high_card.Rank = 'J'
        if (high_card.Rank == 12):
            high_card.Rank = 'Q'
        if (high_card.Rank == 13):
            high_card.Rank = 'K'

        print(high_card.Rank, high_card.Suit)
        
    





#draw()


draw()




        
    

    











