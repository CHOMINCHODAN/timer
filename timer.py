# Timer
import time

class Timer:
    def __init__(self):
        self.hour_value = 0
        self.min_value = 0
        self.sec_value = 0
        self.start_value = 0

    def set_hour(self, get_hour_value: int):
        self.hour_value = get_hour_value * 60 * 60

    def set_min(self, get_min_value: int):
        self.min_value = get_min_value * 60

    def set_sec(self, get_sec_value: int):
        self.sec_value = get_sec_value

    def set_start(self, get_hour_value: int, get_min_value: int, get_sec_value: int ):
        self.start_value =  get_hour_value + get_min_value + get_sec_value



if __name__ == '__main__':
    timer = Timer()         # 계산기를 만들었다.

    timer.set_hour(2)        #
    timer.set_min(2)
    timer.set_sec(2)

    print(timer.hour_value)
    print(timer.min_value)
    print(timer.sec_value)






