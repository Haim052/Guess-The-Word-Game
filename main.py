# def main():
#     lst_words = ["aba", "mama"]
#     for i in range(len(lst_words)):
#         current_word = prints_hidden_word(lst_words)
#         print(current_word)

#         check_letter_in_word(current_word)


# def main1():
#     points_player1 = 0
#     points_player2 = 0
#     for x in range(len(lst)):
#             print(
#                 f"player1 '{points_player1}' points\nplayer2 '{points_player2}' points"
#             )


# def main2():
#     global lst_words
#     global i
#     new_hid_word = ""
#     lst_players = {}
#     lst_words = ["father", "math", "children"]
#     sum_players = int(input("how much players: "))
#     # for z in range(len(sum_players)):
#     #     play1 = input("Enter your name: ")
#     #     lst_players["play1"] = play1
#     play1 = input("Enter your name: ")
#     play2 = input("Enter your name: ")
#
#     for i in range(len(lst_words)):
#         print(hidden_word(lst_words[i]))
#         for x in lst_words[i]:
#             re_player1 = player1()
#             print(re_player1)



def main():
    sum_points = 0
    real_word = ["hello", "world"]
    for x in range(len(real_word)):
        hid_word = len(real_word[x]) * '*'
        guess = []
        print(f"the length of the word is: {hid_word}")
        while '*' in hid_word:
            print(f"The guesses so far are: {hid_word}")
            player_guess = input("Enter a guess: ")
            while len(player_guess) != 1:
                player_guess = input(
                    "You entered more than one letter, please enter again a letter: "
                )
            while player_guess in guess:
                player_guess = input("They already guessed the letter please enter again a letter:")
            guess.append(player_guess)
            hid_word, points = check_letter_in_word(hid_word, real_word[x], player_guess)
            print(hid_word)
            print(points)
            sum_points += points
            print("-------------------------")
        print(f"total points: {sum_points}")



# def hidden_word(word: str) -> str:
#     """מחזירה את המילה כשהיא מוסתרת"""
#     return len(word) * "*"


def player1():
    gu = 0
    sum_point_player1 = 0
    player1 = input("Enter a gusse ")
    gu, points1 = check_letter_in_word(hidden_word(lst_words[i]), lst_words[i], player1)
    sum_point_player1 += points1
    if gu == 2:
        return "this is not a guess"
    else:
        return gu


def checking_guess(real_word: str, hid_word: str, guesses: str) -> (int, str):
    """ בודקת אם נחשו את האות כבר
    מחזיר שלא ניחושו - כן
    קורא לפונקציה של הניחושים ומדפיסה את סך הנקודות לפי הניחושים - לא
    """
    while '*' in hid_word:
        player_guess = input("letter: ")
        if player_guess in guesses:
            return "The letter is already guessing enter another"
        else:
            guesses.append(player_guess)
            hid_word, points = check_letter_in_word(hid_word, real_word, player_guess)
            print(hid_word)
            print(points)
            return hid_word, points


def check_letter_in_word(hid_word: str, word: str, letter: str) -> (int, str):
    """Gets the word when it is hidden and the guess of the letter
    and checks if it is a true guess,
    if so it replaces the index with the letter and returns it
    if not it returns a level"""
    sum_point = 0
    if letter in word:
        guesses = hid_word
        for inx, char in enumerate(word):
            if char == letter:
                guesses = guesses[:inx] + letter + guesses[inx + 1:]
                sum_point += 1
        return guesses, sum_point
    else:
        print("The letter is not in the word")
        return hid_word, sum_point


main()
