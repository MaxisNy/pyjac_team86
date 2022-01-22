import time


class Timer:
    """
    The Timer class that keeps track of the current time and
    the time elapsed since the set-up.
    """

    time: float     # current time

    # TODO: do we need this constructor at all???
    def __init__(self):
        self.time = 0

    def get_time(self):
        """
        Returns the current value of time.
        """
        return self.time

    def get_time_elapsed(self):
        """
        Returns the time elapsed since it was set.
        """
        return time.time() - self.time

    def start(self):
        """
        Sets the current time to be the point-reference.
        """
        self.time = time.time()
