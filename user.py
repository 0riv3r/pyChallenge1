import os

key = "7781c66d36dc3a22447a6e5bf8c89090"
message = "*authentic__msg*"

cmd = "python sign.py " + key + " " + message

os.system(cmd)
