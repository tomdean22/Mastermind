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

Card = namedtuple('Card', 'position color')

class Deck:
    DEFAULT_SIZE = 3

    def __init__(self, size=DEFAULT_SIZE):
        assert(size < len(Colors.colors)), f'There are {len(Colors.colors)} colors!'
        self._size = size
        self._deck = None

    def __str__(self):
        return '\n'.join([str(card.position) + ' ' + card.color for card in self.deck])

    def __repr__(self):
        return ' '.join([str(card) for card in self.deck])

    def __len__(self):
        return self._size

    def __iter__(self):
        return iter(self.deck)

    def _newDeck(self):
        selection = sample(range(len(Colors.colors)), self._size)
        return [Card(pos, col) for pos, col in enumerate([Colors.colors[i] for i in selection])]

    @property
    def deck(self):
        if not self._deck:
            self._deck = self._newDeck()
        return self._deck

    @deck.setter
    def deck(self, size):
        assert(size < len(Colors.colors)), f'There are only {len(Colors.colors)} colors!'
        self._size = size
        self._deck = self._newDeck()

    def resetDeck(self, size=DEFAULT_SIZE):
        self._size = size
        self._deck = None







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