import time

def currenttime():
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    # 22:30:45
    curr_clock = curr_clock.split(":")
    curr_clock = curr_clock[0] + curr_clock[1]
    curr_clock = int(curr_clock)

    return curr_clock