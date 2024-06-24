# def main():
#     lst_words = ["aba", "mama"]
#     for i in range(len(lst_words)):
#         current_word = prints_hidden_word(lst_words)
#         print(current_word)

#         check_letter_in_word(current_word)


# def main1():
#     points_player1 = 0
#     points_player2 = 0
#     for word in range(len(lst)):
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
#         for word in lst_words[i]:
#             re_player1 = player1()
#             print(re_player1)


# def main1():
#     global hid_word
#     global lst_words
#     global word
#     sum_points = 0
#     lst_words = ["hello", "world"]
#     # for word in range(len(lst_words)):
#         # hid_word = len(lst_words[word]) * "*"
#         guess = []
#         print(f"the length of the word is: {hid_word}")
#         while "*" in hid_word:
#             print(f"The guesses so far are: {hid_word}")
#             player_guess = input("Enter a guess: ")
#             # בודק אם הכניסו רק תו אחד
#             while len(player_guess) != 1:
#                 player_guess = input(
#                     "You entered more than one letter, please enter again a letter: "
#                 )
#             # בודק אם ניחשו כבר את האות
#             while player_guess in guess:
#                 player_guess = input(
#                     "They already guessed the letter please enter again a letter:"
#                 )
#             guess.append(player_guess)
#             hid_word, points = check_letter_in_word(hid_word, lst_words[word], player_guess)
#             print(hid_word)
#             print(points)
#             sum_points += points
#             print("-------------------------")
#         print(f"total points: {sum_points}")


# def hidden_word(word: str) -> str:
#     """מחזירה את המילה כשהיא מוסתרת"""
#     return len(word) * "*"


def main2():
    global hid_word
    global lst_words
    global word
    sum_points1 = 0
    sum_points2 = 0
    lst_words = ["hello", "world"]
    for word in range(len(lst_words)):
        hid_word = len(lst_words[word]) * "*"
        guess = []
        print(f"the length of the word is: {hid_word}")


        while "*" in hid_word:
            print(f"player 1 The guesses so far are: {hid_word}")
            player_guess1 = input("Enter a gusse: ")
            while len(player_guess1) != 1:
                player_guess1 = input(
                    "You entered more than one letter, please enter again a letter: "
                )
            while player_guess1 in guess:
                player_guess1 = input(
                    "They already guessed the letter please enter again a letter:"
                )
            guess.append(player_guess1)
            hid_word, points1 = check_letter_in_word(hid_word, lst_words[word], player_guess1)
            sum_points1 += points1
            print(f"you guessed so far {hid_word}")
            print(f"your points are {points1}")
            print("-----")



            print(f"player 2 The guesses so far are: {hid_word}")
            player_guess2 = input("Enter a gusse: ")
            while len(player_guess2) != 1:
                player_guess = input(
                    "You entered more than one letter, please enter again a letter: "
                )
            while player_guess2 in guess:
                player_guess2 = input(
                    "They already guessed the letter please enter again a letter:"
                )
            guess.append(player_guess2)
            hid_word, points1 = check_letter_in_word(hid_word, lst_words[word], player_guess2)
            sum_points2 += points1
            print(f"you guessed so far {hid_word}")
            print(f"your points are {points1}")
            print("-----")
    print(f"the point are player1: {sum_points1} player2: {sum_points2}")





def player1():
    sum_points1 = 0
    player_gues = input("enter a gusse: ")
    gue, sum_poin = check_letter_in_word(hid_word, lst_words[word], player_gues)
    sum_points1 += sum_poin
    return gue, sum_points1


def player2():
    sum_points1 = 0
    player_gues = input("enter a gusse: ")
    gue, sum_poin = check_letter_in_word(hid_word, lst_words[word], player_gues)
    sum_points1 += sum_poin
    return gue, sum_points1


def checking_guess(real_word: str, hid_word: str, guesses: str) -> (int, str):
    """בודקת אם נחשו את האות כבר
    מחזיר שלא ניחושו - כן
    קורא לפונקציה של הניחושים ומדפיסה את סך הנקודות לפי הניחושים - לא
    """
    while "*" in hid_word:
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
    if so it replaces the indeword with the letter and returns it
    if not it returns a level"""
    sum_point = 0
    if letter in word:
        guesses = hid_word
        for inword, char in enumerate(word):
            if char == letter:
                guesses = guesses[:inword] + letter + guesses[inword + 1 :]
                sum_point += 1
        return guesses, sum_point
    else:
        print("The letter is not in the word")
        return hid_word, sum_point


# player1()
# main1()
main2()
