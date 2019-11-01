from timer_cm import Timer
import subprocess
from tqdm import tqdm
from termcolor import colored
import sys

# key = "7781c66d36dc3a22447a6e5bf8c89090"

message = "First___we_take_Manhattan____then_we_take_Berlin"
key_array = list("00000000000000000000000000000000")
time_one_char = 0.077

pbar = tqdm(key_array)
found = []

original = sys.stdout
sys.stdout = open('./stdout.txt', 'w')
tmp = subprocess.call('clear',shell=True)


def set_output(out):
    cur_char = colored(str(out), 'red', 'on_green', attrs=['bold'])
    found.append(cur_char)
    pbar.update()
    pbar.set_description("Key: %s " % ''.join(found))

def breakit(key, i):
    cmd = "python sign.py " + key + " " + message
    with Timer('timing') as timer:
        p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
        (output, err) = p.communicate()
        if output:
            print "output : ", output
    if float(timer.elapsed) > (i*time_one_char):
        return True
    else:
        return False


with Timer('total') as total_time:
    for i in range(0, (len(key_array))/2):
        if breakit(''.join(key_array), i+1):
            set_output(key_array[i])
            continue
        key_array[i] = "1"
        if breakit(''.join(key_array), i+1):
            set_output(key_array[i])
            continue

        d = int(key_array[i], 16)
        for j in range(0, 14):
            d += 1
            key_array[i] = hex(d).lstrip("0x1")
            if breakit(''.join(key_array), i+1):
                set_output(key_array[i])
                break

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

# pip install timer_cm