import time
from Hangman_Phases import Phases
import random


# Functions&Classes

class Functions:
    #Variables
    def starter_variables(self):
        self.play_again = True
        self.letter_index = 100

    # Introduction
    def introduction(self):
        print("\n\n" + '*' * 37 + " Hangman " + '*' * 37 + "\n")
        print("""\
Description: You have to guess a word. As you guess wrong letters, you will get
                            hanged time to time. Good luck!""")

    # Gamemode (Multiplayer or Singleplayer)
    def gamemode(self):
        self.two_users = False
        self.single_player = False
        user_input = ""
        while not self.two_users and not self.single_player:
            user_input = input("\n(a) You are two players (b) You are one player | Your answer: ")
            if user_input.lower() == "a":
                self.two_users = True
            elif user_input.lower() == "b":
                self.single_player = True
            else:
                print("Error! The answer: " + user_input + " is not recognized.")

        return self.two_users, self.single_player, user_input

    # Gamemode Setup (two or one user)
    def gamemode_setup(self):
        word_entered = False
        self.searched_word = ""
        self.word = ""
        if self.two_users:
            while not word_entered:
                self.searched_word = input("\nPerson 1 enter your word here: ")
                self.searched_word = self.searched_word.upper()
                self.word = list(self.searched_word)
                user_answer = input("\nYour word is: " + self.searched_word +
                                    ". Do you want to proceed? (a) Yes (b) No | Your answer: ")
                if user_answer.lower() == "a":
                    word_entered = True
                elif user_answer.lower() == "b":
                    word_entered = False
                else:
                    print("Error! The answer: " + user_answer + " is not recognized.")
                i = 5
                while i <= 20 and word_entered:
                    print("/" * 37 + 'barrier!' + "/" * 37)
                    i += 1

        elif self.single_player:
            single_player_words = open("words.txt", "r")
            single_player_words = list(single_player_words)
            index_count = -1
            for indx in single_player_words:
                index_count += 1

            self.searched_word = (single_player_words[random.randint(0, index_count)])
            self.searched_word = self.searched_word.upper()
            self.word = list(self.searched_word)
            x = self.word.index("\n")
            self.word = self.word[:x]
            self.searched_word = self.searched_word[:x]

        return self.word, self.searched_word

    # create_found_letters
    def create_found_letters(self):
        self.found_letters = ""
        for letter in self.word:
            self.found_letters = self.found_letters + "-"

        print("\nThe word is: " + self.found_letters)

        return self.found_letters

    # While not lost or won
    def run_variables(self):
        self.user_tries = 0
        self.maximum_tries = 6
        self.index_list = []
        self.used_letters = []

        return self.maximum_tries, self.user_tries

    # Input letter
    def input_letter(self):
        self.user_letter = input("Enter a Letter: ")
        self.user_letter = self.user_letter.upper()

        return self.user_letter

    # check_float_letter
    def check_float_letter(self):
        self.Right_letter = False
        if self.word.count(self.user_letter) > 0:
            i = self.word.count(self.user_letter)
            for index in range(i):
                self.letter_index = (self.word.index(self.user_letter))
                self.index_list.append(self.letter_index)
                self.word[self.letter_index] = "*"
                self.Right_letter = True

        else:
            self.used_letters.append(self.user_letter)

            return self.Right_letter, self.index_list, self.used_letters, self.word

    # process_right_or_wrong
    def effect(self):
        self.phases = Phases()
        if self.Right_letter:
            self.found_letters = ""

            for letter in self.searched_word:
                self.found_letters = self.found_letters + "-"

            temp = list(self.found_letters)

            for index in self.index_list:
                letters = self.searched_word[index]
                temp[index] = letters
            result = ''.join(temp)
            self.found_letters = str(result)

        else:
            self.user_tries += 1
            print("The Letter: " + self.user_letter + " is not in the word!\n")
            if self.user_tries == 1:
                self.phases.phase_1()
            elif self.user_tries == 2:
                self.phases.phase_2()
            elif self.user_tries == 3:
                self.phases.phase_3()
            elif self.user_tries == 4:
                self.phases.phase_4()
            elif self.user_tries == 5:
                self.phases.phase_5()
            elif self.user_tries == 6:
                self.phases.phase_6()

        return self.index_list, self.found_letters

    # Output_Text (Presentation usw.)
    def output(self):
        print("\nThe word: " + self.found_letters + "\n")
        print("Wrong letters: ")
        for letter in self.used_letters:
            print(letter + ", ", end="")
        print("\n")
        print("_" * 82)

    # Check won or lost
    def won_or_lost(self):
        if self.found_letters == self.searched_word:
            print("\n\n" + "*" * 29 + ' $You Won$ ' + "*" * 29 + "\n")

        elif self.user_tries == self.maximum_tries:
            print("The word was: " + self.searched_word)
            print("\n\n" + "*" * 29 + ' You Lost! Game Over ' + "*" * 29 + "\n")

    # Ask play_again
    def ask_play_again(self):
        x = True
        while x:
            play_input = input("Do you want to play again? (a) Yes of course! (b) No maybe later. | Your answer: ")
            if play_input.lower() == "a":
                print("_" * 82)
                self.play_again = True
                x = False
            elif play_input.lower() == "b":
                self.play_again = False
                x = False
            else:
                print("The syntax: " + play_input + " is not recognized!\n")

        return self.play_again


# main

# Introduction
f = Functions()
f.introduction()
time.sleep(5)

# Gamephase

f.starter_variables()

while f.play_again:
    f.gamemode()
    time.sleep(1)
    f.gamemode_setup()
    time.sleep(2)
    f.create_found_letters()
    f.run_variables()

    while f.found_letters != f.searched_word and not f.user_tries == f.maximum_tries:
        f.input_letter()
        f.check_float_letter()
        f.effect()
        time.sleep(2)
        f.output()
        time.sleep(1)

    f.won_or_lost()
    time.sleep(5)
    f.ask_play_again()
