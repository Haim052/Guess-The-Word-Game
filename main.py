def hidden_word(word: str) -> str:
    """Receives a word and returns it hidden"""
    return len(word) * "*"


def check_letter_in_word(word: str, letter: str) -> int:
    """Gets the word when it is hidden and the guess of the letter
    and checks if it is a true guess,
    if so it replaces the index with the letter and returns it
    if not it returns a level"""

    if letter in word:
        for char in range(len(word)):
            if word[char] == letter:
                guess = word.replace(word[char], letter)
                return guess
    return False
