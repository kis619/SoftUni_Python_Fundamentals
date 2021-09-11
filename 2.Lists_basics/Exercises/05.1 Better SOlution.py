deck = input().split()
shuffles = int(input())

half_deck = len(deck) // 2
for _ in range(shuffles):
    left_half = deck[0: half_deck]
    right_half = deck[half_deck:]

    shuffled_deck =[]
    for i in range(len(left_half)):
        shuffled_deck.append(left_half[i])
        shuffled_deck.append(right_half[i])
    deck = shuffled_deck

print(deck)
