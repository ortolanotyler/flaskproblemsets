#TESTING EXCERCISES

from random import choice
import string

class Boggle:

    def __init__(self):
        self.words = self.read_dict("words.txt")

    def read_dict(self, dict_path):
        with open(dict_path) as dict_file:
            return [word.strip() for word in dict_file]

    def make_board(self):
        board = []
        for y in range(5):
            row = [choice(string.ascii_uppercase) for _ in range(5)]
            board.append(row)
        return board

    def check_valid_word(self, board, word):
        word_exists = word in self.words
        valid_word = self.find(board, word.upper())

        if word_exists and valid_word:
            result = "ok"
        elif word_exists and not valid_word:
            result = "not-on-board"
        else:
            result = "not-word"

        return result

    def find_from(self, board, word, y, x, seen):
        if x > 4 or y > 4:
            return

        if board[y][x] != word[0]:
            return False

        if (y, x) in seen:
            return False

        if len(word) == 1:
            return True

        seen = seen | {(y, x)}

        neighbors = [(y-1, x), (y+1, x), (y, x-1), (y, x+1),
                     (y-1, x-1), (y+1, x+1), (y-1, x+1), (y+1, x-1)]

        for ny, nx in neighbors:
            if self.find_from(board, word[1:], ny, nx, seen):
                return True

        seen.remove((y, x))
        return False

    def find(self, board, word):
        for y in range(0, 5):
            for x in range(0, 5):
                if self.find_from(board, word, y, x, seen=set()):
                    return True
        return False
