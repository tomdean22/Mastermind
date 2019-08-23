from collections import namedtuple
from random import sample, shuffle, randint


class Colors:
    colors = [
        'red',
        'blue',
        'green',
        'purple',
        'yellow',
        'orange'
    ]

    def __len__(self):
        return len(Colors.colors)

Pair = namedtuple('Pair', 'position color')

class SecretCode:
    DEFAULT_SIZE = 3

    def __init__(self, size=DEFAULT_SIZE):
        assert(size < len(Colors.colors)), f'There are {len(Colors.colors)} colors!'
        self._size = size
        self._code = None

    def __repr__(self):
        return ' '.join([str(pair) for pair in self.code])

    def __len__(self):
        return self._size

    def __iter__(self):
        return iter(self.code)

    def _newCode(self):
        # a random list of non-repeating numbers with length: self._size and range: 0 - len(Colors.colors)
        selection = sample(range(len(Colors.colors)), self._size)
        return [Pair(pos, color) for pos, color in enumerate([Colors.colors[i] for i in selection])]

    @property
    def code(self):
        if not self._code:
            self._code = self._newCode()
        return self._code

    def resetCode(self, size=DEFAULT_SIZE):
        self._size = size
        self._code = None







# - create code
# - collect guesses from player
# - iterate through the positions
#   • list available colors
#   • record choice
#   • clean choice
#     > if clean: create Card(pos, choice) and append to self._guesses
#     > if dirty: ask again
# - check guesses
#   • iterate through guesses and code
#     > pos & color are correct: append black card to self.clues
#     > color is correct, but in the wrong position: append brown card to self.clues
#     > neither are correct: pass