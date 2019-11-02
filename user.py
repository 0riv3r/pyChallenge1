import os

KEY = "7781c66d36dc3a22447a6e5bf8c89090"
MESSAGE = "*authentic__msg*"

cmd = "python sign.py " + KEY + " " + MESSAGE
os.system(cmd)
print
