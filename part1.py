
vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]

suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

card_dict = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 11,
    'queen': 12,
    'king': 13,
    'ace': 14
}

############ Functions of returning the Deck of Cards ############

def get_deck_of_cards() -> set:
    """
    Returns the complete deck of cards set of 52 tuples with different vals and suits combinations
    This functions uses zip function for it
    """
    return set(zip(vals * 4, suits * 13))

def get_deck_of_cards_without_zip() -> set:
    """
    Returns the complete deck of cards set of 52 tuples with different vals and suits combinations
    This function uses list comprehension without zip function
    """
    deck_vals = vals * 4
    deck_suits = suits * 13
    return set([(deck_vals[i], deck_suits[i]) for i in range(52)])

############ Utility Functions ###############

def validate_cards(player_cards: "Set of tuples") -> bool:
    """
    Validates the player_cards 
    1. Checks if the player_cards is a set or not and throws a TypeError if not
    2. Checks if each card in player_cards is valid or not and throws a value error if not
    """
    if type(player_cards) != set:
        raise TypeError("Invalid type of player_cards sent, The player_cards should be a set")

    for card in player_cards:
        if type(card) != tuple:
            raise TypeError("Each card inside player_cards should be a tuple with value and suit in it")
        
        if card[0] not in vals:
            raise ValueError(f"Invalid card passed as {card[0]} is not a valid value")

        if card[1] not in suits:
            raise ValueError(f"Invalid card passed as {card[1]} is not a valid suit")

    return True

def convert_cards_to_values(player_cards: "Set of 3 or 4 or 5 cards") -> list:
    """
    Converts the set of tuples of string and suits into set of tuples of corresponding value and suits
    Example
    ("10", "spades"), ("jack", "clubs"), ("king", "hearts") -> (10, "spades"), (11, "spades"), (13, "hearts")
    """
    return list(map(lambda x: (card_dict[x[0]], x[1]) if x[0] in card_dict else (int(x[0]), x[1]), player_cards))

def check_if_list_in_sequence(values: list) -> bool:
    """
    Checks if the list contains all the values in a straight sequence or not
    Example
    [1,2,3,4,5] -> True
    [1,7,8,4,6] -> False

    Returns True if they are consecutive sequence else False
    """
    max_value = max(values)
    min_value = min(values)
    return values == list(range(min_value, max_value + 1))

def get_top_2_frequencies_of_list(values: list) -> tuple:
    """
    Returns a tuple with the top 2 highest frequencies in the list
    Example
    [1,1,1,2,2] -> (3, 2)
    [1,1,3,3,6] -> (2, 2)

    """
    max_cnt = 0
    prev_max_cnt = 0
    for x in sorted(set(values), key=lambda x: values.count(x)):
        cnt = values.count(x)
        if cnt >= max_cnt:
            prev_max_cnt = max_cnt
            max_cnt = cnt
    return (max_cnt, prev_max_cnt)

############### Functions for checking a hand in Poker ##############

def check_for_royal_flush(player_cards: "Set of 3 or 4 or 5 cards") -> bool:
    """
    Checks if the player_cards contains 5 cards and a royal flush
    Example
    10 jack queen king ace 
    The Hightest sequence cards all of same suit - spades, clubs, hearts or diamonds

    Returns True if it finds in player_cards else Returns False
    """
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))
        
        return len(set(map(lambda x: x[1], sorted_cards))) == 1 and [10, 11, 12, 13, 14] == list(map(lambda x: x[0], sorted_cards))

def check_for_straight_flush(player_cards: "Set of 3 or 4 or 5 cards") -> bool:
    """
    Checks if the player_cards contains 5 cards and a straight flush
    Example
    6 7 8 9 10 
    Any sequence of the cards all of the same suit - spades, clubs, hearts or diamonds

    Returns True if it finds in player_cards else Returns False
    """
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))

        values_list = list(map(lambda x: x[0], sorted_cards))
        return len(set(map(lambda x: x[1], sorted_cards))) == 1 and check_if_list_in_sequence(values_list)
        

def check_for_four_of_a_kind(player_cards: "Set of 3 or 4 or 5 cards") -> bool:
    """
    Checks if the player_cards contains a Four of a kind in it
    Example
    queen queen queen queen 10
    4 Cards of same value 

    Returns True if it finds 4 Cards of same value else Returns False
    """
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))

        values_list = list(map(lambda x: x[0], sorted_cards))
        
        max_cnt, prev_max_cnt = get_top_2_frequencies_of_list(values_list)
        
        return max_cnt == 4

def check_for_full_house(player_cards: "Set of 3 or 4 or 5 cards") -> bool:
    """
    Checks if the player_cards contains Full House in it
    Example
    queen queen queen 8 8
    3 Cards of one value and 2 Cards of another value

    Returns True if it finds 3 cards of one value and 2 cards of another value else returns False
    """
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))

        values_list = list(map(lambda x: x[0], sorted_cards))
        max_cnt, prev_max_cnt = get_top_2_frequencies_of_list(values_list)
        return max_cnt == 3 and prev_max_cnt == 2

def check_for_flush(player_cards: "Set of 3 or 4 or 5 cards") -> bool:
    """
    Checks if the player_cards contains a Flush in it
    Example
    (queen, spades), (10, spades), (5, spades), (4, spades), (2, spades)
    All the 5 cards of same suit

    Returns True if it finds all the 5 cards of same suit else returns False
    """
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))

        return len(set(map(lambda x: x[1], sorted_cards))) == 1

def check_for_straight(player_cards: "Set of 3 or 4 or 5 cards") -> bool:
    """
    Checks if the player_cards contains a Straight in it
    Example
    (4, spades), (5, clubs), (6, hearts), (7, spades), (8, hearts)
    All the 5 cards values are in sequence and suits doesn't matter

    Returns True if it finds all the 5 cards values are in sequence without considering suits else returns False
    """
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))

        values_list = list(map(lambda x: x[0], sorted_cards))
        return check_if_list_in_sequence(values_list)

def check_for_three_of_a_kind(player_cards: "Set of 3 or 4 or 5 cards") -> bool:
    """
    Checks if the player_cards contains a Three of a Kind in it
    Example
    (queen, spades), (queen, hearts), (queen, clubs), (6, spades), (10, hearts)
    Any 3 cards of the same values 

    Returns True if it finds any 3 cards are same in value else returns False
    """
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))

        values_list = list(map(lambda x: x[0], sorted_cards))
        max_cnt, prev_max_cnt = get_top_2_frequencies_of_list(values_list)    

        return max_cnt >= 3

def check_for_two_pair(player_cards: "Set of 3 or 4 or 5 cards") -> bool:
    """
    Checks if the player_cards contains a 2 Pair in it
    Example
    (king, spades), (king, hearts), (8, clubs), (8, hearts), (5, spades)
    Any 2 pair of cards with same value

    Returns True if it finds any 2 Pairs with the same value else returns False
    """
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))

        values_list = list(map(lambda x: x[0], sorted_cards))
        max_cnt, prev_max_cnt = get_top_2_frequencies_of_list(values_list)

        return max_cnt == 2 and prev_max_cnt == 2

def check_for_pair(player_cards: "Set of 3 or 4 or 5 cards") -> bool:
    """
    Checks if the player_cards contains a Pair in it
    Example
    (jack, spades), (jack, clubs), (10, hearts), (8, spades), (7, clubs)
    A pair of cards with same value

    Returns True if it finds a pair with the same value else returns False
    """
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))

        values_list = list(map(lambda x: x[0], sorted_cards))
        max_cnt, prev_max_cnt = get_top_2_frequencies_of_list(values_list)
        return max_cnt >= 2

######################## End of Poker Hand Functions ####################


poker_hand_order = (
    (check_for_royal_flush, "Royal Flush"),
    (check_for_straight_flush, "Straight Flush"),
    (check_for_four_of_a_kind, "Four of a Kind"), 
    (check_for_full_house, "Full House"),
    (check_for_flush, "Flush"),
    (check_for_straight, "Straight"), 
    (check_for_three_of_a_kind, "Three Of a Kind"),
    (check_for_two_pair, "Two Pair"),
    (check_for_pair, "Pair")
)

def get_high_card_value(player_cards: "Set of 3 or 4 or 5 cards") -> int:
    """
    Returns maximum value of the card in player_cards

    Example
    (10, spades), (5, clubs), (7, hearts), (3, clubs), (2, diamonds) -> Returns 10
    """
    if not len(player_cards):
        return None
    if validate_cards(player_cards):
        sorted_cards = sorted(convert_cards_to_values(player_cards))
        
        return max(set(map(lambda x: x[0], sorted_cards)))

def resolve_by_high_card(player_a_cards: "Set of 3 or 4 or 5 cards", player_b_cards: "Set of 3 or 4 or 5 cards"):
    player_a_high_card = get_high_card_value(player_a_cards)
    player_b_high_card = get_high_card_value(player_b_cards)
    while player_a_high_card is not None and player_b_high_card is not None and player_a_high_card == player_b_high_card:
        player_a_high_card = get_high_card_value({val for val in player_a_cards if val[0] != vals[player_a_high_card]})
        player_b_high_card = get_high_card_value({val for val in player_b_cards if val[0] != vals[player_b_high_card]})

    if player_a_high_card is not None and player_b_high_card is not None:
        return "Player A" if player_a_high_card > player_b_high_card else "Player B"
    else:
        return "Player A and Player B"

def resolve_with_preferential_high_card_value(
    player_a_cards: "Set of 3 or 4 or 5 cards of Player A",
    player_b_cards: "Set of 3 or 4 or 5 cards of player B",
    count: "Preferential High card count"):

    player_a_values_list = list(map(lambda x: x[0], sorted(convert_cards_to_values(player_a_cards))))
    player_b_values_list = list(map(lambda x: x[0], sorted(convert_cards_to_values(player_b_cards))))
    player_a_values_set = set(player_a_values_list)
    player_b_values_set = set(player_b_values_list)

    player_a_cards_to_compare = []
    player_b_cards_to_compare = []

    for val in player_a_values_set:
        if player_a_values_list.count(val) == count:
            player_a_cards_to_compare.append(val)
    for val in player_b_values_set:
        if player_b_values_list.count(val) == count:
            player_b_cards_to_compare.append(val)
    player_a_card_to_compare = max(player_a_cards_to_compare)
    player_b_card_to_compare = max(player_b_cards_to_compare)

    if player_a_card_to_compare > player_b_card_to_compare:
        return "Player A"
    elif player_b_card_to_compare < player_a_card_to_compare:
        return "Player B"
    else:
        resolve_by_high_card(
            [val for val in player_a_cards if card_dict[val[0]] not in player_a_cards_to_compare], 
            [val for val in player_b_cards if card_dict[val[0]] not in player_b_cards_to_compare])

def resolve_rank_tie(
    poker_hand: "The Poker hand which both the players have",
    player_a_cards: "Set of 3 or 4 or 5 cards of Player A",
    player_b_cards: "Set of 3 or 4 or 5 cards of player B") -> str:

    if poker_hand == "Straight Flush" or poker_hand == "Flush" or poker_hand == "Straight":
        return resolve_by_high_card(player_a_cards, player_b_cards)
    elif poker_hand == "Four of a Kind":
        return resolve_with_preferential_high_card_value(player_a_cards, player_b_cards, 4)
    elif poker_hand == "Full House" or poker_hand == "Three Of a Kind":
        return resolve_with_preferential_high_card_value(player_a_cards, player_b_cards, 3)
    elif poker_hand == "Pair" and poker_hand == "Two Pair":
        return resolve_with_preferential_high_card_value(player_a_cards, player_b_cards, 2)

def get_result_of_poker(player_a_cards: "Set of 3 or 4 or 5 cards of player A", player_b_cards: "Set of 3 or 4 or 5 cards of player B") -> str:
    """
    This function returns the player who won the game of poker based on the cards passed to the function
    Each Player's cards are checked if the cards have any of the rank according to the order
    If the Player A rank is less than Player B then Player A has won it
    If the Player B rank is less than Player B then Player B has won it

    If both the Player A rank and Player B rank are same then 
    based on the poker hand the involved high card is calculated and who ever has a high card in the poker hand is the
    winner of the game.
    """

    if validate_cards(player_a_cards) and validate_cards(player_b_cards):
        player_a_rank = player_b_rank = None
        player_a_hand = player_b_hand = None
        for i in range(len(poker_hand_order)):
            if poker_hand_order[i][0](player_a_cards):
                player_a_rank = i + 1
                player_a_hand = poker_hand_order[i][1]
                print("Player A has a " + poker_hand_order[i][1])
                break
        
        for i in range(len(poker_hand_order)):
            if poker_hand_order[i][0](player_b_cards):
                player_b_rank = i + 1
                player_b_hand = poker_hand_order[i][1]
                print("Player B has a " + poker_hand_order[i][1])
                break
        print(player_a_rank)
        print(player_b_rank)
        if player_a_rank is not None and player_b_rank is not None:
            # Both the players have a Poker Hand
            if player_a_rank < player_b_rank:
                # Player A has a higher ranking poker hand than Player B
                print("Player A has won the game.")
                return "Player A"
            elif player_a_rank > player_b_rank:
                # Player B has a higher ranking poker hand than Player A
                print("Player B has won the game.")
                return "Player B"
            elif player_a_rank == player_b_rank:
                # Both Player A and Player B have same ranking poker hand we need to resolve the tie
                return resolve_rank_tie(poker_hand_order[player_a_rank - 1][1], player_a_cards, player_b_cards)
        elif player_a_rank is not None:
            # Player A has a ranking poker hand and Player B does not have any
            print("Player A has won the game.")
            return "Player A"
        elif player_b_rank is not None:
            # Player B has a ranking poker hand and Player A does not have any
            print("Player B has won the game.")
            return "Player B"
        else:
            # Player A and Player B do not have any special poker hand
            player_a_high_card = get_high_card_value(player_a_cards)
            player_b_high_card = get_high_card_value(player_b_cards)
            if player_a_high_card > player_b_high_card:
                print("Player A has a higher card than Player B")
                print("Player A has won the game.")
                return "Player A"
            else:
                print("Player B has a higher card than Player A")
                print("Player B has won the game")
                return "Player B"
