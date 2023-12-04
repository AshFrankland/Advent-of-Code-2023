def get_input():
    input = 'Day_04_input.txt'
    with open(input) as puzzle_input:
        txt = puzzle_input.readlines()
        raw_input = []
        card_dict = {}
        for line in txt:
            raw_input.append(line.lstrip('Card ').rstrip('\n'))
        for string in raw_input:
            card = string.split(':')
            card_id = int(card[0])
            nums = card[1].split('|')
            wins = nums[0].split(' ')
            while '' in wins:
                wins.remove('')
            nums = nums[1].split(' ')
            while '' in nums:
                nums.remove('')
            for num in range(len(wins)):
                wins[num] = int(wins[num])
            for num in range(len(nums)):
                nums[num] = int(nums[num])
            card_dict[card_id] = {'wins': wins, 'nums': nums, 'copies': 1}
        return card_dict

def winning_nums(card_dict):
    score = 0
    for card in card_dict:
        card_score = 0
        for num in card_dict[card]['nums']:
            if num in card_dict[card]['wins']:
                if card_score == 0:
                    card_score += 1
                else:
                    card_score *= 2
        score += card_score
    print(score)

def winning_cards(card_dict):
    for card in card_dict:
        win_count = 0
        for num in card_dict[card]['nums']:
            if num in card_dict[card]['wins']:
                win_count += 1
        for cards in range(1, win_count + 1):
            card_dict[card + cards]['copies'] += card_dict[card]['copies']
    cards = 0
    for card in card_dict:
        cards += card_dict[card]['copies']
    print(cards)

def main():
    card_dict = get_input()
    winning_nums(card_dict)
    winning_cards(card_dict)

if __name__ == '__main__':
    main()