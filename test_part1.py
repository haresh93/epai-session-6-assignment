import pytest
import part1
import random

vals = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]

suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]

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
    royal_flush_scenarios = (
        {("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades"), ("ace", "spades")},
        {("10", "clubs"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
        {("10", "hearts"), ("jack", "hearts"), ("queen", "hearts"), ("king", "hearts"), ("ace", "hearts")},
        {("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")}
    )

    for scenario in royal_flush_scenarios:
        assert part1.check_for_royal_flush(scenario), "Royal Flush function is not working as expected"

def test_check_for_royal_flush_negative():
    negative_scenarios = (
        {("10", "hearts"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
        {("10", "hearts"), ("jack", "spades"), ("queen", "clubs"), ("king", "diamonds"), ("ace", "hearts")},
        {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        {("5", "diamonds"), ("6", "diamonds"), ("8", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")}
    )

    for scenario in negative_scenarios:
        assert part1.check_for_royal_flush(scenario) is False, "Royal Flush function is not working as expected for negative scenarios"


################ Testing Straight Flush ##############

def test_check_for_straight_flush():
    straight_flush_scenarios = (
        {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
        {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
        {("7", "clubs"), ("8", "clubs"), ("9", "clubs"), ("10", "clubs"), ("jack", "clubs")},
        {("8", "hearts"), ("9", "hearts"), ("10", "hearts"), ("jack", "hearts"), ("queen", "hearts")},
        {("9", "diamonds"), ("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds")}
    )

    for scenario in straight_flush_scenarios:
        assert part1.check_for_straight_flush(scenario), "Straight Flush function is not working as expected"

def test_check_for_straight_flush_negative():
    negative_scenarios = (
        {("2", "spades"), ("3", "clubs"), ("4", "spades"), ("5", "diamonds"), ("6", "spades")},
        {("2", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("3", "hearts"), ("5", "spades"), ("6", "clubs"), ("7", "diamonds"), ("8", "hearts")},
        {("king", "spades"), ("jack", "diamonds"), ("7", "hearts"), ("8", "diamonds"), ("9", "diamonds")}
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
        {("queen", "spades"), ("queen", "clubs"), ("queen", "spades"), ("king", "diamonds"), ("king", "spades")},
        {("2", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("3", "hearts"), ("5", "spades"), ("6", "clubs"), ("7", "diamonds"), ("8", "hearts")},
        {("king", "spades"), ("jack", "diamonds"), ("7", "hearts"), ("8", "diamonds"), ("9", "diamonds")}
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
        {("queen", "spades"), ("queen", "clubs"), ("queen", "spades"), ("king", "diamonds"), ("king", "spades")},
        {("2", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("3", "hearts"), ("5", "spades"), ("6", "clubs"), ("7", "diamonds"), ("8", "hearts")},
        {("king", "spades"), ("jack", "diamonds"), ("7", "hearts"), ("8", "diamonds"), ("9", "diamonds")}
    )

    for scenario in negative_scenarios:
        assert part1.check_for_full_house(scenario) is False, "Full House function is not working as expected for negative scenarios"

################ Testing check_for_flush #############

def test_check_for_flush():
    flush_scenarios = (
        {("queen", "spades"), ("3", "spades"), ("5", "spades"), ("10", "spades"), ("ace", "spades")},
        {("6", "clubs"), ("10", "clubs"), ("3", "clubs"), ("9", "clubs"), ("ace", "clubs")},
        {("king", "hearts"), ("10", "hearts"), ("6", "hearts"), ("2", "hearts"), ("4", "hearts")},
        {("king", "diamonds"), ("9", "diamonds"), ("2", "diamonds"), ("10", "diamonds"), ("jack", "diamonds")},
        {("2", "spades"), ("5", "spades"), ("7", "spades"), ("9", "spades"), ("jack", "spades")},
        {("3", "clubs"), ("4", "clubs"), ("6", "clubs"), ("8", "clubs"), ("10", "clubs")},
        {("10", "hearts"), ("2", "hearts"), ("3", "hearts"), ("7", "hearts"), ("king", "hearts")},
        {("jack", "diamonds"), ("10", "diamonds"), ("king", "diamonds"), ("queen", "diamonds"), ("2", "diamonds")}
    )
    
    for scenario in flush_scenarios:
        assert part1.check_for_flush(scenario), "Flush function is not working as expected"

def test_check_for_flush_negative():
    negative_scenarios = (
        {("queen", "spades"), ("queen", "clubs"), ("queen", "spades"), ("king", "diamonds"), ("king", "spades")},
        {("2", "clubs"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds"), ("7", "clubs")},
        {("3", "hearts"), ("5", "spades"), ("6", "clubs"), ("7", "diamonds"), ("8", "hearts")},
        {("king", "spades"), ("jack", "diamonds"), ("7", "hearts"), ("8", "diamonds"), ("9", "diamonds")},
        {("2", "spades"), ("8", "diamonds"), ("3", "hearts"), ("10", "diamonds"), ("6", "diamonds")}
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
        {("queen", "spades"), ("queen", "clubs"), ("queen", "spades"), ("king", "diamonds"), ("king", "spades")},
        {("2", "clubs"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds"), ("7", "clubs")},
        {("3", "hearts"), ("5", "spades"), ("6", "clubs"), ("7", "diamonds"), ("8", "hearts")},
        {("king", "spades"), ("jack", "diamonds"), ("7", "hearts"), ("8", "diamonds"), ("9", "diamonds")},
        {("2", "spades"), ("8", "diamonds"), ("3", "hearts"), ("10", "diamonds"), ("6", "diamonds")}
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
        {("queen", "spades"), ("queen", "clubs"), ("queen", "spades"), ("king", "diamonds"), ("king", "spades")},
        {("2", "clubs"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds"), ("7", "clubs")},
        {("3", "hearts"), ("5", "spades"), ("6", "clubs"), ("7", "diamonds"), ("8", "hearts")},
        {("king", "spades"), ("jack", "diamonds"), ("7", "hearts"), ("8", "diamonds"), ("9", "diamonds")},
        {("2", "spades"), ("8", "diamonds"), ("3", "hearts"), ("10", "diamonds"), ("6", "diamonds")}
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
        {("queen", "spades"), ("2", "clubs"), ("3", "spades"), ("king", "diamonds"), ("king", "spades")},
        {("2", "clubs"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds"), ("7", "clubs")},
        {("3", "hearts"), ("5", "spades"), ("6", "clubs"), ("7", "diamonds"), ("8", "hearts")},
        {("king", "spades"), ("jack", "diamonds"), ("7", "hearts"), ("8", "diamonds"), ("9", "diamonds")},
        {("2", "spades"), ("8", "diamonds"), ("3", "hearts"), ("10", "diamonds"), ("6", "diamonds")}
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
        {("queen", "spades"), ("2", "clubs"), ("3", "spades"), ("jack", "diamonds"), ("king", "spades")},
        {("2", "clubs"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds"), ("7", "clubs")},
        {("3", "hearts"), ("5", "spades"), ("6", "clubs"), ("7", "diamonds"), ("8", "hearts")},
        {("king", "spades"), ("jack", "diamonds"), ("7", "hearts"), ("8", "diamonds"), ("9", "diamonds")},
        {("2", "spades"), ("8", "diamonds"), ("3", "hearts"), ("10", "diamonds"), ("6", "diamonds")}
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
    royal_flush_scenarios = (
        {("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades"), ("ace", "spades")},
        {("10", "clubs"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
        {("10", "hearts"), ("jack", "hearts"), ("queen", "hearts"), ("king", "hearts"), ("ace", "hearts")},
        {("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")}
    )
    random_scenarios = (
        # four_of_a_kind Scenarios
        {("2", "spades"), ("2", "clubs"), ("2", "hearts"), ("2", "diamonds"), ("6", "spades")},
        {("3", "spades"), ("3", "clubs"), ("3", "hearts"), ("3", "diamonds"), ("8", "spades")},
        {("4", "spades"), ("4", "clubs"), ("4", "hearts"), ("4", "diamonds"), ("10", "spades")},
        {("5", "spades"), ("5", "clubs"), ("5", "hearts"), ("5", "diamonds"), ("3", "spades")},
        {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("6", "diamonds"), ("5", "spades")},
        # Straight Flush Scenarios
        {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
        {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
        # Flush Scenarios
        {("2", "spades"), ("8", "spades"), ("3", "spades"), ("5", "spades"), ("ace", "spades")},
        {("5", "hearts"), ("7", "hearts"), ("2", "hearts"), ("9", "hearts"), ("king", "hearts")},
        {("6", "clubs"), ("9", "clubs"), ("jack", "clubs"), ("10", "clubs"), ("3", "clubs")},
        {("queen", "diamonds"), ("9", "diamonds"), ("5", "diamonds"), ("7", "diamonds"), ("king", "diamonds")},
        {("5", "spades"), ("9", "spades"), ("4", "spades"), ("10", "spades"), ("ace", "spades")},
        # Straight Scenarios
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("3", "spades"), ("4", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("4", "spades"), ("5", "hearts"), ("6", "clubs"), ("7", "spades"), ("8", "diamonds")},
        {("5", "spades"), ("6", "hearts"), ("7", "clubs"), ("8", "spades"), ("9", "diamonds")},
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Three of a Kind Scenarios
        {("3", "spades"), ("3", "hearts"), ("3", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("5", "spades"), ("5", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("8", "clubs"), ("7", "spades"), ("10", "diamonds")},
        {("9", "spades"), ("9", "hearts"), ("9", "clubs"), ("5", "spades"), ("4", "diamonds")},
        {("10", "spades"), ("10", "hearts"), ("10", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Two Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("6", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("10", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("ace", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("10", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("5", "spades"), ("8", "diamonds")},
        # One Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
        # High Card Scenarios
        {("5", "spades"), ("9", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("king", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("jack", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("king", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("2", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
    )

    for player_a_cards in royal_flush_scenarios:
        for player_b_cards in random_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
    
def test_get_result_of_poker_with_straight_flush():
    straight_flush_scenarios = (
        {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
        {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
    )

    player_a_scenarios = (
        # Four Of a Kind Scenarios
        {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("king", "diamonds"), ("6", "spades")},
        {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("8", "spades")},
        {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("10", "spades")},
        {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
        {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("5", "spades")},
        # Flush Scenarios
        {("2", "spades"), ("8", "spades"), ("3", "spades"), ("5", "spades"), ("ace", "spades")},
        {("5", "hearts"), ("7", "hearts"), ("2", "hearts"), ("9", "hearts"), ("king", "hearts")},
        {("6", "clubs"), ("9", "clubs"), ("jack", "clubs"), ("10", "clubs"), ("3", "clubs")},
        {("queen", "diamonds"), ("9", "diamonds"), ("5", "diamonds"), ("7", "diamonds"), ("king", "diamonds")},
        {("5", "spades"), ("9", "spades"), ("4", "spades"), ("10", "spades"), ("ace", "spades")},
        # Straight Scenarios
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("3", "spades"), ("4", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("4", "spades"), ("5", "hearts"), ("6", "clubs"), ("7", "spades"), ("8", "diamonds")},
        {("5", "spades"), ("6", "hearts"), ("7", "clubs"), ("8", "spades"), ("9", "diamonds")},
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Three of a Kind Scenarios
        {("3", "spades"), ("3", "hearts"), ("3", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("5", "spades"), ("5", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("8", "clubs"), ("7", "spades"), ("10", "diamonds")},
        {("9", "spades"), ("9", "hearts"), ("9", "clubs"), ("5", "spades"), ("4", "diamonds")},
        {("10", "spades"), ("10", "hearts"), ("10", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Two Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("6", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("10", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("ace", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("10", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("5", "spades"), ("8", "diamonds")},
        # One Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
        # High Card Scenarios
        {("5", "spades"), ("9", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("king", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("jack", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("king", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("2", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
    )

    player_b_scenarios = (
        {("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades"), ("ace", "spades")},
        {("10", "clubs"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
        {("10", "hearts"), ("jack", "hearts"), ("queen", "hearts"), ("king", "hearts"), ("ace", "hearts")},
        {("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")}
    )

    for player_a_cards in straight_flush_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
    
    for player_a_cards in straight_flush_scenarios:
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_four_of_a_kind():
    four_of_a_kind_scenarios = (
        {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("king", "diamonds"), ("6", "spades")},
        {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("8", "spades")},
        {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("10", "spades")},
        {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
        {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("5", "spades")},
    )

    player_a_scenarios = (
        # Flush Scenarios
        {("2", "spades"), ("8", "spades"), ("3", "spades"), ("5", "spades"), ("ace", "spades")},
        {("5", "hearts"), ("7", "hearts"), ("2", "hearts"), ("9", "hearts"), ("king", "hearts")},
        {("6", "clubs"), ("9", "clubs"), ("jack", "clubs"), ("10", "clubs"), ("3", "clubs")},
        {("queen", "diamonds"), ("9", "diamonds"), ("5", "diamonds"), ("7", "diamonds"), ("king", "diamonds")},
        {("5", "spades"), ("9", "spades"), ("4", "spades"), ("10", "spades"), ("ace", "spades")},
        # Straight Scenarios
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("3", "spades"), ("4", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("4", "spades"), ("5", "hearts"), ("6", "clubs"), ("7", "spades"), ("8", "diamonds")},
        {("5", "spades"), ("6", "hearts"), ("7", "clubs"), ("8", "spades"), ("9", "diamonds")},
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Three of a Kind Scenarios
        {("3", "spades"), ("3", "hearts"), ("3", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("5", "spades"), ("5", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("8", "clubs"), ("7", "spades"), ("10", "diamonds")},
        {("9", "spades"), ("9", "hearts"), ("9", "clubs"), ("5", "spades"), ("4", "diamonds")},
        {("10", "spades"), ("10", "hearts"), ("10", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Two Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("6", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("10", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("ace", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("10", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("5", "spades"), ("8", "diamonds")},
        # One Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
        # High Card Scenarios
        {("5", "spades"), ("9", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("king", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("jack", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("king", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("2", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        {("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades"), ("ace", "spades")},
        {("10", "clubs"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
        {("10", "hearts"), ("jack", "hearts"), ("queen", "hearts"), ("king", "hearts"), ("ace", "hearts")},
        {("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")},
        # Straight Flush Scenarios
        {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
        {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
    )

    for player_a_cards in four_of_a_kind_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_full_house():
    full_house_scenarios = (
        {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("queen", "diamonds"), ("queen", "spades")},
        {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("8", "diamonds"), ("8", "spades")},
        {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("10", "diamonds"), ("10", "spades")},
        {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("2", "diamonds"), ("2", "spades")},
        {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts"), ("10", "diamonds"), ("10", "spades")},
    )

    player_a_scenarios = (
        # Flush Scenarios
        {("2", "spades"), ("8", "spades"), ("3", "spades"), ("5", "spades"), ("ace", "spades")},
        {("5", "hearts"), ("7", "hearts"), ("2", "hearts"), ("9", "hearts"), ("king", "hearts")},
        {("6", "clubs"), ("9", "clubs"), ("jack", "clubs"), ("10", "clubs"), ("3", "clubs")},
        {("queen", "diamonds"), ("9", "diamonds"), ("5", "diamonds"), ("7", "diamonds"), ("king", "diamonds")},
        {("5", "spades"), ("9", "spades"), ("4", "spades"), ("10", "spades"), ("ace", "spades")},
        # Straight Scenarios
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("3", "spades"), ("4", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("4", "spades"), ("5", "hearts"), ("6", "clubs"), ("7", "spades"), ("8", "diamonds")},
        {("5", "spades"), ("6", "hearts"), ("7", "clubs"), ("8", "spades"), ("9", "diamonds")},
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Three of a Kind Scenarios
        {("3", "spades"), ("3", "hearts"), ("3", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("5", "spades"), ("5", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("8", "clubs"), ("7", "spades"), ("10", "diamonds")},
        {("9", "spades"), ("9", "hearts"), ("9", "clubs"), ("5", "spades"), ("4", "diamonds")},
        {("10", "spades"), ("10", "hearts"), ("10", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Two Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("6", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("10", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("ace", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("10", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("5", "spades"), ("8", "diamonds")},
        # One Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
        # High Card Scenarios
        {("5", "spades"), ("9", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("king", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("jack", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("king", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("2", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        {("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades"), ("ace", "spades")},
        {("10", "clubs"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
        {("10", "hearts"), ("jack", "hearts"), ("queen", "hearts"), ("king", "hearts"), ("ace", "hearts")},
        {("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")},
        # Straight Flush Scenarios
        {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
        {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
    )

    for player_a_cards in full_house_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_flush_scenarios():
    flush_scenarios = (
        # Flush Scenarios
        {("2", "spades"), ("8", "spades"), ("3", "spades"), ("5", "spades"), ("ace", "spades")},
        {("5", "hearts"), ("7", "hearts"), ("2", "hearts"), ("9", "hearts"), ("king", "hearts")},
        {("6", "clubs"), ("9", "clubs"), ("jack", "clubs"), ("10", "clubs"), ("3", "clubs")},
        {("queen", "diamonds"), ("9", "diamonds"), ("5", "diamonds"), ("7", "diamonds"), ("king", "diamonds")},
        {("5", "spades"), ("9", "spades"), ("4", "spades"), ("10", "spades"), ("ace", "spades")},
    )

    player_a_scenarios = (
        # Straight Scenarios
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("3", "spades"), ("4", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("4", "spades"), ("5", "hearts"), ("6", "clubs"), ("7", "spades"), ("8", "diamonds")},
        {("5", "spades"), ("6", "hearts"), ("7", "clubs"), ("8", "spades"), ("9", "diamonds")},
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Three of a Kind Scenarios
        {("3", "spades"), ("3", "hearts"), ("3", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("5", "spades"), ("5", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("8", "clubs"), ("7", "spades"), ("10", "diamonds")},
        {("9", "spades"), ("9", "hearts"), ("9", "clubs"), ("5", "spades"), ("4", "diamonds")},
        {("10", "spades"), ("10", "hearts"), ("10", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Two Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("6", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("10", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("ace", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("10", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("5", "spades"), ("8", "diamonds")},
        # One Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
        # High Card Scenarios
        {("5", "spades"), ("9", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("king", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("jack", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("king", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("2", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        {("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades"), ("ace", "spades")},
        {("10", "clubs"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
        {("10", "hearts"), ("jack", "hearts"), ("queen", "hearts"), ("king", "hearts"), ("ace", "hearts")},
        {("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")},
        # Straight Flush Scenarios
        {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
        {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
        # Four Of a Kind Scenarios
        {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("king", "diamonds"), ("6", "spades")},
        {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("8", "spades")},
        {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("10", "spades")},
        {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
        {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("5", "spades")},
        # Full House Scenarios
        {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("queen", "diamonds"), ("queen", "spades")},
        {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("8", "diamonds"), ("8", "spades")},
        {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("10", "diamonds"), ("10", "spades")},
        {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("2", "diamonds"), ("2", "spades")},
        {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts"), ("10", "diamonds"), ("10", "spades")},
    )

    for player_a_cards in flush_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_straight_scenarios():
    straight_scenarios = (
        # Straight Scenarios
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("3", "spades"), ("4", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("4", "spades"), ("5", "hearts"), ("6", "clubs"), ("7", "spades"), ("8", "diamonds")},
        {("5", "spades"), ("6", "hearts"), ("7", "clubs"), ("8", "spades"), ("9", "diamonds")},
        {("2", "spades"), ("3", "hearts"), ("4", "clubs"), ("5", "spades"), ("6", "diamonds")},
    )

    player_a_scenarios = (
        # Three of a Kind Scenarios
        {("3", "spades"), ("3", "hearts"), ("3", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("5", "spades"), ("5", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("8", "clubs"), ("7", "spades"), ("10", "diamonds")},
        {("9", "spades"), ("9", "hearts"), ("9", "clubs"), ("5", "spades"), ("4", "diamonds")},
        {("10", "spades"), ("10", "hearts"), ("10", "clubs"), ("5", "spades"), ("6", "diamonds")},
        # Two Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("6", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("10", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("ace", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("10", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("5", "spades"), ("8", "diamonds")},
        # One Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
        # High Card Scenarios
        {("5", "spades"), ("9", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("king", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("jack", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("king", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("2", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        {("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades"), ("ace", "spades")},
        {("10", "clubs"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
        {("10", "hearts"), ("jack", "hearts"), ("queen", "hearts"), ("king", "hearts"), ("ace", "hearts")},
        {("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")},
        # Straight Flush Scenarios
        {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
        {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
        # Four Of a Kind Scenarios
        {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("king", "diamonds"), ("6", "spades")},
        {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("8", "spades")},
        {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("10", "spades")},
        {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
        {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("5", "spades")},
        # Full House Scenarios
        {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("queen", "diamonds"), ("queen", "spades")},
        {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("8", "diamonds"), ("8", "spades")},
        {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("10", "diamonds"), ("10", "spades")},
        {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("2", "diamonds"), ("2", "spades")},
        {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts"), ("10", "diamonds"), ("10", "spades")},
        # Flush Scenarios
        {("2", "spades"), ("8", "spades"), ("3", "spades"), ("5", "spades"), ("ace", "spades")},
        {("5", "hearts"), ("7", "hearts"), ("2", "hearts"), ("9", "hearts"), ("king", "hearts")},
        {("6", "clubs"), ("9", "clubs"), ("jack", "clubs"), ("10", "clubs"), ("3", "clubs")},
        {("queen", "diamonds"), ("9", "diamonds"), ("5", "diamonds"), ("7", "diamonds"), ("king", "diamonds")},
        {("5", "spades"), ("9", "spades"), ("4", "spades"), ("10", "spades"), ("ace", "spades")},
    )

    for player_a_cards in straight_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"

def test_get_result_of_poker_with_three_of_a_kind_scenarios():
    three_of_a_kind_scenarios = (
        # Three of a Kind Scenarios
        {("3", "spades"), ("3", "hearts"), ("3", "clubs"), ("5", "spades"), ("6", "diamonds")},
        {("5", "spades"), ("5", "hearts"), ("5", "clubs"), ("6", "spades"), ("7", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("8", "clubs"), ("7", "spades"), ("10", "diamonds")},
        {("9", "spades"), ("9", "hearts"), ("9", "clubs"), ("5", "spades"), ("4", "diamonds")},
        {("10", "spades"), ("10", "hearts"), ("10", "clubs"), ("5", "spades"), ("6", "diamonds")},
    )

    player_a_scenarios = (
        # Two Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("6", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("10", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("ace", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("10", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("5", "spades"), ("8", "diamonds")},
        # One Pair Scenarios
        {("5", "spades"), ("5", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("8", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("king", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("6", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("7", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
        # High Card Scenarios
        {("5", "spades"), ("9", "hearts"), ("6", "clubs"), ("4", "spades"), ("10", "diamonds")},
        {("8", "spades"), ("king", "hearts"), ("10", "clubs"), ("6", "spades"), ("2", "diamonds")},
        {("king", "spades"), ("jack", "hearts"), ("ace", "clubs"), ("queen", "spades"), ("8", "diamonds")},
        {("6", "spades"), ("king", "hearts"), ("10", "clubs"), ("ace", "spades"), ("9", "diamonds")},
        {("7", "spades"), ("2", "hearts"), ("5", "clubs"), ("10", "spades"), ("8", "diamonds")},
    )

    player_b_scenarios = (
        # Royal Flush Scenarios
        {("10", "spades"), ("jack", "spades"), ("queen", "spades"), ("king", "spades"), ("ace", "spades")},
        {("10", "clubs"), ("jack", "clubs"), ("queen", "clubs"), ("king", "clubs"), ("ace", "clubs")},
        {("10", "hearts"), ("jack", "hearts"), ("queen", "hearts"), ("king", "hearts"), ("ace", "hearts")},
        {("10", "diamonds"), ("jack", "diamonds"), ("queen", "diamonds"), ("king", "diamonds"), ("ace", "diamonds")},
        # Straight Flush Scenarios
        {("2", "spades"), ("3", "spades"), ("4", "spades"), ("5", "spades"), ("6", "spades")},
        {("3", "clubs"), ("4", "clubs"), ("5", "clubs"), ("6", "clubs"), ("7", "clubs")},
        {("4", "hearts"), ("5", "hearts"), ("6", "hearts"), ("7", "hearts"), ("8", "hearts")},
        {("5", "diamonds"), ("6", "diamonds"), ("7", "diamonds"), ("8", "diamonds"), ("9", "diamonds")},
        {("6", "spades"), ("7", "spades"), ("8", "spades"), ("9", "spades"), ("10", "spades")},
        # Four Of a Kind Scenarios
        {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("king", "diamonds"), ("6", "spades")},
        {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("7", "diamonds"), ("8", "spades")},
        {("8", "spades"), ("8", "clubs"), ("8", "hearts"), ("8", "diamonds"), ("10", "spades")},
        {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("9", "diamonds"), ("3", "spades")},
        {("10", "spades"), ("10", "clubs"), ("10", "hearts"), ("10", "diamonds"), ("5", "spades")},
        # Full House Scenarios
        {("king", "spades"), ("king", "clubs"), ("king", "hearts"), ("queen", "diamonds"), ("queen", "spades")},
        {("7", "spades"), ("7", "clubs"), ("7", "hearts"), ("8", "diamonds"), ("8", "spades")},
        {("9", "spades"), ("9", "clubs"), ("9", "hearts"), ("10", "diamonds"), ("10", "spades")},
        {("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("2", "diamonds"), ("2", "spades")},
        {("ace", "spades"), ("ace", "clubs"), ("ace", "hearts"), ("10", "diamonds"), ("10", "spades")},
        # Flush Scenarios
        {("2", "spades"), ("8", "spades"), ("3", "spades"), ("5", "spades"), ("ace", "spades")},
        {("5", "hearts"), ("7", "hearts"), ("2", "hearts"), ("9", "hearts"), ("king", "hearts")},
        {("6", "clubs"), ("9", "clubs"), ("jack", "clubs"), ("10", "clubs"), ("3", "clubs")},
        {("queen", "diamonds"), ("9", "diamonds"), ("5", "diamonds"), ("7", "diamonds"), ("king", "diamonds")},
        {("5", "spades"), ("9", "spades"), ("4", "spades"), ("10", "spades"), ("ace", "spades")},
        # Straight Scenarios
        {("6", "spades"), ("7", "hearts"), ("8", "clubs"), ("9", "spades"), ("10", "diamonds")},
        {("7", "spades"), ("8", "hearts"), ("9", "clubs"), ("10", "spades"), ("jack", "diamonds")},
        {("8", "spades"), ("9", "hearts"), ("10", "clubs"), ("jack", "spades"), ("queen", "diamonds")},
        {("9", "spades"), ("10", "hearts"), ("jack", "clubs"), ("queen", "spades"), ("king", "diamonds")},
        {("10", "spades"), ("jack", "hearts"), ("queen", "clubs"), ("king", "spades"), ("ace", "diamonds")},
    )

    for player_a_cards in three_of_a_kind_scenarios:
        for player_b_cards in player_a_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player A", "The get_result_of_poker is not working as expected"
        
        for player_b_cards in player_b_scenarios:
            winner = part1.get_result_of_poker(player_a_cards, player_b_cards)
            assert winner == "Player B", "The get_result_of_poker is not working as expected"