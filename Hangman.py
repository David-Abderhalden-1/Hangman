import time
from Hangman_Phases import Phases
import random


# Variables_1
two_users = False
single_player = False
letter_index = 100
play_again = True

# Introduction
print("\n\n" + '*' * 37 + " Hangman " + '*' * 37 + "\n")
print("""\
Description: You have to guess a word. As you guess wrong letters, you will get
                          hanged time to time. Good luck!""")
time.sleep(8)
# Functions

while play_again:
    two_users = False
    single_player = False
    while not two_users and not single_player:
        user_input = input("\n(a) You are two players (b) You are one player | Your answer: ")
        if user_input.lower() == "a":
            two_users = True
        elif user_input.lower() == "b":
            single_player = True
        else:
            time.sleep(2)
            print("Error! The answer: " + user_input + " is not recognized.")

    # Program
    # Starter phase
    # Variables_2
    searched_word = ""
    time.sleep(2)
    word_entered = False
    index_list = []
    used_letters = []
    maximum_tries = 6
    user_tries = 0
    found_letters = ""
    phases = Phases()
    i = 1

    if two_users:
        while not word_entered:
            searched_word = input("\nPerson 1 enter your word here: ")
            searched_word = searched_word.upper()
            word = list(searched_word)
            time.sleep(2)
            user_answer = input("\nYour word is: " + searched_word +
                                ". Do you want to proceed? (a) Yes (b) No | Your answer: ")
            if user_answer.lower() == "a":
                word_entered = True
            elif user_answer.lower() == "b":
                word_entered = False
            else:
                time.sleep(2)
                print("Error! The answer: " + user_answer + " is not recognized.")
            while i <= 20 and word_entered:
                print("/" * 37 + 'barrier!' + "/" * 37)
                i += 1

    elif single_player:
        single_player_words = open("words_1.0.txt", "r")
        single_player_words = list(single_player_words)
        index_count = -1
        for indx in single_player_words:
            index_count += 1

        searched_word = (single_player_words[random.randint(0, index_count)])
        searched_word = searched_word.upper()
        word = list(searched_word)
        x = word.index("\n")
        word = word[:x]
        searched_word = searched_word[:x]

    time.sleep(2)

    # Game phase
    for letter in word:
        found_letters = found_letters + "-"

    print("\nThe word is: " + found_letters)

    while found_letters != searched_word and not user_tries == maximum_tries:

        user_letter = input("Enter a Letter: ")
        user_letter = user_letter.upper()
        Right_letter = False

        if word.count(user_letter) > 0:
            i = word.count(user_letter)
            for index in range(i):
                letter_index = (word.index(user_letter))
                index_list.append(letter_index)
                word[letter_index] = "*"
                Right_letter = True

        else:
            time.sleep(2)
            Right_letter = False
            used_letters.append(user_letter)

        if Right_letter:
            found_letters = ""

            for letter in searched_word:
                found_letters = found_letters + "-"

            temp = list(found_letters)

            for index in index_list:
                letters = searched_word[index]
                temp[index] = letters
            result = ''.join(temp)
            found_letters = str(result)

        else:
            user_tries += 1
            print("The Letter: " + user_letter + " is not in the word!\n")
            time.sleep(2)
            if user_tries == 1:
                phases.phase_1()
            elif user_tries == 2:
                phases.phase_2()
            elif user_tries == 3:
                phases.phase_3()
            elif user_tries == 4:
                phases.phase_4()
            elif user_tries == 5:
                phases.phase_5()
            elif user_tries == 6:
                phases.phase_6()

        time.sleep(2)
        print("\nThe word: " + found_letters + "\n")
        print("Wrong letters: ")
        for letter in used_letters:
            print(letter + ", ", end="")
        print("\n")
        print("_" * 82)

    if found_letters == searched_word:
        print("\n\n" + "*" * 29 + ' $You Won$ ' + "*" * 29 + "\n")

    elif user_tries == maximum_tries:
        print("The word was: " + searched_word)
        print("\n\n" + "*" * 29 + ' You Lost! Game Over ' + "*" * 29 + "\n")

    time.sleep(4)
    x = True
    while x:
        play_input = input("Do you want to play again? (a) Yes of course! (b) No maybe later. | Your answer: ")
        if play_input.lower() == "a":
            print("_" * 82)
            play_again = True
            x = False
            time.sleep(2)
        elif play_input.lower() == "b":
            play_again = False
            x = False
            time.sleep(2)
        else:
            time.sleep(2)
            print("The syntax: " + play_input + " is not recognized!\n")

# Comment Test
# Another Comment
