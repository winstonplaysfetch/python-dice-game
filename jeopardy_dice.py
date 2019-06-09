#Jeopardy Dice


from random import randint

#Prints a statement indicating who's turn it is
def print_current_player(is_user_turn):
    if is_user_turn:
        print("It is your turn")
    else:
        print("It is not your turn")

#Rolls a 6-sided die and returns the value rolled
def roll_die():
    return randint(1,6)

#Executes a game turn, returns new total for current player
def take_turn(is_user_turn, COMPUTER_HOLD):
    user_total = roll_die()
    if raw_input("Do you want to roll again (Y/N)? ") == Y:
        new_roll = roll_die()
        user_total = user_total + new_roll
        print("You rolled a " + str(user_total))
    else:
        report_points()
    return user_total

#Prints a report of how many points each player has
def report_points(user_total, bot_total):
    print("computer: " + bot_total + "/n" 
            + "human: " + user_total)

#Returns the opposite of the current user's turn
def get_next_player(is_user_turn):
    if not is_user_turn:
        print("Your turn is next")
    else:
        print("The bot's turn is next")

def main():
    print("Jeopardy Dice by Jennifer Daly")
    #print("Game Rules: ")
    #print("Press Y to roll die; N to hold.")
    #print("First player to 100 points wins")
    GAME_END_POINTS	= 100
    COMPUTER_HOLD = 10
    is_user_turn = True

    #print("Test dice roll: " + str(roll_die()))
    get_next_player(is_user_turn)

if __name__ == '__main__':
    main()


