import random

def rd(b=0):
    return random.randint(0,b)

def tc_gen(N):

    tc = []

    for i in range(N):
        tc.append([rd(5),rd(6),rd(100),rd(500),rd(60),rd(90),rd(15)])

    return tc