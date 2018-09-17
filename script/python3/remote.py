# -*- coding: utf-8 -*-
# this made for python3

from itertools import product
from fstrings import f # generally raspi python3 < 3.6
# When python updated over 3.6.0, you can replace f('...') to f'...', but this replaces dont have to do.

class Remote(object):

    NOTAVAILABLE = 'NA'
    def setupKeycode(self, keycodes):
        self.name = keycodes['name']
        self.keys = keycodes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def keys(self, position: tuple):
        """ key must be given by 2x2 list """
        assert(len(position) == 2)
        row, col  = position
        return self._keys[row][col]

    @keys.setter
    def keys(self, val):
        """
        _keys must be constructed as 2x2 list.
        see also. KEYCODE  0_0, 0_1, .... in yaml
        """
        self._keys = []
        check = lambda dict, key, default_val: dict[key] if key in dict.keys() else default_val
        for i in range(val['row_max']):
            self._keys.append([check(val, f('{x}_{y}'), self.NOTAVAILABLE) \
            for x, y in list(product([i], list(range(val['col_max']))))])