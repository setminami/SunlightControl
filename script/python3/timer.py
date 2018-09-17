# -*- coding: utf-8 -*-
# this made for python3

from threading import Thread
from datetime import datetime
import sys, logging, pytz
from fstrings import f # generally raspi python3 < 3.6
# When python updated over 3.6.0, you can replace f('...') to f'...', but this replaces dont have to do.

class LEDLightDayTimer(Thread):
    """ a simple day timer """

    @property
    def timezone(self):
        return self._TZ
    @timezone.setter
    def timezone(self, val):
        assert val in pytz.all_timezones, "Timezone not valid."
        self._TZ = pytz.timezone(val)

    def regist(self, f):
        pass

    def unregist(self, f):
        pass

    def is_just_or_passed_now(self, time):
        """
        time: str [hh:mm]
        just time or passed : return True
        not passed: return False
        """
        assert time.count(':') == 1, f('Illegal time format Found. {time}')
        h, m = time.split(':')
        now = datetime.now(self._TZ)
        check = datetime(*(now.year, now.month, now.day, h, m, 0, 0, self._TZ))
        return now > check



    def run(self):
        pass