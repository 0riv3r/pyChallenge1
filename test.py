

key_array = list("0fffffffffffffffffffffffffffffff")
key_array = list("00000000000000000000000000000000")

for i in range(0, len(key_array)):
    print ''.join(key_array)
    key_array[i] = "1"
    print ''.join(key_array)

    d = int(key_array[i], 16)
    for j in range(0, 14):
        d += 1
        key_array[i] = hex(d).lstrip("0x1")
        print ''.join(key_array)

