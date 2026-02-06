import random

score = 0

while score < 20:
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)
    ans = float(input(str(n1) + " · " + str(n2) + " = "))
    if ans == (n1 * n2):
        print("correct!!!! gud job yaya")
        score += 2
        print("score: ", str(score))
    else:
        print("YOU IS STUPID HOW YOU GET WONRG????? yo know ling ling can do it better because he practises 40 hours a day")
        score -= 1
        print("score: ", str(score))


print("CONGRATS!!! YOU HIT 20 SCORE!?!?!?!??!?!")
