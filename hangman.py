import random

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

def hangman():
    word_list = ["photon", "java", "copper", "hecker", "printer"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["",
            "________      ", 
            "|      |      ", 
            "|      0      ", 
            "|     /|\     ", 
            "|     / \     ", 
            "|"]
    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter: ")
        if guess in remaining_letters:
            character_index=findOccurrences(remaining_letters,guess)
            for value in character_index:
                letter_board[value] = guess
                remaining_letters[value] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '_' not in letter_board:  
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman()