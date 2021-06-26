import pytest
import part1
import random

vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]

suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

ROYAL_FLUSH_SCENARIOS = (
    {("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades"), ("ace", "spades")},
    {("10", "clubs"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
    {("10", "hearts"), ("jack", "hearts"), ("queen", "hearts"), ("king", "hearts"), ("ace", "hearts")},
    {("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")}
)

STRAIGHT_FLUSH_SCENARIOS = (
    {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
    {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
    {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
    {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
    {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
    {("7", "clubs"), ("8", "clubs"), ("9", "clubs"), ("10", "clubs"), ("jack", "clubs")},
    {("8", "hearts"), ("9", "hearts"), ("10", "hearts"), ("jack", "hearts"), ("queen", "hearts")},
    {("9", "diamonds"), ("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds")}
)

FOUR_OF_A_KIND_SCENARIOS = (
    {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("2", "diamonds"), ("5", "spades")},
    {("3", "spades"), ("3", "clubs"), ("3", "hearts"), ("3", "diamonds"), ("2", "spades")},
    {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("4", "diamonds"), ("3", "spades")},
    {("5", "spades"), ("5", "clubs"), ("5", "hearts"), ("5", "diamonds"), ("king", "spades")},
    {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("6", "diamonds"), ("ace", "spades")},
    {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("jack", "spades")},
    {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("2", "spades")},
    {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
    {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("5", "spades")},
    {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("jack", "diamonds"), ("queen", "spades")},
    {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("queen", "diamonds"), ("5", "spades")},
    {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("king", "diamonds"), ("6", "spades")},
    {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts"), ("ace", "diamonds"), ("8", "spades")},
    # Scenarios with only 4 cards
    {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("2", "diamonds")},
    {("3", "spades"), ("3", "clubs"), ("3", "hearts"), ("3", "diamonds")},
    {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("4", "diamonds")},
    {("5", "spades"), ("5", "clubs"), ("5", "hearts"), ("5", "diamonds")},
    {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("6", "diamonds")},
    {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds")},
    {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("8", "diamonds")},
    {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds")},
    {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds")},
    {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("jack", "diamonds")},
    {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("queen", "diamonds")},
    {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("king", "diamonds")},
    {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts"), ("ace", "diamonds")},   
)

FULL_HOUSE_SCENARIOS = (
    {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("10", "diamonds"), ("10", "spades")},
    {("3", "spades"), ("3", "clubs"), ("3", "hearts"), ("9", "diamonds"), ("9", "spades")},
    {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("8", "diamonds"), ("8", "spades")},
    {("5", "spades"), ("5", "clubs"), ("5", "hearts"), ("7", "diamonds"), ("7", "spades")},
    {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("5", "diamonds"), ("5", "spades")},
    {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("4", "diamonds"), ("4", "spades")},
    {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("3", "diamonds"), ("3", "spades")},
    {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("2", "diamonds"), ("2", "spades")},
    {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("ace", "diamonds"), ("ace", "spades")},
    {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("king", "diamonds"), ("king", "spades")},
    {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("jack", "diamonds"), ("jack", "spades")},
    {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("10", "diamonds"), ("10", "spades")},
    {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts"), ("9", "diamonds"), ("9", "spades")},
)

FLUSH_SCENARIOS = (
    {("queen", "spades"), ("3", "spades"), ("5", "spades"), ("10", "spades"), ("ace", "spades")},
    {("6", "clubs"), ("10", "clubs"), ("3", "clubs"), ("9", "clubs"), ("ace", "clubs")},
    {("king", "hearts"), ("10", "hearts"), ("6", "hearts"), ("2", "hearts"), ("4", "hearts")},
    {("king", "diamonds"), ("9", "diamonds"), ("2", "diamonds"), ("10", "diamonds"), ("jack", "diamonds")},
    {("2", "spades"), ("5", "spades"), ("7", "spades"), ("9", "spades"), ("jack", "spades")},
    {("3", "clubs"), ("4", "clubs"), ("6", "clubs"), ("8", "clubs"), ("10", "clubs")},
    {("10", "hearts"), ("2", "hearts"), ("3", "hearts"), ("7", "hearts"), ("king", "hearts")},
    {("jack", "diamonds"), ("10", "diamonds"), ("king", "diamonds"), ("queen", "diamonds"), ("2", "diamonds")}
)

STRAIGHT_SCENARIOS = (
    {("2", "spades"), ("3", "clubs"), ("4", "hearts"), ("5", "diamonds"), ("6", "spades")},
    {("3", "spades"), ("4", "clubs"), ("5", "hearts"), ("6", "diamonds"), ("7", "clubs")},
    {("4", "spades"), ("5", "clubs"), ("6", "hearts"), ("7", "diamonds"), ("8", "hearts")},
    {("5", "spades"), ("6", "clubs"), ("7", "hearts"), ("8", "diamonds"), ("9", "diamonds")},
    {("6", "spades"), ("7", "clubs"), ("8", "hearts"), ("9", "diamonds"), ("10", "spades")},
    {("7", "spades"), ("8", "clubs"), ("9", "hearts"), ("10", "diamonds"), ("jack", "clubs")},
    {("8", "spades"), ("9", "clubs"), ("10", "hearts"), ("jack", "diamonds"), ("queen", "hearts")},
    {("9", "spades"), ("10", "clubs"), ("jack", "hearts"), ("queen", "diamonds"), ("king", "diamonds")}
)

THREE_OF_A_KIND_SCENARIOS = (
    {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("10", "diamonds"), ("3", "spades")},
    {("3", "spades"), ("3", "clubs"), ("3", "hearts"), ("9", "diamonds"), ("4", "spades")},
    {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("8", "diamonds"), ("5", "spades")},
    {("5", "spades"), ("5", "clubs"), ("5", "hearts"), ("7", "diamonds"), ("6", "spades")},
    {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("5", "diamonds"), ("7", "spades")},
    {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("4", "diamonds"), ("8", "spades")},
    {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("3", "diamonds"), ("9", "spades")},
    {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("2", "diamonds"), ("10", "spades")},
    {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("ace", "diamonds"), ("king", "spades")},
    {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("king", "diamonds"), ("ace", "spades")},
    {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("jack", "diamonds"), ("3", "spades")},
    {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("10", "diamonds"), ("5", "spades")},
    {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts"), ("9", "diamonds"), ("4", "spades")},
    # Scenarios with only 4 cards
    {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("10", "diamonds")},
    {("3", "spades"), ("3", "clubs"), ("3", "hearts"), ("9", "diamonds")},
    {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("8", "diamonds")},
    {("5", "spades"), ("5", "clubs"), ("5", "hearts"), ("7", "diamonds")},
    {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("5", "diamonds")},
    {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("4", "diamonds")},
    {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("3", "diamonds")},
    {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("2", "diamonds")},
    {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("ace", "diamonds")},
    {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("king", "diamonds")},
    {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("jack", "diamonds")},
    {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("10", "diamonds")},
    {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts"), ("9", "diamonds")},
    # Scenarios with only 3 cards
    {("2", "spades"), ("2", "clubs"), ("2", "hearts")},
    {("3", "spades"), ("3", "clubs"), ("3", "hearts")},
    {("4", "spades"), ("4", "clubs"), ("4", "hearts")},
    {("5", "spades"), ("5", "clubs"), ("5", "hearts")},
    {("6", "spades"), ("6", "clubs"), ("6", "hearts")},
    {("7", "spades"), ("7", "clubs"), ("7", "hearts")},
    {("8", "spades"), ("8", "clubs"), ("8", "hearts")},
    {("9", "spades"), ("9", "clubs"), ("9", "hearts")},
    {("10", "spades"), ("10", "clubs"), ("10", "hearts")},
    {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts")},
    {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts")},
    {("king", "spades"), ("king", "clubs"), ("king", "hearts")},
    {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts")},
)

TWO_PAIR_SCENARIOS = (
    {("2", "spades"), ("2", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("5", "spades")},
    {("3", "spades"), ("3", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("6", "spades")},
    {("4", "spades"), ("4", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("7", "spades")},
    {("5", "spades"), ("5", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("8", "spades")},
    {("6", "spades"), ("6", "clubs"), ("5", "hearts"), ("5", "diamonds"), ("9", "spades")},
    {("7", "spades"), ("7", "clubs"), ("4", "hearts"), ("4", "diamonds"), ("10", "spades")},
    {("8", "spades"), ("8", "clubs"), ("3", "hearts"), ("3", "diamonds"), ("jack", "spades")},
    {("9", "spades"), ("9", "clubs"), ("2", "hearts"), ("2", "diamonds"), ("queen", "spades")},
    {("10", "spades"), ("10", "clubs"), ("ace", "hearts"), ("ace", "diamonds"), ("king", "spades")},
    {("jack", "spades"), ("jack", "clubs"), ("4", "hearts"), ("4", "diamonds"), ("9", "spades")},
    {("queen", "spades"), ("queen", "clubs"), ("5", "hearts"), ("5", "diamonds"), ("8", "spades")},
    {("king", "spades"), ("king", "clubs"), ("6", "hearts"), ("6", "diamonds"), ("7", "spades")},
    {("ace", "spades"), ("ace", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("6", "spades")},
    # Scenarios with only 4 cards
    {("2", "spades"), ("2", "clubs"), ("10", "hearts"), ("10", "diamonds")},
    {("3", "spades"), ("3", "clubs"), ("9", "hearts"), ("9", "diamonds")},
    {("4", "spades"), ("4", "clubs"), ("8", "hearts"), ("8", "diamonds")},
    {("5", "spades"), ("5", "clubs"), ("7", "hearts"), ("7", "diamonds")},
    {("6", "spades"), ("6", "clubs"), ("5", "hearts"), ("5", "diamonds")},
    {("7", "spades"), ("7", "clubs"), ("4", "hearts"), ("4", "diamonds")},
    {("8", "spades"), ("8", "clubs"), ("3", "hearts"), ("3", "diamonds")},
    {("9", "spades"), ("9", "clubs"), ("2", "hearts"), ("2", "diamonds")},
    {("10", "spades"), ("10", "clubs"), ("ace", "hearts"), ("ace", "diamonds")},
    {("jack", "spades"), ("jack", "clubs"), ("4", "hearts"), ("4", "diamonds")},
    {("queen", "spades"), ("queen", "clubs"), ("5", "hearts"), ("5", "diamonds")},
    {("king", "spades"), ("king", "clubs"), ("6", "hearts"), ("6", "diamonds")},
    {("ace", "spades"), ("ace", "clubs"), ("7", "hearts"), ("7", "diamonds")},
)

ONE_PAIR_SCENARIOS = (
    {("2", "spades"), ("2", "clubs"), ("10", "hearts"), ("8", "diamonds"), ("6", "spades")},
    {("3", "spades"), ("3", "clubs"), ("9", "hearts"), ("7", "diamonds"), ("5", "spades")},
    {("4", "spades"), ("4", "clubs"), ("8", "hearts"), ("6", "diamonds"), ("3", "spades")},
    {("5", "spades"), ("5", "clubs"), ("7", "hearts"), ("4", "diamonds"), ("2", "spades")},
    {("6", "spades"), ("6", "clubs"), ("5", "hearts"), ("3", "diamonds"), ("ace", "spades")},
    {("7", "spades"), ("7", "clubs"), ("4", "hearts"), ("2", "diamonds"), ("king", "spades")},
    {("8", "spades"), ("8", "clubs"), ("3", "hearts"), ("ace", "diamonds"), ("queen", "spades")},
    {("9", "spades"), ("9", "clubs"), ("2", "hearts"), ("king", "diamonds"), ("jack", "spades")},
    {("10", "spades"), ("10", "clubs"), ("ace", "hearts"), ("queen", "diamonds"), ("9", "spades")},
    {("jack", "spades"), ("jack", "clubs"), ("queen", "hearts"), ("9", "diamonds"), ("7", "spades")},
    {("queen", "spades"), ("queen", "clubs"), ("10", "hearts"), ("8", "diamonds"), ("6", "spades")},
    {("king", "spades"), ("king", "clubs"), ("9", "hearts"), ("7", "diamonds"), ("5", "spades")},
    {("ace", "spades"), ("ace", "clubs"), ("8", "hearts"), ("6", "diamonds"), ("4", "spades")},
    # Scenarions with only 4 cards
    {("2", "spades"), ("2", "clubs"), ("10", "hearts"), ("8", "diamonds")},
    {("3", "spades"), ("3", "clubs"), ("9", "hearts"), ("7", "diamonds")},
    {("4", "spades"), ("4", "clubs"), ("8", "hearts"), ("6", "diamonds")},
    {("5", "spades"), ("5", "clubs"), ("7", "hearts"), ("4", "diamonds")},
    {("6", "spades"), ("6", "clubs"), ("5", "hearts"), ("3", "diamonds")},
    {("7", "spades"), ("7", "clubs"), ("4", "hearts"), ("2", "diamonds")},
    {("8", "spades"), ("8", "clubs"), ("3", "hearts"), ("ace", "diamonds")},
    {("9", "spades"), ("9", "clubs"), ("2", "hearts"), ("king", "diamonds")},
    {("10", "spades"), ("10", "clubs"), ("ace", "hearts"), ("queen", "diamonds")},
    {("jack", "spades"), ("jack", "clubs"), ("queen", "hearts"), ("9", "diamonds")},
    {("queen", "spades"), ("queen", "clubs"), ("10", "hearts"), ("8", "diamonds")},
    {("king", "spades"), ("king", "clubs"), ("9", "hearts"), ("7", "diamonds")},
    {("ace", "spades"), ("ace", "clubs"), ("8", "hearts"), ("6", "diamonds")},
    # Scenarios with only 3 cards
    {("2", "spades"), ("2", "clubs"), ("10", "hearts")},
    {("3", "spades"), ("3", "clubs"), ("9", "hearts")},
    {("4", "spades"), ("4", "clubs"), ("8", "hearts")},
    {("5", "spades"), ("5", "clubs"), ("7", "hearts")},
    {("6", "spades"), ("6", "clubs"), ("5", "hearts")},
    {("7", "spades"), ("7", "clubs"), ("4", "hearts")},
    {("8", "spades"), ("8", "clubs"), ("3", "hearts")},
    {("9", "spades"), ("9", "clubs"), ("2", "hearts")},
    {("10", "spades"), ("10", "clubs"), ("ace", "hearts")},
    {("jack", "spades"), ("jack", "clubs"), ("queen", "hearts")},
    {("queen", "spades"), ("queen", "clubs"), ("10", "hearts")},
    {("king", "spades"), ("king", "clubs"), ("9", "hearts")},
    {("ace", "spades"), ("ace", "clubs"), ("8", "hearts")},
)

HIGH_CARD_SCENARIOS = (
    {("2", "spades"), ("4", "clubs"), ("6", "hearts"), ("8", "diamonds"), ("10", "spades")},
    {("3", "spades"), ("5", "clubs"), ("7", "hearts"), ("9", "diamonds"), ("jack", "spades")},
    {("4", "spades"), ("6", "clubs"), ("8", "hearts"), ("10", "diamonds"), ("queen", "spades")},
    {("5", "spades"), ("7", "clubs"), ("9", "hearts"), ("jack", "diamonds"), ("king", "spades")},
    {("6", "spades"), ("8", "clubs"), ("10", "hearts"), ("queen", "diamonds"), ("ace", "spades")},
    {("7", "spades"), ("9", "clubs"), ("jack", "hearts"), ("king", "diamonds"), ("2", "spades")},
    {("8", "spades"), ("10", "clubs"), ("queen", "hearts"), ("ace", "diamonds"), ("3", "spades")},
    {("9", "spades"), ("jack", "clubs"), ("king", "hearts"), ("2", "diamonds"), ("4", "spades")},
    {("10", "spades"), ("queen", "clubs"), ("ace", "hearts"), ("3", "diamonds"), ("5", "spades")},
    {("jack", "spades"), ("king", "clubs"), ("2", "hearts"), ("4", "diamonds"), ("6", "spades")},
    {("queen", "spades"), ("ace", "clubs"), ("3", "hearts"), ("5", "diamonds"), ("7", "spades")},
    {("king", "spades"), ("2", "clubs"), ("4", "hearts"), ("6", "diamonds"), ("8", "spades")},
    {("ace", "spades"), ("3", "clubs"), ("5", "hearts"), ("7", "diamonds"), ("9", "spades")},
    # Scenarios with only 4 cards
    {("2", "spades"), ("4", "clubs"), ("6", "hearts"), ("8", "diamonds")},
    {("3", "spades"), ("5", "clubs"), ("7", "hearts"), ("9", "diamonds")},
    {("4", "spades"), ("6", "clubs"), ("8", "hearts"), ("10", "diamonds")},
    {("5", "spades"), ("7", "clubs"), ("9", "hearts"), ("jack", "diamonds")},
    {("6", "spades"), ("8", "clubs"), ("10", "hearts"), ("queen", "diamonds")},
    {("7", "spades"), ("9", "clubs"), ("jack", "hearts"), ("king", "diamonds")},
    {("8", "spades"), ("10", "clubs"), ("queen", "hearts"), ("ace", "diamonds")},
    {("9", "spades"), ("jack", "clubs"), ("king", "hearts"), ("2", "diamonds")},
    {("10", "spades"), ("queen", "clubs"), ("ace", "hearts"), ("3", "diamonds")},
    {("jack", "spades"), ("king", "clubs"), ("2", "hearts"), ("4", "diamonds")},
    {("queen", "spades"), ("ace", "clubs"), ("3", "hearts"), ("5", "diamonds")},
    {("king", "spades"), ("2", "clubs"), ("4", "hearts"), ("6", "diamonds")},
    {("ace", "spades"), ("3", "clubs"), ("5", "hearts"), ("7", "diamonds")},
    # Scenarios with only 3 cards
    {("2", "spades"), ("4", "clubs"), ("6", "hearts")},
    {("3", "spades"), ("5", "clubs"), ("7", "hearts")},
    {("4", "spades"), ("6", "clubs"), ("8", "hearts")},
    {("5", "spades"), ("7", "clubs"), ("9", "hearts")},
    {("6", "spades"), ("8", "clubs"), ("10", "hearts")},
    {("7", "spades"), ("9", "clubs"), ("jack", "hearts")},
    {("8", "spades"), ("10", "clubs"), ("queen", "hearts")},
    {("9", "spades"), ("jack", "clubs"), ("king", "hearts")},
    {("10", "spades"), ("queen", "clubs"), ("ace", "hearts")},
    {("jack", "spades"), ("king", "clubs"), ("2", "hearts")},
    {("queen", "spades"), ("ace", "clubs"), ("3", "hearts")},
    {("king", "spades"), ("2", "clubs"), ("4", "hearts")},
    {("ace", "spades"), ("3", "clubs"), ("5", "hearts")},
)


######### Testing the Building deck of cards ##############

def test_get_deck_of_cards():
    """ 
    Test get_deck_of_cards function - if all the 52 cards are returned are not
    """
    result = part1.get_deck_of_cards()
    
    assert len(result) == 52, "52 cards do not exist the in the deck"
    for i in vals:
        for j in suits:
            assert (i, j) in result, f"The card {i} {j} does not exist in the deck of cards"

def test_get_deck_of_cards_without_zip():
    """ 
    Test get_deck_of_cards_without_zip function - if all the 52 cards are returned are not
    """
    result = part1.get_deck_of_cards_without_zip()

    assert len(result) == 52, "52 cards do not exist the in the deck"
    for i in vals:
        for j in suits:
            assert (i, j) in result, f"The card {i} {j} does not exist in the deck of cards"

############ Testing Royal Flush ############

def test_check_for_royal_flush():
    royal_flush_scenarios = ROYAL_FLUSH_SCENARIOS

    for scenario in royal_flush_scenarios:
        assert part1.check_for_royal_flush(scenario), "Royal Flush function is not working as expected"

def test_check_for_royal_flush_negative():
    negative_scenarios = (
        *STRAIGHT_FLUSH_SCENARIOS,
        *FOUR_OF_A_KIND_SCENARIOS,
        *FULL_HOUSE_SCENARIOS,
        *FLUSH_SCENARIOS,
        *STRAIGHT_SCENARIOS,
        *THREE_OF_A_KIND_SCENARIOS,
        *TWO_PAIR_SCENARIOS,
        *ONE_PAIR_SCENARIOS,
        *HIGH_CARD_SCENARIOS
    )

    for scenario in negative_scenarios:
        assert part1.check_for_royal_flush(scenario) is False, "Royal Flush function is not working as expected for negative scenarios"


################ Testing Straight Flush ##############

def test_check_for_straight_flush():

    straight_flush_scenarios = []
    for x in range(7):
        for suit in suits:
            straight_flush_scenarios.append({(vals[x], suit), (vals[x + 1], suit), (vals[x + 2], suit), (vals[x + 3], suit), (vals[x + 4], suit)})

    for scenario in straight_flush_scenarios:
        assert part1.check_for_straight_flush(scenario), "Straight Flush function is not working as expected"

def test_check_for_straight_flush_negative():
    negative_scenarios = (
        *FOUR_OF_A_KIND_SCENARIOS,
        *FULL_HOUSE_SCENARIOS,
        *FLUSH_SCENARIOS,
        *STRAIGHT_SCENARIOS,
        *THREE_OF_A_KIND_SCENARIOS,
        *TWO_PAIR_SCENARIOS,
        *ONE_PAIR_SCENARIOS,
        *HIGH_CARD_SCENARIOS
    )

    for scenario in negative_scenarios:
        assert part1.check_for_straight_flush(scenario) is False, "Straight Flush function is not working as expected for negative scenarios"

################ Testing Four of a Kind ##############

def test_check_for_four_of_a_kind():
    four_of_a_kind_scenarios = []
    for x in vals:
        scenario = {(x, suit) for suit in suits}
        scenario.add((random.choice([i for i in vals if i != x]), random.choice(suits)))
        four_of_a_kind_scenarios.append(scenario)

    for scenario in four_of_a_kind_scenarios:
        assert part1.check_for_four_of_a_kind(scenario), "Four of a Kind function is not working as expected"

def test_check_for_four_of_a_kind_negative():
    negative_scenarios = (
        *ROYAL_FLUSH_SCENARIOS,
        *STRAIGHT_FLUSH_SCENARIOS,
        *FULL_HOUSE_SCENARIOS,
        *FLUSH_SCENARIOS,
        *STRAIGHT_SCENARIOS,
        *THREE_OF_A_KIND_SCENARIOS,
        *TWO_PAIR_SCENARIOS,
        *ONE_PAIR_SCENARIOS,
        *HIGH_CARD_SCENARIOS
    )

    for scenario in negative_scenarios:
        assert part1.check_for_four_of_a_kind(scenario) is False, "Four of a Kind function is not working as expected for negative scenarios"

################ Testing check_for_a_full_house #############

def test_check_for_full_house():
    full_house_scenarios = []
    for x in vals:
        scenario = {(x, suit) for suit in ["spades", "clubs", "hearts"]}
        value = random.choice([i for i in vals if i != x])
        scenario.add((value, "spades"))
        scenario.add((value, "clubs"))
        full_house_scenarios.append(scenario)

    for scenario in full_house_scenarios:
        assert part1.check_for_full_house(scenario), "Full House function is not working as expected"

def test_check_for_full_house_negative():
    negative_scenarios = (
        *ROYAL_FLUSH_SCENARIOS,
        *STRAIGHT_FLUSH_SCENARIOS,
        *FOUR_OF_A_KIND_SCENARIOS,
        *FLUSH_SCENARIOS,
        *STRAIGHT_SCENARIOS,
        *THREE_OF_A_KIND_SCENARIOS,
        *TWO_PAIR_SCENARIOS,
        *ONE_PAIR_SCENARIOS,
        *HIGH_CARD_SCENARIOS
    )

    for scenario in negative_scenarios:
        assert part1.check_for_full_house(scenario) is False, "Full House function is not working as expected for negative scenarios"

################ Testing check_for_flush #############

def test_check_for_flush():
    flush_scenarios = FLUSH_SCENARIOS
    
    for scenario in flush_scenarios:
        assert part1.check_for_flush(scenario), "Flush function is not working as expected"

def test_check_for_flush_negative():
    negative_scenarios = (
        *FOUR_OF_A_KIND_SCENARIOS,
        *FULL_HOUSE_SCENARIOS,
        *STRAIGHT_SCENARIOS,
        *THREE_OF_A_KIND_SCENARIOS,
        *TWO_PAIR_SCENARIOS,
        *ONE_PAIR_SCENARIOS,
        *HIGH_CARD_SCENARIOS
    )

    for scenario in negative_scenarios:
        assert part1.check_for_flush(scenario) is False, "Flush function is not working as expected for negative scenarios"

################ Testing check_for_straight #############

def test_check_for_straight():

    straight_scenarios = []

    for index in range(8):
        scenario = set()
        scenario.add((vals[index], random.choice(suits)))
        scenario.add((vals[index + 1], random.choice(suits)))
        scenario.add((vals[index + 2], random.choice(suits)))
        scenario.add((vals[index + 3], random.choice(suits)))
        scenario.add((vals[index + 4], random.choice(suits)))

        straight_scenarios.append(scenario)
    
    for scenario in straight_scenarios:
        assert part1.check_for_straight(scenario), "Straight function is not working as expected"

def test_check_for_straight_negative():
    negative_scenarios = (
        *FOUR_OF_A_KIND_SCENARIOS,
        *FULL_HOUSE_SCENARIOS,
        *FLUSH_SCENARIOS,
        *THREE_OF_A_KIND_SCENARIOS,
        *TWO_PAIR_SCENARIOS,
        *ONE_PAIR_SCENARIOS,
        *HIGH_CARD_SCENARIOS
    )

    for scenario in negative_scenarios:
        assert part1.check_for_straight(scenario) is False, "Straight function is not working as expected for negative scenarios"

################ Testing check_for_three_of_a_kind #############

def test_check_for_three_of_a_kind():

    three_of_a_kind_scenarios = []

    for value in vals:
        scenario = {(value, suits[0]), (value, suits[1]), (value, suits[2])}

        three_of_a_kind_scenarios.append(scenario)
    
    for value in vals:
        scenario = {(value, suits[0]), (value, suits[1]), (value, suits[2])}
        x = random.choice([i for i in vals if i != value])
        scenario.add((x, suits[3]))
        
        three_of_a_kind_scenarios.append(scenario)
    
    for value in vals:
        scenario = {(value, suits[0]), (value, suits[1]), (value, suits[2])}
        x = random.choice([i for i in vals if i != value])
        scenario.add((x, suits[3]))
        scenario.add((random.choice([i for i in vals if i != value and i != x]), suits[3]))
        
        three_of_a_kind_scenarios.append(scenario)
    
    for scenario in three_of_a_kind_scenarios:
        assert part1.check_for_three_of_a_kind(scenario), "Three of a Kind function is not working as expected"

def test_check_for_three_of_a_kind_negative():
    negative_scenarios = (
        *ROYAL_FLUSH_SCENARIOS,
        *STRAIGHT_FLUSH_SCENARIOS,
        *FLUSH_SCENARIOS,
        *STRAIGHT_SCENARIOS,
        *TWO_PAIR_SCENARIOS,
        *ONE_PAIR_SCENARIOS,
        *HIGH_CARD_SCENARIOS
    )

    for scenario in negative_scenarios:
        assert part1.check_for_three_of_a_kind(scenario) is False, "Three of a Kind function is not working as expected for negative scenarios"

################ Testing check_for_two_pair #############

def test_check_for_two_pair():

    two_pair_scenarios = []

    for value in vals:
        x = random.choice([i for i in vals if i != value])

        scenario = {(value, suits[0]), (value, suits[1])}
        scenario.add((x, suits[2]))
        scenario.add((x, suits[3]))

        two_pair_scenarios.append(scenario)
    
    for value in vals:
        x = random.choice([i for i in vals if i != value])

        scenario = {(value, suits[0]), (value, suits[1])}
        scenario.add((x, suits[2]))
        scenario.add((x, suits[3]))

        rand_value = random.choice([i for i in vals if i != value and i != x])
        scenario.add((rand_value, suits[2]))

        two_pair_scenarios.append(scenario)

    for scenario in two_pair_scenarios:
        assert part1.check_for_two_pair(scenario), "Two Pair function is not working as expected"

def test_check_for_two_pair_negative():
    negative_scenarios = (
        *ROYAL_FLUSH_SCENARIOS,
        *STRAIGHT_FLUSH_SCENARIOS,
        *FOUR_OF_A_KIND_SCENARIOS,
        *FULL_HOUSE_SCENARIOS,
        *FLUSH_SCENARIOS,
        *STRAIGHT_SCENARIOS,
        *THREE_OF_A_KIND_SCENARIOS,
        *ONE_PAIR_SCENARIOS,
        *HIGH_CARD_SCENARIOS
    )

    for scenario in negative_scenarios:
        assert part1.check_for_two_pair(scenario) is False, "Two Pair function is not working as expected for negative scenarios"

################ Testing check_for_one_pair #############

def test_check_for_one_pair():

    one_pair_scenarios = []

    for value in vals:
        x = random.choice([i for i in vals if i != value])

        scenario = {(value, suits[0]), (value, suits[1])}
        scenario.add((x, suits[2]))

        one_pair_scenarios.append(scenario)
    
    for value in vals:
        x = random.choice([i for i in vals if i != value])
        y = random.choice([i for i in vals if i != value and i != x])
        scenario = {(value, suits[0]), (value, suits[1])}
        scenario.add((x, suits[2]))
        scenario.add((y, suits[3]))

        one_pair_scenarios.append(scenario)
    
    for value in vals:
        x = random.choice([i for i in vals if i != value])
        y = random.choice([i for i in vals if i != value and i != x])
        z = random.choice([i for i in vals if i != value and i != x and i != y])

        scenario = {(value, suits[0]), (value, suits[1])}
        scenario.add((x, suits[2]))
        scenario.add((y, suits[3]))
        scenario.add((z, suits[0]))

        one_pair_scenarios.append(scenario)

    for scenario in one_pair_scenarios:
        assert part1.check_for_pair(scenario), "One Pair function is not working as expected"

def test_check_for_one_pair_negative():
    negative_scenarios = (
        *ROYAL_FLUSH_SCENARIOS,
        *STRAIGHT_FLUSH_SCENARIOS,
        *FLUSH_SCENARIOS,
        *STRAIGHT_SCENARIOS,
        *HIGH_CARD_SCENARIOS
    )

    for scenario in negative_scenarios:
        assert part1.check_for_pair(scenario) is False, "One Pair function is not working as expected for negative scenarios"

################ Testing get_result_of_poker Validations ##############

def test_get_result_of_poker_with_invalid_type():
    with pytest.raises(TypeError, match=r".*The player_cards should be a set*"):
        part1.get_result_of_poker("invalid player cards 1", "Invalid player cards 2")

def test_get_result_of_poker_with_invalid_card_type():
    player_a_cards = {"this", "is", "invalid", "type", "of", "cards"}
    player_b_cards = {"his", "is", "invalid", "type", "of", "cards"}

    with pytest.raises(TypeError, match=r".*should be a tuple with value and suit in it*"):
        part1.get_result_of_poker(player_a_cards, player_b_cards)

def test_get_result_of_poker_with_invalid_cards():

    invalid_suit_cards = {("10", ""), ("jack", "foobar"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")}

    invalid_value_cards = {("65", "hearts"), ("75", "diamonds"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")}

    with pytest.raises(ValueError, match=r".*not a valid value*"):
        part1.get_result_of_poker(invalid_value_cards, invalid_value_cards)
    
    with pytest.raises(ValueError, match=r".*not a valid suit*"):
        part1.get_result_of_poker(invalid_suit_cards, invalid_suit_cards)

################ Testing get_result_of_poker  ##############

def test_get_result_of_poker_with_royal_flush():
    royal_flush_scenarios = ROYAL_FLUSH_SCENARIOS
    random_scenarios = (
        # Straight Flush Scenarios
        *STRAIGHT_FLUSH_SCENARIOS,
        # four_of_a_kind Scenarios
        *FOUR_OF_A_KIND_SCENARIOS,
        # Flush Scenarios
        *FLUSH_SCENARIOS,
        # Full House Scenarios
        *FULL_HOUSE_SCENARIOS,
        # Straight Scenarios
        *FLUSH_SCENARIOS,
        #STRAIGHT_SCENARIOS
        *STRAIGHT_SCENARIOS,
        # Three of a Kind Scenarios
        *THREE_OF_A_KIND_SCENARIOS,
        # Two Pair Scenarios
        *TWO_PAIR_SCENARIOS,
        # One Pair Scenarios
        *ONE_PAIR_SCENARIOS,
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS
    )

    for player_a_cards in royal_flush_scenarios:
        for player_b_cards in random_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
    
def test_get_result_of_poker_with_straight_flush():
    straight_flush_scenarios = STRAIGHT_FLUSH_SCENARIOS

    player_a_scenarios = (        
        # Four Of a Kind Scenarios
        *FOUR_OF_A_KIND_SCENARIOS,
        # Full House Scenarios
        *FULL_HOUSE_SCENARIOS,
        # Flush Scenarios
        *FLUSH_SCENARIOS,
        # Straight Scenarios
        *STRAIGHT_SCENARIOS,
        # Three of a Kind Scenarios
        *THREE_OF_A_KIND_SCENARIOS,
        # Two Pair Scenarios
        *TWO_PAIR_SCENARIOS,
        # One Pair Scenarios
        *ONE_PAIR_SCENARIOS,
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS
    )

    player_b_scenarios = ROYAL_FLUSH_SCENARIOS

    for player_a_cards in straight_flush_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
    
    for player_a_cards in straight_flush_scenarios:
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_four_of_a_kind():
    four_of_a_kind_scenarios = FOUR_OF_A_KIND_SCENARIOS

    player_a_scenarios = (
        # Full House Scenarios
        *FULL_HOUSE_SCENARIOS,
        # Flush Scenarios
        *FLUSH_SCENARIOS,
        # Straight Scenarios
        *STRAIGHT_SCENARIOS,
        # Three of a Kind Scenarios
        *THREE_OF_A_KIND_SCENARIOS,
        # Two Pair Scenarios
        *TWO_PAIR_SCENARIOS,
        # One Pair Scenarios
        *ONE_PAIR_SCENARIOS,
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        *ROYAL_FLUSH_SCENARIOS,
        # Straight Flush Scenarios
        *STRAIGHT_FLUSH_SCENARIOS
    )

    for player_a_cards in four_of_a_kind_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_full_house():
    full_house_scenarios = FULL_HOUSE_SCENARIOS

    player_a_scenarios = (
        # Flush Scenarios
        *FLUSH_SCENARIOS,
        # Straight Scenarios
        *STRAIGHT_SCENARIOS,
        # Three of a Kind Scenarios
        *THREE_OF_A_KIND_SCENARIOS,
        # Two Pair Scenarios
        *TWO_PAIR_SCENARIOS,
        # One Pair Scenarios
        *ONE_PAIR_SCENARIOS,
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS,
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        *ROYAL_FLUSH_SCENARIOS,
        # Straight Flush Scenarios
        *STRAIGHT_FLUSH_SCENARIOS,
        # Four Of a Kind Scenarios
        *FOUR_OF_A_KIND_SCENARIOS
    )

    for player_a_cards in full_house_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_flush_scenarios():
    flush_scenarios = FLUSH_SCENARIOS

    player_a_scenarios = (
        # Straight Scenarios
        *STRAIGHT_SCENARIOS,
        # Three of a Kind Scenarios
        *THREE_OF_A_KIND_SCENARIOS,
        # Two Pair Scenarios
        *TWO_PAIR_SCENARIOS,
        # One Pair Scenarios
        *ONE_PAIR_SCENARIOS,
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS,
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        *ROYAL_FLUSH_SCENARIOS,
        # Straight Flush Scenarios
        *STRAIGHT_FLUSH_SCENARIOS,
        # Four Of a Kind Scenarios
        *FOUR_OF_A_KIND_SCENARIOS,
        # Full House Scenarios
        *FULL_HOUSE_SCENARIOS,
    )

    for player_a_cards in flush_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_straight_scenarios():
    straight_scenarios = STRAIGHT_SCENARIOS

    player_a_scenarios = (
        # Three of a Kind Scenarios
        *THREE_OF_A_KIND_SCENARIOS,
        # Two Pair Scenarios
        *TWO_PAIR_SCENARIOS,
        # One Pair Scenarios
        *ONE_PAIR_SCENARIOS,
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS,
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        *ROYAL_FLUSH_SCENARIOS,
        # Straight Flush Scenarios
        *STRAIGHT_FLUSH_SCENARIOS,
        # Four Of a Kind Scenarios
        *FOUR_OF_A_KIND_SCENARIOS,
        # Full House Scenarios
        *FULL_HOUSE_SCENARIOS,
        # Flush Scenarios
        *FLUSH_SCENARIOS
    )

    for player_a_cards in straight_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_three_of_a_kind_scenarios():
    three_of_a_kind_scenarios = THREE_OF_A_KIND_SCENARIOS

    player_a_scenarios = (
        # Two Pair Scenarios
        *TWO_PAIR_SCENARIOS,
        # One Pair Scenarios
        *ONE_PAIR_SCENARIOS,
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS,
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        *ROYAL_FLUSH_SCENARIOS,
        # Straight Flush Scenarios
        *STRAIGHT_FLUSH_SCENARIOS,
        # Four Of a Kind Scenarios
        *FOUR_OF_A_KIND_SCENARIOS,
        # Full House Scenarios
        *FULL_HOUSE_SCENARIOS,
        # Flush Scenarios
        *FLUSH_SCENARIOS,
        # Straight Scenarios
        *STRAIGHT_SCENARIOS,
    )

    for player_a_cards in three_of_a_kind_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_two_pair_scenarios():
    two_pair_scenarios = TWO_PAIR_SCENARIOS

    player_a_scenarios = (
        # One Pair Scenarios
        *ONE_PAIR_SCENARIOS,
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS,
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        *ROYAL_FLUSH_SCENARIOS,
        # Straight Flush Scenarios
        *STRAIGHT_FLUSH_SCENARIOS,
        # Four Of a Kind Scenarios
        *FOUR_OF_A_KIND_SCENARIOS,
        # Full House Scenarios
        *FULL_HOUSE_SCENARIOS,
        # Flush Scenarios
        *FLUSH_SCENARIOS,
        # Straight Scenarios
        *STRAIGHT_SCENARIOS,
        # Three Of a Kind Scenarios
        *THREE_OF_A_KIND_SCENARIOS
    )

    for player_a_cards in two_pair_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_one_pair_scenarios():
    one_pair_scenarios = ONE_PAIR_SCENARIOS

    player_a_scenarios = (
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS,
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        *ROYAL_FLUSH_SCENARIOS,
        # Straight Flush Scenarios
        *STRAIGHT_FLUSH_SCENARIOS,
        # Four Of a Kind Scenarios
        *FOUR_OF_A_KIND_SCENARIOS,
        # Full House Scenarios
        *FULL_HOUSE_SCENARIOS,
        # Flush Scenarios
        *FLUSH_SCENARIOS,
        # Straight Scenarios
        *STRAIGHT_SCENARIOS,
        # Three Of a Kind Scenarios
        *THREE_OF_A_KIND_SCENARIOS,
        # Two Pair Scenarios
        *TWO_PAIR_SCENARIOS
    )

    for player_a_cards in one_pair_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_both_players_having_straight_flush():
    player_a_scenarios = (
        (
            {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
            {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        ),
        (
            {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
            {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        ),
        (
            {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
            {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        ),
        (
            {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
            {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        ),
        (
            {("9", "spades"), ("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades")},
            {("6", "clubs"), ("7", "clubs"), ("8", "clubs"), ("9", "clubs"), ("10", "clubs")}
        ),
    )

    player_b_scenarios = (
        (
            {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
            {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")}
        ),
        (
            {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
            {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
        ),
        (
            {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
            {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")}
        ),
        (
            {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
            {("7", "hearts"), ("8", "hearts"), ("9", "hearts"), ("10", "hearts"), ("jack", "hearts")},
        ),
        (
            {("6", "clubs"), ("7", "clubs"), ("8", "clubs"), ("9", "clubs"), ("10", "clubs")},
            {("9", "spades"), ("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades")},
        ),
    )

    for cards in player_a_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player A", "The get_result_of_poker is not working as expected"

    for cards in player_b_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_both_players_having_four_of_a_kind():
    player_a_scenarios = (
        (
            {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("king", "diamonds"), ("6", "spades")},
            {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("8", "spades")},
        ),
        (
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("2", "spades")},
            {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
        ),
        (
            {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
            {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("10", "spades")},
        ),
        (
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("ace", "spades")},
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("king", "spades")},
        ),
        (
            {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("queen", "diamonds"), ("king", "spades")},
            {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("queen", "diamonds"), ("jack", "spades")},
        ),
    )
    player_b_scenarios = (
        (
            {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("8", "spades")},
            {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("king", "diamonds"), ("6", "spades")},
        ),
        (
            {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("2", "spades")},
        ),
        (
            {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("10", "spades")},
            {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
        ),
        (
            {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("jack", "diamonds"), ("9", "spades")},
            {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("jack", "diamonds"), ("queen", "spades")},
        ),
        (
            {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("king", "spades")},
            {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("ace", "spades")},
        ),
    )

    for cards in player_a_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player A", "The get_result_of_poker is not working as expected"

    for cards in player_b_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_both_players_having_full_house():
    player_a_scenarios = (
        (
            {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("king", "diamonds"), ("king", "spades")},
            {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("queen", "diamonds"), ("queen", "spades")},
        ),
        (
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("2", "diamonds"), ("2", "spades")},
            {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("king", "diamonds"), ("king", "spades")},
        ),
        (
            {("5", "spades"), ("5", "clubs"), ("5", "hearts"), ("king", "diamonds"), ("king", "spades")},
            {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("queen", "diamonds"), ("queen", "spades")},
        ),
        (
            {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("ace", "diamonds"), ("ace", "spades")},
            {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("king", "diamonds"), ("king", "spades")},
        ),
        (
            {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("ace", "diamonds"), ("ace", "spades")},
            {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("king", "diamonds"), ("king", "spades")},
        ),
    )
    player_b_scenarios = (
        (
            {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("9", "diamonds"), ("9", "spades")},
            {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("8", "diamonds"), ("8", "spades")},
        ),
        (
            {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("3", "diamonds"), ("3", "spades")},
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("7", "diamonds"), ("7", "spades")},
        ),
        (
            {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("queen", "diamonds"), ("queen", "spades")},
            {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("ace", "diamonds"), ("ace", "spades")},
        ),
        (
            {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("king", "diamonds"), ("king", "spades")},
            {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("ace", "diamonds"), ("ace", "spades")},
        ),
        (
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("jack", "diamonds"), ("jack", "spades")},
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("king", "diamonds"), ("king", "spades")},
        ),
    )

    for cards in player_a_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player A", "The get_result_of_poker is not working as expected"

    for cards in player_b_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_both_players_having_flush():
    player_a_scenarios = (
        (
            {("10", "spades"), ("8", "spades"), ("king", "spades"), ("6", "spades"), ("5", "spades")},
            {("4", "clubs"), ("7", "clubs"), ("queen", "clubs"), ("9", "clubs"), ("3", "clubs")},
        ),
        (
            {("king", "hearts"), ("8", "hearts"), ("10", "hearts"), ("7", "hearts"), ("2", "hearts")},
            {("5", "diamonds"), ("10", "diamonds"), ("queen", "diamonds"), ("jack", "diamonds"), ("9", "diamonds")},
        ),
        (
            {("2", "clubs"), ("4", "clubs"), ("9", "clubs"), ("jack", "clubs"), ("5", "clubs")},
            {("2", "hearts"), ("10", "hearts"), ("9", "hearts"), ("8", "hearts"), ("7", "hearts")},
        ),
        (
            {("ace", "hearts"), ("king", "hearts"), ("2", "hearts"), ("jack", "hearts"), ("10", "hearts")},
            {("ace", "diamonds"), ("king", "diamonds"), ("5", "diamonds"), ("10", "diamonds"), ("3", "diamonds")},
        ),
        (
            {("10", "diamonds"), ("9", "diamonds"), ("7", "diamonds"), ("4", "diamonds"), ("3", "diamonds")},
            {("10", "clubs"), ("9", "clubs"), ("7", "clubs"), ("4", "clubs"), ("2", "clubs")}
        )
    )
    player_b_scenarios = (
        (
            {("6", "diamonds"), ("4", "diamonds"), ("king", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
            {("4", "spades"), ("2", "spades"), ("3", "spades"), ("ace", "spades"), ("5", "spades")},
        ),
        (
            {("7", "clubs"), ("10", "clubs"), ("4", "clubs"), ("3", "clubs"), ("2", "clubs")},
            {("2", "hearts"), ("4", "hearts"), ("jack", "hearts"), ("5", "hearts"), ("8", "hearts")},
        ),
        (
            {("2", "clubs"), ("6", "clubs"), ("5", "clubs"), ("4", "clubs"), ("7", "clubs")},
            {("8", "diamonds"), ("2", "diamonds"), ("3", "diamonds"), ("9", "diamonds"), ("10", "diamonds")},
        ),
        (
            {("2", "clubs"), ("10", "clubs"), ("9", "clubs"), ("4", "clubs"), ("6", "clubs")},
            {("king", "spades"), ("queen", "spades"), ("5", "spades"), ("7", "spades"), ("2", "spades")},
        ),
        (
            {("2", "diamonds"), ("ace", "diamonds"), ("8", "diamonds"), ("6", "diamonds"), ("4", "diamonds")},
            {("2", "hearts"), ("ace", "hearts"), ("8", "hearts"), ("6", "hearts"), ("5", "hearts")}
        ),
    )

    for cards in player_a_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player A", "The get_result_of_poker is not working as expected"

    for cards in player_b_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player B", "The get_result_of_poker is not working as expected"


def test_get_result_of_poker_with_both_players_having_straight():
    player_a_scenarios = (
        (
            {("10", "spades"), ("9", "clubs"), ("8", "hearts"), ("7", "diamonds"), ("6", "spades")},
            {("7", "spades"), ("6", "hearts"), ("4", "diamonds"), ("3", "clubs"), ("5", "spades")},
        ),
        (
            {("7", "spades"), ("6", "clubs"), ("5", "hearts"), ("4", "diamonds"), ("3", "spades")},
            {("6", "spades"), ("5", "hearts"), ("4", "diamonds"), ("3", "clubs"), ("2", "spades")},
        ),
        (
            {("king", "spades"), ("ace", "clubs"), ("queen", "hearts"), ("jack", "diamonds"), ("10", "spades")},
            {("8", "spades"), ("7", "clubs"), ("6", "hearts"), ("5", "diamonds"), ("4", "spades")},
        ),
        (
            {("9", "spades"), ("8", "clubs"), ("7", "hearts"), ("6", "diamonds"), ("5", "spades")},
            {("8", "spades"), ("7", "hearts"), ("6", "diamonds"), ("5", "clubs"), ("4", "spades")},
        ),
        (
            {("6", "clubs"), ("7", "clubs"), ("8", "clubs"), ("9", "diamonds"), ("10", "diamonds")},
            {("5", "spades"), ("6", "spades"), ("7", "spades"), ("8", "hearts"), ("9", "hearts")},
        ),
    )
    player_b_scenarios = (
        (
           {("5", "spades"), ("4", "clubs"), ("3", "hearts"), ("2", "diamonds"), ("6", "spades")},
            {("king", "spades"), ("queen", "hearts"), ("jack", "diamonds"), ("10", "clubs"), ("9", "spades")},
        ),
        (
            {("9", "spades"), ("8", "hearts"), ("7", "diamonds"), ("6", "clubs"), ("5", "spades")},
            {("10", "spades"), ("9", "clubs"), ("8", "hearts"), ("7", "diamonds"), ("6", "spades")},
        ),
        (
            {("5", "spades"), ("4", "clubs"), ("3", "hearts"), ("2", "diamonds"), ("6", "spades")},
            {("8", "spades"), ("7", "clubs"), ("6", "hearts"), ("5", "diamonds"), ("4", "spades")},
        ),
        (
            {("9", "spades"), ("8", "clubs"), ("7", "hearts"), ("6", "diamonds"), ("5", "spades")},
            {("ace", "spades"), ("king", "hearts"), ("queen", "diamonds"), ("jack", "clubs"), ("10", "spades")},
        ),
        (
            {("5", "clubs"), ("4", "clubs"), ("3", "clubs"), ("2", "diamonds"), ("6", "diamonds")},
            {("5", "spades"), ("4", "spades"), ("8", "spades"), ("6", "hearts"), ("7", "hearts")},
        ),
    )

    for cards in player_a_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player A", "The get_result_of_poker is not working as expected"

    for cards in player_b_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player B", "The get_result_of_poker is not working as expected"


def test_get_result_of_poker_with_both_players_having_three_of_a_kind():
    player_a_scenarios = (
        (
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("ace", "diamonds"), ("king", "spades")},
            {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("10", "diamonds"), ("3", "spades")},
        ),
        (
            {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("4", "diamonds"), ("6", "spades")},
            {("5", "spades"), ("5", "clubs"), ("5", "hearts"), ("7", "diamonds"), ("8", "spades")},
        ),
        (
            {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("jack", "diamonds"), ("3", "spades")},
            {("jack", "spades"), ("jack", "clubs"), ("jack", "hearts"), ("king", "diamonds"), ("ace", "spades")},
        ),
        (
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("2", "diamonds"), ("king", "spades")},
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("9", "diamonds"), ("8", "spades")},
        ),
        (
            {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("10", "diamonds"), ("5", "spades")},
            {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("8", "diamonds"), ("9", "spades")},
        ),
    )
    player_b_scenarios = (
        
        (
            {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("8", "diamonds"), ("5", "spades")},
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("ace", "diamonds"), ("king", "spades")},
        ),
        (
            {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("3", "diamonds"), ("9", "spades")},
            {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("2", "diamonds"), ("10", "spades")},
        ),
        (
            {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("ace", "diamonds"), ("king", "spades")},
            {("queen", "spades"), ("queen", "clubs"), ("queen", "hearts"), ("jack", "diamonds"), ("3", "spades")},
        ),
        (
            {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("9", "diamonds"), ("8", "spades")},
            {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("2", "diamonds"), ("king", "spades")},
        ),
        (
            {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("7", "diamonds"), ("9", "spades")},
            {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("10", "diamonds"), ("5", "spades")},
        ),
    )

    for cards in player_a_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player A", "The get_result_of_poker is not working as expected"

    for cards in player_b_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_both_players_having_two_pair():
    player_a_scenarios = (
        (
            {("2", "spades"), ("2", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("5", "spades")},
            {("3", "spades"), ("3", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("6", "spades")},
        ),
        (
            {("9", "spades"), ("9", "clubs"), ("2", "hearts"), ("2", "diamonds"), ("queen", "spades")},
            {("7", "spades"), ("7", "clubs"), ("4", "hearts"), ("4", "diamonds"), ("10", "spades")},
        ),
        (
            {("10", "spades"), ("10", "clubs"), ("ace", "hearts"), ("ace", "diamonds"), ("king", "spades")},
            {("jack", "spades"), ("jack", "clubs"), ("4", "hearts"), ("4", "diamonds"), ("9", "spades")},
        ),
        (
            {("5", "spades"), ("5", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("10", "spades")},
            {("5", "diamonds"), ("5", "hearts"), ("7", "clubs"), ("7", "spades"), ("8", "spades")},
        ),
        (
            {("jack", "spades"), ("jack", "clubs"), ("4", "hearts"), ("4", "diamonds"), ("ace", "spades")},
            {("jack", "diamonds"), ("jack", "hearts"), ("4", "clubs"), ("4", "spades"), ("king", "spades")},
        ),
    )
    player_b_scenarios = (
        (
            {("3", "spades"), ("3", "clubs"), ("6", "hearts"), ("6", "diamonds"), ("9", "spades")},
            {("2", "spades"), ("2", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("5", "spades")},
        ),
        (
            {("5", "spades"), ("5", "clubs"), ("4", "hearts"), ("4", "diamonds"), ("10", "spades")},
            {("10", "spades"), ("10", "clubs"), ("2", "hearts"), ("2", "diamonds"), ("queen", "spades")},
        ),
        (
            {("jack", "spades"), ("jack", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("king", "spades")},
            {("king", "spades"), ("king", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("9", "spades")},
        ),
        (
            {("6", "spades"), ("6", "clubs"), ("4", "hearts"), ("4", "diamonds"), ("10", "spades")},
            {("6", "diamonds"), ("6", "hearts"), ("4", "clubs"), ("4", "spades"), ("king", "spades")},
        ),
        (
            {("queen", "spades"), ("queen", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("5", "spades")},
            {("queen", "diamonds"), ("queen", "hearts"), ("8", "clubs"), ("8", "spades"), ("10", "spades")},
        ),
    )

    for cards in player_a_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player A", "The get_result_of_poker is not working as expected"

    for cards in player_b_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_both_players_having_one_pair():
    player_a_scenarios = (
        (
            {("7", "spades"), ("7", "clubs"), ("4", "hearts"), ("2", "diamonds"), ("king", "spades")},
            {("5", "spades"), ("5", "clubs"), ("7", "hearts"), ("4", "diamonds"), ("2", "spades")},
        ),
        (
            {("8", "spades"), ("8", "clubs"), ("3", "hearts"), ("ace", "diamonds"), ("queen", "spades")},
            {("4", "spades"), ("4", "clubs"), ("8", "hearts"), ("6", "diamonds"), ("3", "spades")},
        ),
        (
            {("queen", "spades"), ("queen", "clubs"), ("10", "hearts"), ("8", "diamonds"), ("6", "spades")},
            {("9", "spades"), ("9", "clubs"), ("2", "hearts"), ("king", "diamonds"), ("jack", "spades")},
        ),
        (
            {("3", "spades"), ("3", "clubs"), ("10", "hearts"), ("7", "diamonds"), ("5", "spades")},
            {("3", "diamonds"), ("3", "hearts"), ("9", "hearts"), ("5", "diamonds"), ("2", "spades")},
        ),
        (
            {("king", "spades"), ("king", "clubs"), ("ace", "hearts"), ("7", "diamonds"), ("5", "spades")},
            {("king", "diamonds"), ("king", "hearts"), ("jack", "hearts"), ("10", "diamonds"), ("5", "spades")},
        ),
    )
    player_b_scenarios = (
        (
            {("7", "spades"), ("7", "clubs"), ("4", "hearts"), ("2", "diamonds"), ("king", "spades")},
            {("10", "spades"), ("10", "clubs"), ("7", "hearts"), ("4", "diamonds"), ("2", "spades")},
        ),
        (
            {("4", "spades"), ("4", "clubs"), ("8", "hearts"), ("6", "diamonds"), ("3", "spades")},
            {("9", "spades"), ("9", "clubs"), ("3", "hearts"), ("ace", "diamonds"), ("queen", "spades")},
        ),
        (
            {("9", "spades"), ("9", "clubs"), ("2", "hearts"), ("king", "diamonds"), ("jack", "spades")},
            {("jack", "spades"), ("jack", "clubs"), ("10", "hearts"), ("8", "diamonds"), ("6", "spades")},
        ),
        (
            {("4", "spades"), ("4", "clubs"), ("7", "hearts"), ("3", "diamonds"), ("5", "spades")},
            {("4", "diamonds"), ("4", "hearts"), ("8", "hearts"), ("5", "diamonds"), ("2", "spades")},
        ),
        (
            {("queen", "spades"), ("queen", "clubs"), ("jack", "hearts"), ("7", "diamonds"), ("5", "spades")},
            {("queen", "diamonds"), ("queen", "hearts"), ("king", "hearts"), ("10", "diamonds"), ("5", "spades")},
        ),
    )

    for cards in player_a_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player A", "The get_result_of_poker is not working as expected"

    for cards in player_b_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_both_players_having_high_card():
    player_a_scenarios = (
        (
            {("5", "spades"), ("7", "clubs"), ("9", "hearts"), ("jack", "diamonds"), ("king", "spades")},
            {("2", "spades"), ("4", "clubs"), ("6", "hearts"), ("8", "diamonds"), ("10", "spades")},
        ),
        (
            {("6", "spades"), ("8", "clubs"), ("10", "hearts"), ("queen", "diamonds"), ("ace", "spades")},
            {("5", "spades"), ("7", "clubs"), ("9", "hearts"), ("jack", "diamonds"), ("king", "spades")},
        ),
        (
            {("3", "spades"), ("5", "clubs"), ("7", "hearts"), ("9", "diamonds"), ("jack", "spades")},
            {("2", "spades"), ("4", "clubs"), ("6", "hearts"), ("8", "diamonds"), ("10", "spades")},
        ),
        (
            {("3", "spades"), ("5", "clubs"), ("7", "hearts"), ("9", "diamonds"), ("jack", "spades")},
            {("2", "spades"), ("4", "clubs"), ("6", "hearts"), ("9", "clubs"), ("jack", "hearts")},
        ),
        (
            {("ace", "spades"), ("3", "clubs"), ("5", "hearts"), ("10", "diamonds"), ("9", "spades")},
            {("ace", "hearts"), ("3", "hearts"), ("5", "clubs"), ("9", "diamonds"), ("4", "spades")},
        ),
    )
    player_b_scenarios = (
        (
            {("2", "spades"), ("4", "clubs"), ("6", "hearts"), ("8", "diamonds"), ("10", "spades")},
            {("5", "spades"), ("7", "clubs"), ("9", "hearts"), ("jack", "diamonds"), ("king", "spades")},
        ),
        (
            {("5", "spades"), ("7", "clubs"), ("9", "hearts"), ("jack", "diamonds"), ("king", "spades")},
            {("6", "spades"), ("8", "clubs"), ("10", "hearts"), ("queen", "diamonds"), ("ace", "spades")},
        ),
        (
            {("2", "spades"), ("4", "clubs"), ("6", "hearts"), ("8", "diamonds"), ("10", "spades")},
            {("3", "spades"), ("5", "clubs"), ("7", "hearts"), ("9", "diamonds"), ("jack", "spades")},
        ),
        (
            {("2", "spades"), ("4", "clubs"), ("6", "hearts"), ("9", "clubs"), ("jack", "hearts")},
            {("3", "spades"), ("5", "clubs"), ("7", "hearts"), ("9", "diamonds"), ("jack", "spades")},
        ),
        (
            {("ace", "hearts"), ("3", "hearts"), ("5", "clubs"), ("9", "diamonds"), ("4", "spades")},
            {("ace", "spades"), ("3", "clubs"), ("5", "hearts"), ("10", "diamonds"), ("9", "spades")},
        ),
    )

    for cards in player_a_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player A", "The get_result_of_poker is not working as expected"

    for cards in player_b_scenarios:
        winner = part1.get_result_of_poker(cards[0], cards[1])
        assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_a_tie():
    scenarios = (
        # Royal Flush Scenarios
        *ROYAL_FLUSH_SCENARIOS,
        # Straight Flush Scenarios
        *STRAIGHT_FLUSH_SCENARIOS,
        # Four Of a Kind
        *FOUR_OF_A_KIND_SCENARIOS,
        # Full House Scenarios
        *FULL_HOUSE_SCENARIOS,
        # Flush Scenarios
        *FLUSH_SCENARIOS,
        # Straight Scenarios
        *STRAIGHT_SCENARIOS,
        # Three of a Kind Scenarios
        *THREE_OF_A_KIND_SCENARIOS,
        # Two Pair Scenarios
        *TWO_PAIR_SCENARIOS,
        # One Pair Scenarios
        *ONE_PAIR_SCENARIOS,
        # High Card Scenarios
        *HIGH_CARD_SCENARIOS
    )

    for cards in scenarios:
        winner = part1.get_result_of_poker(cards, cards)
        assert winner == "Player A and Player B", "The get_result_of_poker is not working as expected"