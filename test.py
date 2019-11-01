# import time
# import sys
#
# progress_1 = 'Process 1: {}%'
# progress_2 = 'Process 2: {}%'
# print
# print
#
# for i in range(100):
#     sys.stdout.write('\033[F')
#     sys.stdout.write('\033[F')
#     print(progress_1.format(i))
#     print(progress_2.format(i))
#     time.sleep(0.02)
from termcolor import colored, cprint
from tqdm import tqdm
import time


pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(1)

    text = colored(char, 'red', attrs=['reverse', 'blink'])

    pbar.set_description(" %s " % text)

# with tqdm(total=100) as pbar:
#     for i in range(10):
#         time.sleep(0.1)
#         pbar.update(10)