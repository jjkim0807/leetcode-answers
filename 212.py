import functools
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def findWord(board, word, start, ban):
            x, y = start
            if word == "" or word == None or word == board[x][y]:
                return True
            elif board[x][y] != word[0]:
                return False
            else:
                candidates = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
                for i, j in candidates:
                    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                        continue
                    elif (i, j) in ban:
                        continue
                    elif findWord(board, word[1:], (i, j), ban + [(x, y)]):
                        return True
                    else:
                        continue
                return False

        result = []
        for word in words:
            found = False
            for i, line in enumerate(board):
                if found:
                    break
                for j, c in enumerate(line):
                    if findWord(board, word, (i, j), []):
                        result.append(word)
                        found = True
                        break

        return result
