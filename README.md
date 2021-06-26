# EPAI Session 6 Poker Assignment

## Overview of the functions in Part1.py

### get_deck_of_cards

Returns the complete set representing the deck of cards with a card being represented by a tuple consists of value and a suit like below:

`('8', 'spades')`
`('jack', 'clubs')`
`('ace', 'diamonds')`

This function uses lambda, zip and map functions to create the deck

### get_deck_of_cards_without_zip

Same as the above function returns the complete deck of cards just that it creates the deck without using zip

### validate_cards

Takes a player cards and applies the below validations over them:

1. Checks if the player_cards is a set or not and throws a `TypeError` if not
2. Checks if each card in player_cards is valid or not and throws a `ValueError` if not

### get_result_of_poker

This function accepts 2 sets of 3 or 4 or 5 cards each representing player_a_cards and player_b_cards and it returns who is the winner of the game.

Firstly it finds out if player_a_cards and player_b_cards fall under which poker_hand. It utilizes the poker hand utility functions writte for this purpose.

The poker hand is evaluated in the order as given below: 

1. Royal Flush
2. Straight Flush
3. Four Of a Kind
4. Full House
5. Flush
6. Straight
7. Three Of a Kind
8. Two Pair
9. One Pair

In this order the player_a_rank and player_b_rank is evaluated and now the following cases are evaluated:

1. If both fall under any of the above ranks and player_a_rank is lower than player_b_rank it returns `Player A`
2. If both fall under any of the above ranks and player_b_rank is lower than player_a_rank it returns `Player B`
3. If both fall under any of the above ranks and both the ranks are the same then the other function `resolve_rank_tie` is called with the poker_hand and both the sets of the cards.
4. If player a does not fall under any of the above poker hands and player_b_rank exists then it return `Player B`
5. If player b does not fall under any of the above poker hands and player_a_rank exists then it returns `Player A`
6. if both of them do not fall under any of the poker hands then the winner is selected based on high card.

### resolve_rank_tie

This is function is called when the rank of the Player A and Player B is same, then based on the poker_hand that is passed to the function 
    
1. if it is Straight Flush or Flush or Straight Then `resolve_by_high_card` is called and the result is returned
    
2. if it is Four Of a Kind then `resolve_with_preferential_high_card_value` is called with both the player cards and 4 as the count
    
3. if it is Full House or Three Of a Kind then `resolve_with_preferential_high_card_value` is called with bothe the player cards and 3 as the count
    
4. if it is a Pair or Two Pair then `resolve_with_preferential_high_card_value` is called with both the player_cards and 2 as the count

### resolve_with_preferential_high_card_value

This function takes player_a_cards and player_b_cards and the preferential count

It resolves the tie by giving preference to the card in the set of cards which is repeated as the no. of times the passed `count` parameter.

Comparing with the card with count times is also resulting in a tie then it resolve it with a high card from the rest of the cards

Example:

Player A - `("5", "spades"), ("5", "clubs"), ("5", "hearts"), ("5", "diamonds"), ("king", "diamonds")`

Player B - `("6", "spades"), ("6", "clubs"), ("6", "hearts"), ("6", "diamonds"), ("ace", "diamonds")`

In the above sets of cards Player A has a Four of a Kind Hand and Player B also has a Four of a Kind Hand

Now to resolve the tie the value of the card which is repeating 4 times is compared in both the sets and if that is also same it compares the rest of the cards.

This method is called with both the sets of the cards and `count` parameter as 4, It compares the value 5 and 6 and return `Player B`.

### resolve_by_high_card

This function takes player_a_cards and player_b_cards and checks recursively the high card from player a and high card from player B
and till it gets a result, if it is not able to get a result it returns "Player A and Player B"

### convert_cards_to_values

This function takes the set of cards as input and returns a set with the cards corresponding value and suit

Example
`{("10", "spades"), ("jack", "clubs"), ("king", "hearts")}` -> `{(10, "spades"), (11, "spades"), (13, "hearts")}`

This transformation is very much necessary to perform operations on the cards like to sort the cards, get the high card value and so on.

### check_if_list_in_sequence

This is an utility function to check if the values are in a sequence:

Example
`[1,2,3,4,5]` -> `True`
`[1,7,8,4,6]` -> `False`

This is used to detect straight sequences in the cards for Royal Flush, Straight Flush and Straight

### get_top_2_frequencies_of_list

This is another utility function which returns a tuple with the top 2 highest frequencies in the list
Example
`[1,1,1,2,2]` -> `(3, 2)`
`[1,1,3,3,6]` -> `(2, 2)`

This is used mainly for detecting full house in the the set of cards

### check_for_royal_flush

Checks if the player_cards contains 5 cards and a royal flush
Example
`10 jack queen king ace`

The Highest sequence cards all of same suit - spades, clubs, hearts or diamonds

Returns `True` if it finds in player_cards else Returns `False`

### check_for_straight_flush

Checks if the player_cards contains 5 cards and a straight flush
if the values are in sequence and all are of same suit

Example
`6 7 8 9 10` 
    
Any sequence of the cards all of the same suit - spades, clubs, hearts or diamonds

Returns `True` if it finds in player_cards else Returns `False`

### check_for_four_of_a_kind

Checks if the player_cards contains a Four of a kind in it
Example
`queen queen queen queen 10`

4 Cards of same value 

Returns `True` if it finds 4 Cards of same value else Returns `False`

### check_for_full_house

Checks if the player_cards contains Full House in it
    
Example
`queen queen queen 8 8`

3 Cards of one value and 2 Cards of another value

Returns `True` if it finds 3 cards of one value and 2 cards of another value else returns `False`

### check_for_flush

Checks if the player_cards contains a Flush in it

Example
`(queen, spades), (10, spades), (5, spades), (4, spades), (2, spades)`

All the 5 cards of same suit

Returns `True` if it finds all the 5 cards of same suit else returns `False`

### check_for_straight

Checks if the player_cards contains a Straight in it

Example

`(4, spades), (5, clubs), (6, hearts), (7, spades), (8, hearts)`

All the 5 cards values are in sequence and suits doesn't matter

Returns `True` if it finds all the 5 cards values are in sequence without considering suits else returns `False`

### check_for_three_of_a_kind

Checks if the player_cards contains a Three of a Kind in it

Example

`(queen, spades), (queen, hearts), (queen, clubs), (6, spades), (10, hearts)`

Any 3 cards of the same value 

Returns `True` if it finds any 3 cards are same in value else returns `False`

### check_for_two_pair

Checks if the player_cards contains a 2 Pair in it
Example
`(king, spades), (king, hearts), (8, clubs), (8, hearts), (5, spades)`

Any 2 pair of cards with same value

Returns `True` if it finds any 2 Pairs with the same value else returns `False`

### check_for_pair

Checks if the player_cards contains a Pair in it

Example
`(jack, spades), (jack, clubs), (10, hearts), (8, spades), (7, clubs)`

A pair of cards with same value

Returns `True` if it finds a pair with the same value else returns `False`

## Overview of the Test Cases

There are in total 42 tests which test the complete all the functions in part1. In test_part1.py there are different poker hand scenarios listed:

1. ROYAL_FLUSH_SCENARIOS - There are only 4 Royal flush scenarios that can be there, and all of them are listed in it.
2. STRAIGHT_FLUSH_SCENARIOS - There are like 8 Straight Flush Scenarios listed here with different sequences and different suits too.
3. FOUR_OF_A_KIND_SCENARIOS - There are like 26 Four of a kind Scenarios listed where all the values are covered with set of 5 cards and 4 cards
4. FULL_HOUSE_SCENARIOS - Randomly chosen 13 randomly chosed scenarios covering all the cards with pair and 3 of kind with different suits
5. FLUSH_SCENARIOS - Randomly chosen 9 scenarios with different cards with all suits same
6. STRAIGHT_SCENARIOS - 8 Scenarios covering all the sequences from 2 to 9 with different suits
7. THREE_OF_A_KIND_SCENARIOS - 39 Scenarios covering each value of card 3 times covering 3 and 4 and 5 cards
8. TWO_PAIR_SCENARIOS - 26 Scenarios covering each value of card twice and having set of 4 cards and 5 cards
9. ONE_PAIR_SCENARIOS - 39 Scenarios covering each card a single pair and having a set of 3 and 4 and 5 cards
10. HIGH_CARD_SCENARIOS - 39 Scenarios Randomly selected covering 3 and 4 and 5 cards

These scenarios are used heavily in the following tests.


### test_deck_of_cards

Test `get_deck_of_cards` function - if all the 52 cards are returned are not

Programmatically generated all the 52 cards and check if they exist in the returned result or not

### test_get_deck_of_cards_without_zip

Test `get_deck_of_cards_without_zip` function - if all the 52 cards are returned are not

Same test as above is run over the result of `get_deck_of_cards_without_zip`

### Poker hand Utility Function Test Cases 

Here are the different Poker hand functions that are tested

1. check_for_royal_flush
2. check_for_straight_flush
3. check_for_four_of_a_kind
4. check_for_full_house
5. check_for_flush
6. check_for_straight
7. check_for_three_of_a_kind
8. check_for_two_pair
9. check_for_pair

For each function there is a positive test case, which programmatically generates the positive scenarios for the poker hand and calls the function and checks if the function is returning `True`

For the negative Test Case ALL the scenarios listed above other than the concerned poker hand are sent and checked if it is returning `False`

These constitute around 18 Test Cases

### test_get_result_of_poker_with_invalid_type

Testing the get_result_of_poker validations 

Sending invalid type for the cards should result in Type Error with the following message `The player_cards should be a set`

### test_get_result_of_poker_with_invalid_card_type

Testing the get_result_of_poker validations 

Sending a set of invalid cards should result in Type Error with the following message `should be a tuple with value and suit in it`

### test_get_result_of_poker_with_invalid_cards

Testing the get_result_of_poker validations

Sending set of tuples with invalid value and suits in the tuple should result in a ValueError with the following message
`not a valid value` or `not a valid suit`

### Testing the get_result_of_poker with different Poker Hands

This function is the main function that needs to be tested with different scenarios of player_cards. The following cases have been tested

1. `test_get_result_of_poker_with_royal_flush` - Every Royal Flush Scenario is compared with every other scenario of the other poker hands and we are checking if the winner is the Player A or not
2. `test_get_result_of_poker_with_straight_flush` - Every Straight Flush Scenario is compared with every other scenario of the other Poker Hands 
For All other Scenarios Except Royal Flush Scenarios Player A is the Winner and for Royal Flush Player B is the winner.
3. `test_get_result_of_poker_with_four_of_a_kind` - Every Four of a Kind Scenario is compared with every other scenarion of the other poker hands 
Except for Royal Flush, Straight_Flush Player A should be the winner
4. `test_get_result_of_poker_with_full_house` - Every Full House Scenario is compared with every other scenario of the other Poker Hands 
Except for Royal Flush, Straight Flush, Four_of_a_kind - Player A should be the Winner
5. `test_get_result_of_poker_with_flush_scenarios` - Every Flush Scenario is compared with every other scenario of the other Poker Hands
Except for Royaal Flush, Straight Flush, Four_of_a_kind, Full House - Player A should be the Winner
6. `test_get_result_of_poker_with_straight_scenarios` - Every Straight Scenario is compared with every other scenario of the other Poker Hands
Three Of a Kind, Two Pair, One Pair, High card - Player A
Royaal Flush, Straight Flush, Four_of_a_kind, Full House, Flush - Player B
7. `test_get_result_of_poker_with_three_of_a_kind_scenarios` - Every Three of a Kind Scenario is compared with every other scenario of the other Poker Hands
Two Pair, One Pair, High card - Player A
Royaal Flush, Straight Flush, Four_of_a_kind, Full House, Flush, Straight - Player B
8. `test_get_result_of_poker_with_two_pair_scenarios` - Every Two Pair Scenario is compared with every other scenario of the other Poker Hands
One Pair, High card - Player A
Royaal Flush, Straight Flush, Four_of_a_kind, Full House, Flush, Straight, Three Of a Kind - Player B
9. `test_get_result_of_poker_with_one_pair_scenarios` - Every One Pair Scenario is compared with every other scenario of the other Poker Hands
High card - Player A
Royaal Flush, Straight Flush, Four_of_a_kind, Full House, Flush, Straight, Three Of a Kind, Two Pair - Player B

### Testing get_result_of_poker with Same Poker Hands

These tests test the `get_result_of_poker` when both players get the same poker hands

1. `test_get_result_of_poker_with_both_players_having_straight_flush` - The tie needs to be resolved only with a high card, 5 different scenarios of player A winning and 5 different scenarios of player B winnin are tested
2. `test_get_result_of_poker_with_both_players_having_four_of_a_kind` - 2 Cases are tested in this where one is the tie is resolved with the value of the card which is 4 of kind and another case that is tested is the both the Four of a kind card value is same and the tie is resolved by the 5th Card. 5 different Scenarios with Player A winning and 5 different Scenarios with Player B winning.
3. `test_get_result_of_poker_with_both_players_having_full_house` - 2 Cases are tested in this too, one is the tie is resolved with 3 of kind card Value and another is the 3 of a kind value is same and it is resolved by the value of the Pair. 5 Different Scenarios in which Player A is winning and 5 Different Scenarios with Player B winning.
4. `test_get_result_of_poker_with_both_players_having_flush` - The tie needs to be resolved only with a high card, 5 different scenarios of player A winning and 5 different scenarios of player B winnin are tested.
5. `test_get_result_of_poker_with_both_players_having_straight` - The tie needs to be resolved only with a high card, 5 different scenarios of player A winning and 5 different scenarios of player B winnin are tested.
6. `test_get_result_of_poker_with_both_players_having_three_of_a_kind` - 2 Cases are tested in this too, one is the tie is resolved with 3 of kind card Value and another is the 3 of a kind value is same and it is resolved by the high card in the rest of the cards. 5 Different Scenarios in which Player A is winning and 5 Different Scenarios with Player B winning.
7. `test_get_result_of_poker_with_both_players_having_two_pair` - 2 Cases are tested in this too, one is the tie is resolved with 2 pair cards and another is the both the pairs are same and it is resolved by the high card over the 5th card. 5 Different Scenarios in which Player A is winning and 5 Different Scenarios with Player B winning.
8. `test_get_result_of_poker_with_both_players_having_one_pair` - 2 Cases are tested in this too, one is the tie is resolved with the value of the card pair and another is the value of the card pair is same and it is resolved by the high card in the rest of the cards. 5 Different Scenarios in which Player A is winning and 5 Different Scenarios with Player B winning.
9. `test_get_result_of_poker_with_both_players_having_high_card` - The tie needs to be resolved only with a high card, 5 different scenarios of player A winning and 5 different scenarios of player B winnin are tested.

### test_get_result_of_poker_with_a_tie - Testing the get_result_of_poker with actual tie

All the poker hand scenarios are iterated and the Same cards are sent to the `get_result_of_poker`  function to check if it is returning `Player A and Player B` as a result.
