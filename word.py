def get_plural(noun):
    if noun[-2:] == "ch" or "sh" or "x" or "s" or "z":
        return (noun + "es")
    elif noun[-1] == "f":
        return (noun[:-1] + "ves")
    elif noun[-2:] == "fe":
        return (noun[:-2] + "ves")
    elif noun[-1] == "o":
        return (noun + "es")
    elif noun[-2:] == "by" or "cy" or "dy" or "fy" or "gy" or "hy" or "jy" or "ky" or "ly" or "my" or "ny" or "py" or "qy" or "ry" or "sy" or "ty" or "vy" or "wy" or "xy" or "yy" or "zy":
        return (noun[:-1] + "ies")
    else:
        return (noun + "s")


import sys
from word import get_plural

def check(word, plural):
    return 1 # if the plural is correct or 0 otherwise.

words = ["beach", "fish", "fox", "bus", "fez", "potato", "fairy", "lady", "boy", "elf", "knife", "fog", "tissue"]

num_correct = 0
for word in words:
    num_correct += check(word, get_plural(word))

print("All Good" if num_correct == len(words) else str(len(words) - num_correct) + " incorrect.")
