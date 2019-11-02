from timer_cm import Timer
import subprocess
from tqdm import tqdm
from termcolor import colored
import sys


# Message to be signed
message = "First___we_take_Manhattan____then_we_take_Berlin"
key_array = list("00000000000000000000000000000000")


# The one-char test benchmark
# Should be a bit more than the max time it takes to respond to one false char
# If the response is greater than this benchmark, the tested char is true
# Has to be adjusted for the target machine running the sign app
time_one_char = 0.100


# The progressbar object
pbar = tqdm(key_array)
# The discovered key chars array to be prined out on the progressbar
found = []


# Taking control of the stdout
original = sys.stdout
sys.stdout = open('./stdout.txt', 'w')
tmp = subprocess.call('clear',shell=True)


# Manage the progressbar
# char out (the new char to add to the so far recovered key)
def set_output(out):
    cur_char = colored(str(out), 'green', attrs=['bold'])
    found.append(cur_char)
    pbar.update()
    pbar.set_description("Key: %s " % ''.join(found))


# Try the next key
# string key (the key with the updated char)
# int i (to multiply the benchmark with the i passed chars + 1)
def breakit(key, i):
    cmd = "python sign.py " + key + " " + message
    # Measure the time it takes for the response
    with Timer('timing') as timer:
        # Execute the cmd with catching the stderr
        p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
        (output, err) = p.communicate()
        # printout only the successful signed message
        if output:
            print "output : ", output
    # Is the response-time greater than the benchmark
    # Multiplying the benchmark time with the number of already passed chars
    if float(timer.elapsed) > (i*time_one_char):
        return True
    else:
        return False


# Manage the generating of the key
# Also measure the total time it takes to discover the whole key
with Timer('total') as total_time:
    for i in range(0, (len(key_array))):
        # Pass also i+1 because it is used to multiply the number of passed chars
        if breakit(''.join(key_array), i+1):
            # add the new discovered char to the printed key
            set_output(key_array[i])
            continue
        # Have to seperately test for '1' because 
        # the hex filter below filters out also the right hex digit if it is '1'
        key_array[i] = "1"
        if breakit(''.join(key_array), i+1):
            set_output(key_array[i])
            continue

        d = int(key_array[i], 16)
        for j in range(0, 14):
            # will begin with d == 2
            d += 1
            # encode in hex
            # remove the hex preface 0x
            # remove the hex left digit which here will always be equql to 1
            key_array[i] = hex(d).lstrip("0x1")
            # test the key with this last char
            if breakit(''.join(key_array), i+1):
                set_output(key_array[i])
                break


# return the original stdout to printout the signed message
sys.stdout = original
tmp = subprocess.call('clear',shell=True)
print ""
print "Total runtime: ",
microseconds = total_time.elapsed * 60
seconds, microseconds = divmod(microseconds, 60)
minutes, seconds = divmod(seconds, 60)
print "%02d:%02d:%02d"%(minutes, seconds, microseconds)
print ""




###############################################################

# python hacker.py

# Python 2.7.17rc1

# pip install timer_cm
# pip install tqdm
# pip install termcolor

# key = "7781c66d36dc3a22447a6e5bf8c89090"
