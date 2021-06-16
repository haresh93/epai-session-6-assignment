# EPAI Session 6 Poker Assignment


## test_check_for_royal_flush
the cards should be in  highest value viz. 10, J, Q, K, A  and of the ame suite viz. spades, clubs, diamond and hearts. 

## test_check_for_royal_flush_negative
 this functions  testted  if all the three cards of clubs and fourth one  hearts - 10 thouhg in the same sequence 
Also tests if the four cards are of different suite
#test_check_for_straight_flush()

# test_check_for_straight_flush_negative()
Function Tests 

## Testing Straight Flush
This functions tests if the cards are in sequence 2 - 6 and of spades  
Tests if the cards are in the sequence of 3 - 7 and of Clubs 
Tests of the cards are in the sequence of 4 - 8 and of suite hearts
Test if the cards are in sequence 5-9 and of diamonds suite
Test if the cards are in sequence 7 - 10 and of diamonds suite
Test if the cards are in sequence 8 - 10 and jack and queen and of hearts suite
Test if the cards are in sequence 9 and 10 and jack, queen and king and of diamonds suite


## test_check_for_straight_flush_negative
This function tested if the cards of spades suite and in sequence of 2- 6 but two cards are clubs and dimonds 
This function also tests if the clubs suite yet not in the sequence with carsd 2, 4, 5, 6 and 7
This function alsos tests if the cards are not in a seqence and also not of the same suite. 
This function also tests if the cards are not in a seqnece not in the sequence and also not in a singel suite


## test_check_for_four_of_a_kind
four cards tken of the same kind and randomized fifth card to check the status . 


## Utility functions

check_for_royal_flush
check_for_straight_flush
check_for_four_of_a_kind
check_for_full_house
check_for_flush
check_for_straight
check_for_three_of_a_kind
check_for_two_pair
check_for_pair

All the tests with random scenarios have been written to check if the above utility functions are working as expected or not with negative test cases too.

## get_high_card_value

Return the value of the high card in the cards sent

## get_result_of_the_poker

This function returns the player who won the game of poker based on the cards passed to the function
Each Player's cards are checked if the cards have any of the rank according to the order
If the Player A rank is less than Player B then Player A has won it
If the Player B rank is less than Player B then Player B has won it

If both the Player A rank and Player B rank are same then `resolve_rank_tie` is called and the tie is resolved, 
based on the poker hand the involved high card is calculated and who ever has a high card in the poker hand is the
winner of the game.
