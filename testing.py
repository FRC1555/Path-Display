import math
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

reversedSeq = list(reversed(seq))
weirdSeq = list(reversed(seq[:-1]))

def run():
    #print(seq)
    #print(reversedSeq)
    #print(weirdSeq)

    x = 25
    y = -25

    theta = math.atan2(y, x)

    print((theta*180/math.pi))
#
run()
