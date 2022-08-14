"""

"""
from datetime import timedelta
from datetime import datetime
import time
from dateutil.relativedelta import relativedelta


class TimeEventHandle:
    def __init__(self):
        self._start_time = datetime.now()
        self.now = self._start_time
        self.time_format = '%d/%m/%Y %H:%M'
        self.speed_enum = {0: {'name': 'PAUSE',  'time_wait_sec': 0.0},
                           1: {'name': 'SLOW',   'time_wait_sec': 1.0},
                           2: {'name': 'NORMAL', 'time_wait_sec': 0.1},
                           3: {'name': 'FAST',   'time_wait_sec': .01}
                           }
        self._time_wait_for_speed = [self.speed_enum[_i]['time_wait_sec'] for _i in range(len(self.speed_enum))]  # time in seconds
        self._real_time_last_increment = self.now
        self._speed = 0
        self._stop_run = False

    def set_speed(self, speed: int):
        self._speed = speed

    def stop(self):
        self._stop_run = True

    def __now_str(self):
        return self.now.strftime(self.time_format)

    def run(self):
        """
        The function runs a while loop that checks if the stop_run flag is set to True. If it is not, it waits for a certain
        amount of time (depending on the speed) and then increments the time by one minute
        """
        while not self._stop_run:
            if self._speed == 0:
                pass
            elif self.__need_to_increment():
                self.now = self.now + timedelta(minutes=1)
                self._real_time_last_increment = datetime.now()
            yield self.__now_str()

    def time_between_starts(self):
        """
        It takes the current time and the time the program started and returns the difference in years, months, days, hours,
        and minutes.
        """
        diff = relativedelta(self.now, self._start_time)
        return diff.years, diff.months, diff.years, diff.hours, diff.minutes

    def __need_to_increment(self):
        delta = datetime.now() - self._real_time_last_increment
        return delta.total_seconds() > self._time_wait_for_speed[self._speed]


if __name__ == '__main__':
    # time_format = '%d/%m/%Y %H:%M:%S'
    # now = datetime.now()
    # print(f'now   {now.strftime(time_format)}')
    # now_1 = now + timedelta(seconds=1)
    # print(f'now 1 {now_1.strftime(time_format)}')
    tEh = TimeEventHandle()
    g = tEh.run()
    tEh.set_speed(3)
    for i in range(1000):
        e = next(g)
        print('\r\033[K', end='')
        print(e, end='')
    print('\n')
    print(tEh.time_between_starts())
