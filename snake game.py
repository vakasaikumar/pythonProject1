import random as r
s1 = 0
s2 = 0
while True:
    p = int(input("\nEnter player no:"))
    d = r.randint(1, 6)
    print(" Dice score: ", d)
    if p == 1:
        s1 = s1 + d
        if s1 == 7:
            print(" You Got ladder")
            s1 = s1 + 25
        elif s1 == 21:
            s1 = s1 + 41
            print(" You Got ladder")
        elif s1 == 35:
            s1 = s1 + 61
            print(" You Got ladder")
        elif s1 == 48:
            s1 = s1 + 36
            print(" You Got ladder")
        elif s1 == 60:
            s1 = s1 + 29
            print(" You Got ladder")
        elif s1 == 24:
            s1 = s1 - 20
            print(" You caught by snake")
        elif s1 == 49:
            s1 = s1 - 29
            print(" You caught by snake")
        elif s1 == 73:
            s1 = s1 - 36
            print(" You caught by snake")
        elif s1 == 98:
            s1 = s1 - 70
            print(" You caught by snake")
        if s1 > 100:
            s1=s1 - d
        if s1 == 100:
            print(" Player 1 is winner")
            exit(0)

    print(" Player 1: ", s1)

    if p == 2:
        s2 = s2 + d
        if s2 == 7:
            s2 = s2 + 25
            print(" You Got ladder")
        elif s2 == 21:
            s2 = s2 + 41
            print(" You Got ladder")
        elif s2 == 35:
            s2 = s2 + 61
            print(" You Got ladder")
        elif s2 == 48:
            s2 = s2 + 36
            print(" You Got ladder")
        elif s2 == 60:
            s2 = s2 + 29
            print(" You Got ladder")
        elif s2 == 24:
            s2 = s2 - 20
            print(" You caught by snake")
        elif s2 == 49:
            s2 = s2 - 29
            print(" You caught by snake")
        elif s2 == 73:
            s2 = s2 - 36
            print(" You caught by snake")
        elif s2 == 98:
            s2 = s2 - 70
            print(" You caught by snake")
        if s2 > 100:
            s2=s2 - d
            print(" You caught by snake")
        if s2 == 100:
            print(" Player 2 is winner")
            exit(0)
    print(" Player 2: ", s2)
