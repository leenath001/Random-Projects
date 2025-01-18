import random2

dealerhand = random2.randint(1,11) + random2.randint(1,10)

while dealerhand < 16:
    dealerhand = dealerhand + random2.randint(1,11)    
print('Dealer has a', dealerhand)
print()

table = ['Nate','Alex','KD','Isa','Mom','Dad']
scores = []
n = len(table)
winct = [0]*n

for player in table:
    index = table.index(player)
    hnu = random2.randint(1,11) + random2.randint(1,10)
    if hnu == 21:
        print(table[index], 'has blackjack!')
        scores.insert(index,hnu)
    else:
        while hnu < 16:
            hnu = hnu + random2.randint(1,11)
    scores.insert(index, hnu)
    if hnu > 21:
        print(table[index], 'has a', scores[index],'and busted.')
    elif hnu == 21:
        print(table[index], 'has multi-card blackjack!')
    else:
        print(table[index], 'has a', hnu)

print()

for player in table:
    index = table.index(player)
    if scores[index] > 21:
        print(table[index], 'has busted.')
    elif dealerhand > 21:
        print('Dealer bust,', table[index], 'won!')
        winct[index] += 1 
    elif dealerhand == scores[index]:
        print(table[index], 'has pushed with the dealer.')
    elif scores[index] > dealerhand:
        print(table[index], 'has won!')
        winct[index] += 1
    else:
        print('Dealer has beat',table[index])

print()        
print(winct)
