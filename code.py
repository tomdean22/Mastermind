from collections import namedtuple
from random import sample, shuffle


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
        """Initialize a new secret code"""
        assert(size < len(Colors.colors)), f'Maximum: {len(Colors.colors)-1}'
        self._size = size
        self.code = self._newCode()

    def __repr__(self):
        return ' '.join([str(pair) for pair in self.code])

    def __iter__(self):
        return iter(self.code)

    def _newCode(self):
        """
        Generates a random sample of non-repeating numbers  with length: self._size and range: 0 ≤ i < len(Colors.colors).
        Returns a list of namedTuples (position, color) using the sample as the color ordering.
        """
        selection = sample(range(len(Colors.colors)), self._size)
        return [Pair(pos, color) for pos, color in enumerate([Colors.colors[i] for i in selection])]

    def resetCode(self, size=DEFAULT_SIZE):
        """Return a new secret code"""
        assert(size < len(Colors.colors)), f'Maximum: {len(Colors.colors)-1}'
        self._size = size
        self.code = self._newCode()
