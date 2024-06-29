def main():
    global hid_word
    global lst_words
    global word
    global guess
    global sum_points1
    global sum_points2
    sum_points1 = 0
    sum_points2 = 0
    lst_words = ["hello", "world"]
    lst1_words = ["Fruits", "Apple", "Banana", "Orange", "Pear", "Mango"]
    global play1
    global play2
    play1 = input("Enter your name: ")
    play2 = input("Enter your name: ")
    for word in range(len(lst_words)):
        hid_word = len(lst_words[word]) * "*"
        guess = []
        print(f"the length of the word is: {hid_word}")

        while "*" in hid_word:
            player1()
            if "*" in hid_word:
                player2()
            else:
                print("***the gmae is over***")
                print(f"the point are player1: {sum_points1}, player2: {sum_points2}")
                if sum_points1 > sum_points2:
                    print("player 1 you are the winner!!!")
                elif sum_points1 < sum_points2:
                    print("player 2 you are the winner!!!")


def player1():
    global hid_word
    global sum_points1
    print(f"'{play1}' The guesses so far are: {hid_word}")
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
    hid_word, points1 = check_letter_in_word(
        hid_word, lst_words[word], player_guess1.lower()
    )
    sum_points1 += points1
    print(f"you guessed so far {hid_word}")
    print(f"your points are {points1}")
    print("-----")


def player2():
    global hid_word
    global sum_points2
    print(f"'{play2}' The guesses so far are: {hid_word}")
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
    hid_word, points1 = check_letter_in_word(
        hid_word, lst_words[word], player_guess2.lower()
    )
    sum_points2 += points1
    print(f"you guessed so far {hid_word}")
    print(f"your points are {points1}")
    print("-----")


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


main()
