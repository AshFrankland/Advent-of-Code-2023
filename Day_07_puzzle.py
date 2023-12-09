def get_input():
    input = 'Day_07_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        for line in txt:
            raw_input.append(line.rstrip('\n'))
        hands1 = {}
        for hand in raw_input:
            cards, bid_str = hand.split(' ')
            counts = []
            for card in cards:
                counts.append(cards.count(card))
            if counts.count(5) == 5:
                hand_type = 6
            elif counts.count(4) == 4:
                hand_type = 5
            elif counts.count(3) == 3:
                if counts.count(2) == 2:
                    hand_type = 4
                else:
                    hand_type = 3
            elif counts.count(2) == 4:
                hand_type = 2
            elif counts.count(2) == 2:
                hand_type = 1
            else:
                hand_type = 0
            hands1[cards] = {'bid': int(bid_str), 'type': hand_type, 'rank': 0}
            hands2 = {}
            for hand in raw_input:
                cards, bid_str = hand.split(' ')
                counts = []
                for card in cards:
                    counts.append(cards.count(card))
                if counts.count(5) == 5:
                    hand_type = 6
                elif counts.count(4) == 4:
                    if hand.count('J') == 1 or hand.count('J') == 4:
                        hand_type = 6
                    else:
                        hand_type = 5
                elif counts.count(3) == 3:
                    if counts.count(2) == 2:
                        if hand.count('J') == 2 or hand.count('J') == 3:
                            hand_type = 6
                        elif hand.count('J') == 1:
                            hand_type = 5
                        else:
                            hand_type = 4
                    else:
                        if hand.count('J') == 3 or hand.count('J') == 1:
                            hand_type = 5
                        else:
                            hand_type = 3
                elif counts.count(2) == 4:
                    if hand.count('J') == 1:
                        hand_type = 4
                    elif hand.count('J') == 2:
                        hand_type = 5
                    else:
                        hand_type = 2
                elif counts.count(2) == 2:
                    if hand.count('J') == 1 or hand.count('J') == 2:
                        hand_type = 3
                    else:
                        hand_type = 1
                else:
                    if hand.count('J') == 1:
                        hand_type = 1
                    else:
                        hand_type = 0
                hands2[cards] = {'bid': int(bid_str), 'type': hand_type, 'rank': 0}
        return hands1, hands2

def hand_sorter(hands):
    card_power = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
    for hand1 in hands:
        for hand2 in hands:
            if hand1 == hand2:
                hands[hand1]['rank'] += 1
            elif hands[hand1]['type'] > hands[hand2]['type']:
                hands[hand1]['rank'] += 1
            elif hands[hand1]['type'] == hands[hand2]['type']:
                if card_power[hand1[0]] != card_power[hand2[0]]:
                    if card_power[hand1[0]] > card_power[hand2[0]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
                elif card_power[hand1[1]] != card_power[hand2[1]]:
                    if card_power[hand1[1]] > card_power[hand2[1]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
                elif card_power[hand1[2]] != card_power[hand2[2]]:
                    if card_power[hand1[2]] > card_power[hand2[2]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
                elif card_power[hand1[3]] != card_power[hand2[3]]:
                    if card_power[hand1[3]] > card_power[hand2[3]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
                elif card_power[hand1[4]] != card_power[hand2[4]]:
                    if card_power[hand1[4]] > card_power[hand2[4]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
    winnings = 0
    for hand in hands:
        winnings += (hands[hand]['rank'] * hands[hand]['bid'])
    print(winnings)

def joke_sorter(hands):
    card_power = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}
    for hand1 in hands:
        for hand2 in hands:
            if hand1 == hand2:
                hands[hand1]['rank'] += 1
            elif hands[hand1]['type'] > hands[hand2]['type']:
                hands[hand1]['rank'] += 1
            elif hands[hand1]['type'] == hands[hand2]['type']:
                if card_power[hand1[0]] != card_power[hand2[0]]:
                    if card_power[hand1[0]] > card_power[hand2[0]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
                elif card_power[hand1[1]] != card_power[hand2[1]]:
                    if card_power[hand1[1]] > card_power[hand2[1]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
                elif card_power[hand1[2]] != card_power[hand2[2]]:
                    if card_power[hand1[2]] > card_power[hand2[2]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
                elif card_power[hand1[3]] != card_power[hand2[3]]:
                    if card_power[hand1[3]] > card_power[hand2[3]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
                elif card_power[hand1[4]] != card_power[hand2[4]]:
                    if card_power[hand1[4]] > card_power[hand2[4]]:
                        hands[hand1]['rank'] += 1
                    else:
                        pass
    winnings = 0
    for hand in hands:
        winnings += (hands[hand]['rank'] * hands[hand]['bid'])
    print(winnings)

def main():
    hands1, hands2 = get_input()
    hand_sorter(hands1)
    joke_sorter(hands2)

if __name__ == '__main__':
    main()