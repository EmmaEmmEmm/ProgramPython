def getMaxType(cards):
    possible_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    sorted_numbers = sorted([possible_numbers.index(card[:-1]) for card in cards])
    kinds_of_numbers = len(set(sorted_numbers))
    sorted_diffs = [sorted_numbers[i] - sorted_numbers[i-1] for i in range(1, 5)]
    shapes = [card[-1] for card in cards]
    if kinds_of_numbers == 5:
        is_straight = set(sorted_diffs) <= set([1, 9])
        is_flush = len(set(shapes)) == 1
        if is_flush and is_straight:
            return 9
        elif is_flush:
            return 6
        elif is_straight:
            return 5
        return 1
    if kinds_of_numbers == 4:
        return 2 # pair
    if kinds_of_numbers == 3:
        if 0 in [sorted_diffs[i]-sorted_diffs[i-1] for i in range(1,4)]: # at least 3 numbers are the same.
            return 4 # Three of a kind.
        return 3 # two pairs.

    if sorted_diffs[0] != 0 or sorted_diffs[-1] != 0: # diffs = [0,0,0,N] or [N,0,0,0]
        return 8 # Four of the kind.
    return 7 # Full house

def is_logical_input(cards):
    possible_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    possible_shapes = ['S', 'H', 'D', 'C']
    for card in cards:
        if card[:-1] not in possible_numbers or card[-1] not in possible_shapes:
            return False
    return True

def main():
    A_set = input().split(" ")
    B_set = input().split(" ")
    if not is_logical_input(A_set) or not is_logical_input(B_set):
        print('Error input')
    elif len(set(A_set + B_set)) != 10:
        print('Duplicate deal')
    else:
        print(max(getMaxType(A_set), getMaxType(B_set)))
main()