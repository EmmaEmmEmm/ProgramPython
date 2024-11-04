def countScore(a):
    score = 0
    for i in range(len(a)):
        if a[i] == 'A':
            score += 1
        elif a[i] == 'J'or a[i] == 'Q'or a[i] == 'K':
            score += 0.5
        else:
            score += int(a[i])
    if score > 10.5:
        score = 0
    elif score % 1 == 0:
        score = int(score)
    return score
def error(a):
    test = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for i in a:
        if i not in test:
            return -1
    return a
def compare(c, p):
    if c > p:
        print("computer win " + str(p) + " " + str(c))
    elif c < p:
        print("player win " + str(p) + " " + str(c))
    else:
        print("tie " + str(c))
def main():
    player = error(input().split())
    computer = error(input().split())

    if player == -1 or computer == -1:
        print("Error input")
    else:
        pTotal = countScore(player)
        cTotal = countScore(computer)
        compare(cTotal, pTotal)
main()


