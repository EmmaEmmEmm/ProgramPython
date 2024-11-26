def match(s1, s2):
    A = 0
    B = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            if s1[i]==s2[i]:
                A+=1
            else:
                B+=1
    return "{}A, {}B".format(A, B)
print(match("1234", "0123"))