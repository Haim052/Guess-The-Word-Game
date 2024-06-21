# def main():
#     lst_words = ["aba", "mama"]
#     for i in range(len(lst_words)):
#         current_word = prints_hidden_word(lst_words)
#         print(current_word)

#         check_letter_in_word(current_word)


def main():
    lst = ["aba"]
    points_player1 = 0
    points_player2 = 0
    for i in lst:
        print(hidden_word(i))
        user = input("enter a letter guess: ")
        while len(user) != 1:
            user = input(
                "You entered more than one letter, please enter again a letter: "
            )
        open_word, points = check_letter_in_word(hidden_word(i), i, user)
        print(f"The guesses so far are: {open_word}")
        # סך נקודות
        points_player1 += points
        # points_player2 += points
        print(
            f"player1 you have {points_player1} points\nand player2 you have {points_player2} points"
        )


def hidden_word(word: str) -> str:
    """Receives a word and returns it hidden"""
    return len(word) * "*"


def check_letter_in_word(hid_word: str, word: str, letter: str) -> int:
    """Gets the word when it is hidden and the guess of the letter
    and checks if it is a true guess,
    if so it replaces the index with the letter and returns it
    if not it returns a level"""

    if letter in word:
        global gusses
        gusses = hid_word
        caunter_point = 0
        for inx, char in enumerate(word):
            if char == letter:
                gusses = gusses[:inx] + letter + gusses[inx + 1 :]
                caunter_point += 1
        return gusses, caunter_point
    return False


main()
