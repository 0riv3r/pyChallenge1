from timer_cm import Timer
import os

# key = "7781c66d36dc3a22447a6e5bf8c89090"

message = "First___we_take_Manhattan____then_we_take_Berlin"
key_array = list("00000000000000000000000000000000")
time_one_char = 0.075

def breakit(key, i):
    cmd = "python sign.py " + key + " " + message
    with Timer('timing') as timer:
        os.system(cmd)
    if float(timer.elapsed) > (i*time_one_char):
        return True
    else:
        return False


with Timer('total') as total_time:
    for i in range(0, (len(key_array))/4):
        if breakit(''.join(key_array), i+1):
            print key_array
            continue
        key_array[i] = "1"
        if breakit(''.join(key_array), i+1):
            print key_array
            continue

        d = int(key_array[i], 16)
        for j in range(0, 14):
            d += 1
            key_array[i] = hex(d).lstrip("0x1")
            if breakit(''.join(key_array), i+1):
                print key_array
                break
total_time.elapsed





###############################################################

# python hacker.py

# pip install timer_cm