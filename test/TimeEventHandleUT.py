import time
import unittest
from source.TimeEventHandle import TimeEventHandle as TeH


class TimeEventHandleUT(unittest.TestCase):
    def test_run_speed_0(self):
        """
        Test TimeEventHandle.run() with speed 0
        :return:
        """
        e = TeH()
        e.set_speed(0)
        g = e.run()
        for i in range(100):
            next(g)
        self.assertEqual(e.time_between_starts(), (0, 0, 0, 0, 0))

    def test_run_speed_1(self):
        """
        Test TimeEventHandle.run() with speed 1
        :return:
        """
        e = TeH()
        speed = 1
        e.set_speed(speed)
        g = e.run()
        runtime = 1
        for i in range(runtime):
            time.sleep(e.speed_enum[speed]['time_wait_sec'])
            next(g)
        self.assertEqual((0, 0, 0, 0, runtime), e.time_between_starts())

        for i in range(runtime):
            next(g)
        self.assertEqual((0, 0, 0, 0, runtime), e.time_between_starts())  # check is not incremented

    def test_run_speed_2(self):
        """
        Test TimeEventHandle.run() with speed 2
        :return:
        """
        e = TeH()
        speed = 2
        e.set_speed(speed)
        g = e.run()
        runtime = 5
        for i in range(runtime):
            time.sleep(e.speed_enum[speed]['time_wait_sec'])
            next(g)
        self.assertEqual((0, 0, 0, 0, runtime), e.time_between_starts())

    def test_run_speed_3(self):
        """
        Test TimeEventHandle.run() with speed 3
        :return:
        """
        e = TeH()
        speed = 3
        e.set_speed(speed)
        g = e.run()
        runtime = 5
        for i in range(runtime):
            time.sleep(e.speed_enum[speed]['time_wait_sec'])
            next(g)
        self.assertEqual((0, 0, 0, 0, runtime), e.time_between_starts())

    def test_change_pause_to_run(self):
        e = TeH()
        speed = 3
        e.set_speed(speed)
        g = e.run()
        runtime = 5
        for i in range(runtime):
            time.sleep(e.speed_enum[speed]['time_wait_sec'])
            next(g)
        e.set_speed(0)
        next(g)
        next(g)
        self.assertEqual((0, 0, 0, 0, runtime), e.time_between_starts())  # check is not incremented
        time.sleep(0.1)
        e.set_speed(speed)
        next(g)
        self.assertEqual((0, 0, 0, 0, runtime+1), e.time_between_starts())  # check is incremented just one

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TimeEventHandleUT)
    unittest.TextTestRunner(verbosity=2).run(suite)
