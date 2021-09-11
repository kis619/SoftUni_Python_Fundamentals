list_of_cards = input().split()
number_of_shuffles = int(input())
first_half = []
second_half = []
number_of_elements = int(len(list_of_cards) / 2)

for _ in range(number_of_shuffles):
    for _ in range(number_of_elements):
        first_half.append(list_of_cards[0])
        second_half.append(list_of_cards[number_of_elements])
        list_of_cards.pop(0)

    list_after_cutting_the_deck = []
    for _ in range(len(list_of_cards)):
        list_after_cutting_the_deck.append(first_half[0])
        first_half.pop(0)
        list_after_cutting_the_deck.append(second_half[0])
        second_half.pop(0)
    list_of_cards = list_after_cutting_the_deck

print(list_of_cards)


