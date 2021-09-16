winning_symbols = ["@", "#", "$", "^"]


# def is_jackpot(ticket):                90 / 100
#     left_half = ticket[:10]
#     right_half = ticket[10:]
#     if left_half == right_half and left_half[0] in winning_symbols:
#         print(f"ticket \"{ticket}\" - 10{left_half[0]} Jackpot!")
#         return True
#     return False
def is_jackpot(ticket):
    for winning_symbol in winning_symbols:
        if winning_symbol in ticket:
            if ticket.count(winning_symbol) == 20:
                print(f"ticket \"{ticket}\" - 10{winning_symbol} Jackpot!")
                return True
    return False


def is_winning(ticket):
    left_half = ticket[:10]
    right_half = ticket[10:]
    for symbol in winning_symbols:
        if symbol * 6 in left_half and symbol * 6 in right_half:
            left = left_half.count(symbol)
            right = right_half.count(symbol)
            print(f'ticket "{ticket}" - {min(left, right)}{symbol}')
            return True
    return False


tickets = [el.strip() for el in input().split(", ")]
for ticket in tickets:
    ticket = ticket.strip()

    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    if is_jackpot(ticket):
        continue

    if is_winning(ticket):
        continue

    print(f"ticket \"{ticket}\" - no match")

