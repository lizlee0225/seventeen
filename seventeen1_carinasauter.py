import random


def check_human_input(number, marbles_left):
    """Checks if human input is 1, 2 or 3 and that it is never more than the
    marbles that are left. If that is not the case, the check will prompt the
    user for a new input until all conditions are fulfilled.
    """
    lst = ["1", "2", "3"]
    while str(number) not in lst or int(number) > marbles_left:
        print("Sorry, that is not a valid option. Try again!")
        status_prompt(marbles_left)
        number = input(
            "\nYour turn: How many marbles will you remove (1-3)? ")
        number = check_human_input(number, marbles_left)
    return int(number)


def status_prompt(marbles_left):
    """Helper function to print the status prompt across the game"""
    print("Number of marbles left in jar: {}".format(marbles_left))


def seventeen():
    print("\n\nLet's play the game of Seventeen!")
    marbles_left = 17  # Marbles initiated at 17
    status_prompt(marbles_left)
    while marbles_left > 0:  # Loop is entered until no marbles left
        user_input = input(
            "\nYour turn: How many marbles will you remove (1-3)? ")
        user_input = check_human_input(
            user_input, marbles_left)  # user_input sent to check
        print("You removed {} marbles.".format(user_input))  # Feedback to user
        marbles_left -= user_input
        if marbles_left > 0:
            status_prompt(marbles_left)
            print("\nComputer's turn...")
            random_number = random.randint(1, min(marbles_left, 3))
            marbles_left -= random_number
            print("Computer removed {} marbles.".format(random_number))
            if marbles_left > 0:
                status_prompt(marbles_left)
        else:
            print("There are no marbles left. Computer wins!")
            exit()
    print("There are no marbles left. You win!")


def main():  # CALL YOUR FUNCTION BELOW
    seventeen()

if __name__ == '__main__':
    main()
