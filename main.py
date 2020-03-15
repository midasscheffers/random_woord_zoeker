import math as m
import random as r

x_size = ''
y_size = ''
word_count = ''
min_word_len = 3
max_word_len = 15
while not isinstance(x_size, int):
    try:
        x_size = int(input("Hoe breed moet het veld zijn: "))
    except:
        print("is not a number")
while not isinstance(y_size, int):
    try:
        y_size = int(input("Hoe hoog moet het veld zijn: "))
    except:
        print("is not a number")
while not isinstance(word_count, int):
    try:
        word_count = int(input("Hoe veel woorden moeten er zijn: "))
    except:
        print("is not a number")


#want to add supurt for fille reading later
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# characters = [' ', '!', '@']
words = []


def generate_rand_board(x_size, y_size):
    board = [[characters[r.randrange(0, len(characters))] for x in range(x_size)] for y in range(y_size)]
    return board

def print_board(board):
    for line in board:
        for c in line:
            print(c, end=", ")
        print()


def print_words(words):
    for word in words:
        for letter in word[0]:
            print(letter, end="")
        print()


def random_pos(x_size, y_size):
    return [r.randrange(0, x_size), r.randrange(0, y_size)]


def generate_words(board, x_size, y_size):
    words = []
    for i in range(word_count):
        word_letters = []
        while len(word_letters) < min_word_len:
            word_letter_pos = []
            word_letters = []
            start_pos = random_pos(x_size, y_size)
            direct = [0,0]
            while direct == [0,0]:
                direct = [r.randint(-1, 1), r.randint(-1, 1)]
            for j in range(r.randint(min_word_len, max_word_len)):
                if start_pos[0] + j*direct[0] < 0 or start_pos[0] + j*direct[0] >= x_size:
                    break
                if start_pos[1] + j*direct[1] < 0 or start_pos[1] + j*direct[1] >= x_size:
                    break
                word_letter_pos.append([start_pos[0] + j*direct[0], start_pos[1] + j*direct[1]])
                word_letters.append(board[start_pos[1] + j*direct[1]][start_pos[0] + j*direct[0]])
        words.append([word_letters, word_letter_pos])
    return words


board = generate_rand_board(x_size, y_size)
words = generate_words(board, x_size, y_size)
print()
print_board(board)
print()
print_words(words)
print()





